import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Telco Churn Prediction", layout="centered")
st.title("Customer Churn Prediction")
st.write("This app predicts whether a Telco customer is likely to churn based on customer and service information.")

model = joblib.load("best_churn_model.pkl")

with st.form("prediction_form"):
    gender = st.selectbox("Gender", ["Female", "Male"])
    SeniorCitizen = st.selectbox("Senior Citizen", ["No", "Yes"])
    Partner = st.selectbox("Partner", ["Yes", "No"])
    Dependents = st.selectbox("Dependents", ["Yes", "No"])
    tenure = st.slider("Tenure (months)", 0, 72, 12)
    PhoneService = st.selectbox("Phone Service", ["Yes", "No"])
    MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes", "No phone service"])
    InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
    OnlineSecurity = st.selectbox("Online Security", ["No", "Yes", "No internet service"])
    OnlineBackup = st.selectbox("Online Backup", ["No", "Yes", "No internet service"])
    DeviceProtection = st.selectbox("Device Protection", ["No", "Yes", "No internet service"])
    TechSupport = st.selectbox("Tech Support", ["No", "Yes", "No internet service"])
    StreamingTV = st.selectbox("Streaming TV", ["No", "Yes", "No internet service"])
    StreamingMovies = st.selectbox("Streaming Movies", ["No", "Yes", "No internet service"])
    Contract = st.selectbox("Contract", ["Month-to-month", "One year", "Two year"])
    PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])
    PaymentMethod = st.selectbox("Payment Method", ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"])
    MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.0)
    TotalCharges = st.number_input("Total Charges", min_value=0.0, value=850.0)
    submitted = st.form_submit_button("Predict")

if submitted:
    AvgChargesPerTenure = TotalCharges / (tenure + 1)
    if tenure <= 12:
        TenureGroup = "0-12 months"
    elif tenure <= 24:
        TenureGroup = "13-24 months"
    elif tenure <= 48:
        TenureGroup = "25-48 months"
    else:
        TenureGroup = "49-72 months"

    input_df = pd.DataFrame([{ 
        "gender": gender, "SeniorCitizen": SeniorCitizen, "Partner": Partner, "Dependents": Dependents,
        "tenure": tenure, "PhoneService": PhoneService, "MultipleLines": MultipleLines,
        "InternetService": InternetService, "OnlineSecurity": OnlineSecurity, "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection, "TechSupport": TechSupport, "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies, "Contract": Contract, "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod, "MonthlyCharges": MonthlyCharges, "TotalCharges": TotalCharges,
        "AvgChargesPerTenure": AvgChargesPerTenure, "TenureGroup": TenureGroup
    }])
    probability = model.predict_proba(input_df)[0][1]
    prediction = model.predict(input_df)[0]
    st.metric("Churn Probability", f"{probability:.2%}")
    if prediction == 1:
        st.error("High churn risk: This customer is likely to churn.")
    else:
        st.success("Low churn risk: This customer is not likely to churn.")
