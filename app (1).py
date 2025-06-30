import streamlit as st
import joblib
import pandas as pd

# Load the trained model
model = joblib.load('burnout_prediction_model.pkl')

st.title('Burnout Rate Prediction')

st.header('Enter Employee Details:')

designation = st.number_input('Designation (0-5)', min_value=0.0, max_value=5.0, value=2.0, step=0.5)
resource_allocation = st.number_input('Resource Allocation (1-10)', min_value=1.0, max_value=10.0, value=5.0, step=0.1)
mental_fatigue_score = st.number_input('Mental Fatigue Score (0-10)', min_value=0.0, max_value=10.0, value=5.0, step=0.1)
join_year = st.number_input('Joining Year', min_value=2000, max_value=2025, value=2008, step=1)
join_month = st.number_input('Joining Month', min_value=1, max_value=12, value=7, step=1)
join_day = st.number_input('Joining Day', min_value=1, max_value=31, value=15, step=1)
gender_male = st.checkbox('Gender: Male')
company_type_service = st.checkbox('Company Type: Service')
wfh_setup_available_yes = st.checkbox('WFH Setup Available: Yes')

resource_fatigue_interaction = resource_allocation * mental_fatigue_score

if st.button('Predict Burnout Rate'):
    input_data = pd.DataFrame([[designation, resource_allocation, mental_fatigue_score, join_year, join_month, join_day, gender_male, company_type_service, wfh_setup_available_yes, resource_fatigue_interaction]],
                              columns=['Designation', 'Resource Allocation', 'Mental Fatigue Score', 'join_year', 'join_month', 'join_day', 'Gender_Male', 'Company Type_Service', 'WFH Setup Available_Yes', 'resource_fatigue_interaction'])

    predicted_burnout_rate = model.predict(input_data)[0]
    st.subheader(f'Predicted Burnout Rate: {predicted_burnout_rate:.2f}')
