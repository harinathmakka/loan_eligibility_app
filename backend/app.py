# backend/app.py  — full file (replace existing)

import traceback
import os
from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
from database.db import get_db_connection
from utils.preprocess import preprocess_input
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')

app = Flask(__name__)
CORS(app)

# Configurable prediction threshold (use env var PRED_THRESHOLD, default 0.30)
PRED_THRESHOLD = float(os.getenv("PRED_THRESHOLD", "0.25"))

# Load model (ensure file exists at model/xgboost_model.joblib)
MODEL_PATH = "model/xgboost_model.joblib"
try:
    model = joblib.load(MODEL_PATH)
    logging.info("Loaded model from %s", MODEL_PATH)
except Exception as e:
    logging.exception("Failed to load model: %s", e)
    raise

@app.route("/")
def health():
    return "Loan Eligibility Backend Running Successfully"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        logging.info("Received predict request: %s", data)

        # Preprocess input (returns a pandas DataFrame with one row)
        processed = preprocess_input(data)

        # Ensure numeric type
        processed = processed.astype(float)

        # Determine expected features from model (XGBoost booster or sklearn attr)
        expected_features = None
        try:
            # For XGBClassifier: get booster feature names
            expected_features = model.get_booster().feature_names
        except Exception:
            # Fall back to scikit-learn attribute (if present)
            if hasattr(model, "feature_names_in_"):
                expected_features = list(model.feature_names_in_)
            elif hasattr(model, "get_feature_names_out"):
                try:
                    expected_features = list(model.get_feature_names_out())
                except Exception:
                    expected_features = list(processed.columns)
            else:
                expected_features = list(processed.columns)

        # Ensure all expected_features exist in processed; if missing, add zero columns
        for feat in expected_features:
            if feat not in processed.columns:
                processed[feat] = 0.0

        # Reorder columns exactly as expected
        processed = processed[expected_features]

        # Predict probability (works if model supports predict_proba)
        if hasattr(model, "predict_proba"):
            proba_array = model.predict_proba(processed)
            probability = float(proba_array[0][1])
        else:
            # fallback to predict (binary)
            pred = model.predict(processed)
            probability = float(pred[0])

        # Use configurable threshold
        prediction = "Rejected" if probability > PRED_THRESHOLD else "Approved"

        # Insert into DB (safe extraction)
        conn = get_db_connection()
        cursor = conn.cursor()

        sql = """
            INSERT INTO predictions (
                age, income, loan_amount, credit_score, months_employed,
                num_credit_lines, interest_rate, loan_term, dti_ratio,
                education, employment_type, marital_status,
                has_mortgage, has_dependents, loan_purpose, has_cosigner,
                prediction, probability
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        def get_val(k, cast=str, default=None):
            v = data.get(k, default)
            if v is None:
                return None
            try:
                return cast(v)
            except Exception:
                return default

        values = (
            get_val('age', int, None),
            get_val('income', float, None),
            get_val('loan_amount', float, None),
            get_val('credit_score', int, None),
            get_val('months_employed', int, None),
            get_val('num_credit_lines', int, None),
            get_val('interest_rate', float, None),
            get_val('loan_term', int, None),
            get_val('dti_ratio', float, None),
            get_val('education', str, None),
            get_val('employment_type', str, None),
            get_val('marital_status', str, None),
            get_val('has_mortgage', str, None),
            get_val('has_dependents', str, None),
            get_val('loan_purpose', str, None),
            get_val('has_cosigner', str, None),
            prediction,
            probability
        )

        cursor.execute(sql, values)
        conn.commit()
        cursor.close()
        conn.close()

        logging.info("Inserted prediction into DB; prediction=%s probability=%s threshold=%s",
                     prediction, probability, PRED_THRESHOLD)

        return jsonify({"prediction": prediction, "probability": probability, "threshold": PRED_THRESHOLD})

    except Exception as e:
        logging.error("Error in /predict: %s", e)
        logging.error(traceback.format_exc())
        return jsonify({"error": "Internal server error", "detail": str(e)}), 500

@app.route("/history", methods=["GET"])
def history():
    try:
        n = int(request.args.get('n', 20))
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM predictions ORDER BY created_at DESC LIMIT %s", (n,))
        rows = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify({"history": rows})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
