import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="CreditRisk AI",
    page_icon="🏦",
    layout="wide"
)

st.markdown("""
<style>
.main {
    padding-top: 1rem;
}

.stButton > button {
    width: 100%;
    height: 3em;
    border-radius: 10px;
    font-size: 18px;
}
</style>
""", unsafe_allow_html=True)

# Load Model
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

MODEL_PATH = os.path.join(
    BASE_DIR,
    "..",
    "models",
    "loan_default_model.pkl"
)

model = joblib.load(MODEL_PATH)

st.title("🏦 CreditRisk AI")

st.markdown("""
### Smart Loan Approval Prediction System

Predict loan approval chances using Machine Learning.
""")

c1, c2, c3 = st.columns(3)

c1.metric("Dataset Size", "614")
c2.metric("Best Accuracy", "78.86%")
c3.metric("Model", "Random Forest")

st.sidebar.title("About")

st.sidebar.info("""
CreditRisk AI predicts loan approval
using Machine Learning.

Model: Random Forest

Developed by Siddhi Tapase
""")
# User Inputs

col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "Gender",
        ["Male","Female"]
    )

    married = st.selectbox(
        "Married",
        ["Yes","No"]
    )

    dependents = st.selectbox(
        "Dependents",
        ["0","1","2","3+"]
    )

    education = st.selectbox(
        "Education",
        ["Graduate","Not Graduate"]
    )

with col2:

    self_employed = st.selectbox(
        "Self Employed",
        ["Yes","No"]
    )

    property_area = st.selectbox(
        "Property Area",
        ["Urban","Semiurban","Rural"]
    )

    credit_history = st.selectbox(
        "Credit History",
        [1,0]
    )

st.subheader("💰 Financial Information")

col3, col4 = st.columns(2)

with col3:

    applicant_income = st.number_input(
        "Applicant Income",
        min_value=0
    )

    coapplicant_income = st.number_input(
        "Coapplicant Income",
        min_value=0
    )

with col4:

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0
    )

    loan_term = st.number_input(
        "Loan Amount Term",
        value=360
    )

# Predict Button

if st.button("Predict"):

    total_income = (
        applicant_income +
        coapplicant_income
    )

    loan_income_ratio = (
        loan_amount /
        (total_income + 1)
    )

    log_income = np.log1p(
        total_income
    )

    input_data = pd.DataFrame([{
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "TotalIncome": total_income,
        "LoanIncomeRatio": loan_income_ratio,
        "LogIncome": log_income,

        "Gender_Male":
            1 if gender == "Male" else 0,

        "Married_Yes":
            1 if married == "Yes" else 0,

        "Dependents_1":
            1 if dependents == "1" else 0,

        "Dependents_2":
            1 if dependents == "2" else 0,

        "Dependents_3+":
            1 if dependents == "3+" else 0,

        "Education_Not Graduate":
            1 if education == "Not Graduate" else 0,

        "Self_Employed_Yes":
            1 if self_employed == "Yes" else 0,

        "Property_Area_Semiurban":
            1 if property_area == "Semiurban" else 0,

        "Property_Area_Urban":
            1 if property_area == "Urban" else 0
    }])

    prediction = model.predict(input_data)
    probability = model.predict_proba(input_data)[0][1]

    st.metric(
    "Approval Probability",
    f"{probability:.2%}"
)
    probability = model.predict_proba(input_data)[0][1]
    st.write(
    f"Approval Probability: {probability:.2%}"
    )

    if prediction[0] == 1:
        st.balloons()

        st.success(
            "✅ Loan Likely Approved"
        )

    else:

        st.error(
            "❌ Loan Likely Rejected"
        )