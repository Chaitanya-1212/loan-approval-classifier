import streamlit as st
import pandas as pd
import pickle

# Load Model
with open("loan_prediction_model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦"
)

st.title("🏦 Loan Approval Prediction System")

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

married = st.selectbox(
    "Married",
    ["Yes", "No"]
)

dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

self_employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

applicant_income = st.number_input(
    "Applicant Income",
    min_value=0.0,
    value=5000.0
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0.0,
    value=0.0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=120.0
)

loan_term = st.number_input(
    "Loan Amount Term",
    min_value=0.0,
    value=360.0
)

credit_history = st.selectbox(
    "Credit History",
    [1.0, 0.0]
)

property_area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)

if st.button("Predict"):

    applicant = pd.DataFrame({
        "ApplicantIncome":[applicant_income],
        "CoapplicantIncome":[coapplicant_income],
        "LoanAmount":[loan_amount],
        "Loan_Amount_Term":[loan_term],
        "Credit_History":[credit_history],

        "Gender_Male":[1 if gender=="Male" else 0],

        "Married_Yes":[1 if married=="Yes" else 0],

        "Dependents_1":[1 if dependents=="1" else 0],
        "Dependents_2":[1 if dependents=="2" else 0],
        "Dependents_3+":[1 if dependents=="3+" else 0],

        "Education_Not Graduate":[1 if education=="Not Graduate" else 0],

        "Self_Employed_Yes":[1 if self_employed=="Yes" else 0],

        "Property_Area_Semiurban":[1 if property_area=="Semiurban" else 0],
        "Property_Area_Urban":[1 if property_area=="Urban" else 0]
    })

    prediction = model.predict(applicant)

    if prediction[0] == "Y":
        st.success("✅ Loan Approved")
    else:
        st.error("❌ Loan Rejected")
