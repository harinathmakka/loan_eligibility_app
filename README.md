# 📘 Loan Eligibility Prediction Web Application

A full-stack machine learning application that predicts whether a customer is **Approved** or **Rejected** for a loan based on financial & demographic inputs.
Built using **Flask (API)**, **XGBoost ML model**, **MySQL DB**, and **HTML/JS frontend**.

---

# ⭐ Project Highlights

* End-to-end ML pipeline trained on **255K+ loan records**
* **XGBoost** selected as final model (best F1-score)
* Clean REST API backend (Flask)
* MySQL database integration for prediction history
* Simple, responsive frontend UI
* Modular, production-ready project structure

---

# 📂 Project Structure

```
loan_eligibility_app/
│
├── backend/
│   ├── app.py                 # Flask API Server
│   ├── requirements.txt       # Python dependencies
│   ├── model/
│   │   └── xgboost_model.joblib
│   ├── utils/
│   │   └── preprocess.py      # Input preprocessing
│   ├── database/
│   │   └── db.py              # MySQL connection
│   └── venv/                  # Virtual environment (ignored in git)
│
├── frontend/
│   ├── index.html             # UI for loan inputs
│
└── README.md
```

---

# 🧠 Machine Learning Summary

### ✔ Dataset

* File: **Loan_default.csv**
* Size: **255,347 records**
* Target: **Default** (0 = No, 1 = Yes)
* Categorical → One-Hot Encoding
* Numerical → Scaling
* Removed irrelevant fields (LoanID etc.)

---

# 🧪 Models Trained

| Model               | Accuracy | Precision | Recall | F1-Score |
| ------------------- | -------- | --------- | ------ | -------- |
| Logistic Regression | 0.885    | 0.60      | 0.02   | 0.05     |
| Random Forest       | 0.887    | 0.63      | 0.04   | 0.08     |
| **XGBoost (Final)** | 0.886    | 0.55      | 0.08   | 0.14     |

### 🎯 Final Model Used

**XGBoost Classifier** (best performer on imbalanced dataset)

---

# 🧰 Tech Stack

### Backend

* Python 3.10
* Flask + Flask-CORS
* XGBoost
* Scikit-Learn
* Pandas, NumPy
* MySQL Connector

### Frontend

* HTML
* CSS
* JavaScript (Fetch API)

### Database

* MySQL (local)

---

# 🚀 How to Run the Application (Local Setup)

## 1️⃣ Start MySQL Server

```sh
sudo service mysql start
```

### Create Database

```sql
CREATE DATABASE loan_app;
USE loan_app;
```

### Create Predictions Table

```sql
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
```

### Create MySQL User

```sql
DROP USER IF EXISTS 'loan_user'@'localhost';
CREATE USER 'loan_user'@'localhost' IDENTIFIED BY 'prasad123';
GRANT ALL PRIVILEGES ON loan_app.* TO 'loan_user'@'localhost';
FLUSH PRIVILEGES;
```

---

## 2️⃣ Setup Backend

```sh
cd loan_eligibility_app/backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Backend runs at:

👉 [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 3️⃣ Run Frontend

Simply open:

```
loan_eligibility_app/frontend/index.html
```

---

# 🖥️ API Documentation

### **POST /predict**

#### Request Body

```json
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
```

#### Example Response

```json
{
  "prediction": "Approved",
  "probability": 0.19
}
```

*All predictions are stored in MySQL.*

---

# 📌 Key Features

✔ End-to-end ML pipeline
✔ Real-time predictions
✔ MySQL logging
✔ Modular backend
✔ Clean and readable code

---

# 📈 Future Improvements

* Add SHAP explainability
* Add charts to frontend
* Add prediction history UI
* Secure admin login (JWT)
* Deploy backend + frontend
* Convert UI to React
* Improve class imbalance handling

---

# 🏁 Conclusion

This project demonstrates:

* **Data Analysis & ML expertise** (EDA → Model → Evaluation)
* **Backend knowledge** (Flask REST API)
* **Data engineerin** (MySQL storage + pipelines)
* **Frontend development** (HTML/JS)
* **Full-stack ML deployment**

Useful for **Data Analyst, ML Engineer, Data Scientist, BFSI Analytics**, and **Full-Stack** roles.

---
