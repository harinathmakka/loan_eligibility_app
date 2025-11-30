import pandas as pd
import numpy as np

# Feature order EXACTLY as model was trained
FEATURES = [
    'InterestRate','CreditScore','DTIRatio','EmploymentType_Unemployed',
    'Education_High School',"Education_Master's",'Education_PhD',
    'HasMortgage_Yes','HasDependents_Yes','HasCoSigner_Yes',
    'Age','Income','LoanAmount','MonthsEmployed','NumCreditLines','LoanTerm'
]

def preprocess_input(data):
    # Initialize zero array
    row = {f: 0 for f in FEATURES}

    # Fill numerical values
    row['InterestRate'] = float(data['interest_rate'])
    row['CreditScore'] = int(data['credit_score'])
    row['DTIRatio'] = float(data['dti_ratio'])
    row['Age'] = int(data['age'])
    row['Income'] = float(data['income'])
    row['LoanAmount'] = float(data['loan_amount'])
    row['MonthsEmployed'] = int(data['months_employed'])
    row['NumCreditLines'] = int(data['num_credit_lines'])
    row['LoanTerm'] = int(data['loan_term'])

    # Categorical (one-hot)
    row['EmploymentType_Unemployed'] = 1 if data['employment_type'] == "Unemployed" else 0

    row['Education_High School'] = 1 if data['education'] == "High School" else 0
    row["Education_Master's"] = 1 if data['education'] == "Master's" else 0
    row['Education_PhD'] = 1 if data['education'] == "PhD" else 0

    row['HasMortgage_Yes'] = 1 if data['has_mortgage'] == "Yes" else 0
    row['HasDependents_Yes'] = 1 if data['has_dependents'] == "Yes" else 0
    row['HasCoSigner_Yes'] = 1 if data['has_cosigner'] == "Yes" else 0

    return pd.DataFrame([row])
