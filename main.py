import streamlit as st
import joblib
import pandas as pd
import sklearn

# Load the trained Logistic Regression model
model = joblib.load('loan_approval_lr_model.joblib')

# Streamlit App
st.title('AIU Bank Loan Approval Prediction')
st.write("")
# User input form
st.sidebar.header('Customer Form')
st.write("")


# Function to collect user input features
def user_input_features():
    gender = st.sidebar.radio('Gender', ['Male', 'Female'])
    married = st.sidebar.radio('Marital Status', ['Yes', 'No'])
    dependents = st.sidebar.selectbox('Dependents', ['0', '1', '2', '3', '4'])
    education = st.sidebar.radio('Education', ['Graduate', 'Not Graduate'])
    self_employed = st.sidebar.radio('Self Employed', ['Yes', 'No'])
    applicant_income = st.sidebar.number_input('Applicant Income', 0, 10000)
    coapplicant_income = st.sidebar.number_input('Coapplicant Income', 0, 10000)
    loan_amount = st.sidebar.number_input('Loan Amount', 0, 10000)
    loan_amount_term = st.sidebar.number_input('Loan Amount Term (Months)', 12, 48)
    credit_history = st.sidebar.radio('Credit History', ['Good', 'Bad'])
    property_area = st.sidebar.radio('Property Area', ['Urban', 'Semiurban', 'Rural'])

    # Map categorical values to numerical values
    gender_mapping = {'Male': 0, 'Female': 1}
    married_mapping = {'No': 0, 'Yes': 1}
    education_mapping = {'Not Graduate': 0, 'Graduate': 1}
    self_employed_mapping = {'No': 0, 'Yes': 1}
    credit_history_mapping = {'Bad': 0, 'Good': 1}
    property_area_mapping = {'Rural': 0, 'Semiurban': 1, 'Urban': 2}

    # Create a dictionary with user input
    data = {
        'Gender': [gender_mapping[gender]],
        'Married': [married_mapping[married]],
        'Dependents': [int(dependents)],
        'Education': [education_mapping[education]],
        'Self_Employed': [self_employed_mapping[self_employed]],
        'ApplicantIncome': [applicant_income],
        'CoapplicantIncome': [coapplicant_income],
        'LoanAmount': [loan_amount],
        'Loan_Amount_Term': [loan_amount_term],
        'Credit_History': [credit_history_mapping[credit_history]],
        'Property_Area': [property_area_mapping[property_area]]
    }

    user_input_df = pd.DataFrame(data)
    return user_input_df


# Get user input
user_input_df = user_input_features()

# Display user input form
st.subheader('User Input Data:')
st.write(user_input_df)

# Predict loan approval on submit
if st.sidebar.button('Submit'):
    prediction = model.predict(user_input_df)
    st.write("")
    st.write("")
    st.write("")
    st.subheader('Prediction Status:')
    prediction_text = 'You are eligible for the loan' if prediction[0] == 1 else 'Sorry , you are not eligible for the loan'
    #prediction_text = 'Not Approved' if prediction[0] == 1 else 'Approved'


    st.write(f'Your Application: {prediction_text}')


