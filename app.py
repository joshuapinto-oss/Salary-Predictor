import streamlit as st
import pandas as pd
import joblib

# Load the trained pipeline
model = joblib.load('model.pkl')

st.title("Data Science Salary Predictor")
st.write("Enter the details below to predict salary in USD")

# Dropdown inputs
experience_level = st.selectbox(
    "Experience Level",
    ['Entry-level', 'Mid-level', 'Senior-level', 'Executive-level']
)

employment_type = st.selectbox(
    "Employment Type",
    ['Full-time', 'Part-time', 'Contract', 'Freelance']
)

job_title = st.selectbox(
    "Job Title",
    ['Data Scientist', 'Data Engineer', 'ML Engineer',
     'Data Analyst', 'Research Scientist', 'Machine Learning Engineer']
)

company_size = st.selectbox(
    "Company Size",
    ['Small', 'Medium', 'Large']
)

remote_ratio = st.selectbox(
    "Remote Work Ratio (%)",
    [0, 50, 100]
)

# Predict button
if st.button("Predict Salary"):
    input_df = pd.DataFrame({
        'experience_level': [experience_level],
        'employment_type': [employment_type],
        'job_title': [job_title],
        'company_size': [company_size],
        'remote_ratio': [remote_ratio]
    })

    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Salary: ${prediction:,.0f} per year")