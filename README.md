📘 Loan Eligibility Prediction Web Application

A full-stack machine learning project that predicts whether a customer will be approved or rejected for a loan based on financial & demographic inputs.
Built using Flask (backend), XGBoost ML model, MySQL, and a simple HTML/JS frontend.

⭐ Project Highlights

End-to-end machine learning model trained on 255K+ customer loan records.

XGBoost classifier used as final model (best F1-score among Logistic Regression, Random Forest, XGBoost).

Clean REST API backend (Flask) supporting prediction + database logging.

MySQL database integration to store prediction history.

Frontend UI for user inputs and instant results.

Fully deployed locally; structured and production-ready code.

📂 Project Structure
loan_eligibility_app/
│
├── backend/
│   ├── app.py                 # Flask API Server
│   ├── requirements.txt       # Python dependencies
│   ├── model/
│   │   └── xgboost_model.joblib
│   ├── utils/
│   │   └── preprocess.py      # Input preprocessing (one-hot + numerical)
│   ├── database/
│   │   └── db.py              # MySQL connection & helper
│   └── venv/                  # Virtual environment (ignored in git)
│
├── frontend/
│   ├── index.html             # Minimal, clean UI for loan inputs
│
└── README.md

🧠 Machine Learning Summary
✔ Dataset

File: Loan_default.csv

Size: 255,347 records

Target: Default (0 = No Default, 1 = Default)

Categorical variables encoded using One-Hot Encoding

Numerical variables scaled where appropriate

Irrelevant fields like LoanID removed

🧪 Models Trained
Model	Accuracy	Precision	Recall	F1-Score
Logistic Regression	0.885	0.60	0.02	0.05
Random Forest	0.887	0.63	0.04	0.08
XGBoost (Final)	0.886	0.55	0.08	0.14
🎯 Final Model:

👉 XGBoost Classifier (best F1-score on imbalanced dataset)

🧰 Tech Stack
Backend

Python 3.10

Flask

Flask-CORS

XGBoost

Scikit-Learn

Pandas & NumPy

MySQL Connector

Frontend

HTML

CSS

Vanilla JavaScript (fetch API)

Database

MySQL (local)

🚀 How to Run the Application (Local Setup)
1️⃣ Start MySQL Server
sudo service mysql start


Create database:

CREATE DATABASE loan_app;
USE loan_app;


Create predictions table:

CREATE TABLE predictions (
    id INT AUTO_INCREMENT PRIMARY KEY,
    age INT,
    income FLOAT,
    loan_amount FLOAT,
    credit_score INT,
    months_employed INT,
    num_credit_lines INT,
    interest_rate FLOAT,
    loan_term INT,
    dti_ratio FLOAT,
    education VARCHAR(50),
    employment_type VARCHAR(50),
    marital_status VARCHAR(50),
    has_mortgage VARCHAR(10),
    has_dependents VARCHAR(10),
    loan_purpose VARCHAR(50),
    has_cosigner VARCHAR(10),
    prediction VARCHAR(20),
    probability FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


Create MySQL user:

DROP USER IF EXISTS 'loan_user'@'localhost';
CREATE USER 'loan_user'@'localhost' IDENTIFIED BY 'prasad123';
GRANT ALL PRIVILEGES ON loan_app.* TO 'loan_user'@'localhost';
FLUSH PRIVILEGES;

2️⃣ Setup Backend

Navigate to backend folder:

cd loan_eligibility_app/backend


Create virtual environment:

python3 -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Run the API:

python app.py


Backend will start on:

http://127.0.0.1:5000

3️⃣ Run Frontend

Open:

loan_eligibility_app/frontend/index.html


in any browser.

You will see the Loan Eligibility Form.

🖥️ API Documentation
POST /predict

Request Body (JSON)

{
  "age": 25,
  "income": 500000,
  "loan_amount": 200000,
  "credit_score": 800,
  "months_employed": 48,
  "num_credit_lines": 1,
  "interest_rate": 10,
  "loan_term": 60,
  "dti_ratio": 0.45,
  "education": "High School",
  "employment_type": "Employed",
  "marital_status": "Single",
  "has_mortgage": "No",
  "has_dependents": "No",
  "loan_purpose": "Business",
  "has_cosigner": "No"
}


Response

{
  "prediction": "Approved",
  "probability": 0.19
}


All predictions are stored in MySQL.

🎨 UI Preview

✔ Clean, modern form
✔ Hints for each field
✔ Probability + Approval/Rejection badge
✔ Works instantly with backend API

📌 Key Features
✔ Fully functional ML pipeline

From preprocessing → training → evaluation → saving model → serving via API.

✔ Real-time prediction

Frontend collects user input → sends to Flask → returns result instantly.

✔ Database logging

Every prediction saved in MySQL.

✔ Modular backend

preprocess.py = feature processing

db.py = MySQL connection

app.py = API router

✔ Clean and readable code
📈 Future Improvements

(To upgrade for resume + job applications)

Add SHAP explainability

Add charts in frontend (Feature importance, history trends)

Add prediction history page

Add (JWT) login for admin

Deploy backend + frontend online

Convert UI to React.js version

Add SMOTE / class-weight improvements

🏁 Conclusion

This project demonstrates strong capability in:

✔ Machine Learning (EDA → Model → Evaluation)
✔ Backend Development (Flask REST API)
✔ Data Engineering (MySQL integration)
✔ Frontend Development (HTML/JS)
✔ Full-Stack ML Deployment

Perfect for Data Analyst, ML Engineer, Data Scientist, BFSI roles, and full-stack developer positions.