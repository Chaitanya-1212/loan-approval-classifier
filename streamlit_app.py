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

    applicant = pd.DataFrame(
        [[
            gender,
            married,
            dependents,
            education,
            self_employed,
            applicant_income,
            coapplicant_income,
            loan_amount,
            loan_term,
            credit_history,
            property_area
        ]],
        columns=[
            "Gender",
            "Married",
            "Dependents",
            "Education",
            "Self_Employed",
            "ApplicantIncome",
            "CoapplicantIncome",
            "LoanAmount",
            "Loan_Amount_Term",
            "Credit_History",
            "Property_Area"
        ]
    )

    try:
        prediction = model.predict(applicant)

        if prediction[0] == "Y":
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

    except Exception as e:
        st.error(str(e))

        # Debug Info
        st.write("Input Columns:")
        st.write(applicant.columns.tolist())

        if hasattr(model.named_steps["imputer"], "feature_names_in_"):
            st.write("Model Expected Columns:")
            st.write(
                model.named_steps["imputer"].feature_names_in_.tolist()
            )
