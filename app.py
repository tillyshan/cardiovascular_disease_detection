import streamlit as st
from PIL import Image
import pandas as pd
import pickle
import time

st.header('Cardiovascular Disease Detection APP')
image = Image.open('heart-disease-deaths-800x500.png')
resized_image = image.resize((2000, 500))
st.image(resized_image)

st.subheader('Enter Your Information:')
st.markdown('Please fill in the following details:')

col1, col2 = st.columns(2)

with col1:
    age = st.text_input(label='Age (years)')
    height = st.text_input(label='Height (cm)')
    weight = st.text_input(label='Weight (Kg)')
    ap_hi = st.slider(label='Systolic BP (mmHg)', min_value=50, max_value=220, value=80)
    ap_lo = st.slider(label='Diastolic BP (mmHg)', min_value=30, max_value=110, value=80)

with col2:
    gender = st.selectbox('Gender', ['male', 'female'])
    cholesterol = st.selectbox('Cholesterol Level', ['normal', 'above normal', 'well above normal'])
    gluc = st.selectbox('Glucose Level', ['normal', 'above normal', 'well above normal'])
    smoke = st.selectbox('Do you Smoke?', ['Yes', 'No'])
    alco = st.selectbox('Do You Take Alcohol?', ['Yes', 'No'])
    active = st.selectbox('Physical Activity?', ['Yes', 'No'])

Enter_data_button = st.button("Submit")

progress_bar = st.progress(0)

if Enter_data_button:
    if any([value == '' for value in [age, height, weight, ap_hi, ap_lo]]):
        st.error("Please fill in all the required fields.")
    else:
        try:
            age = float(age)
            height = float(height)
            weight = float(weight)
            ap_lo = float(ap_lo)
            ap_hi = float(ap_hi)
        except ValueError:
            st.error("Invalid input. Please enter valid numbers for the required fields.")
        else:
            for percent_complete in range(0, 101, 10):
                progress_bar.progress(percent_complete)
                time.sleep(0.1)

            user_input = {
                'age': [age],
                'gender': [gender],
                'height': [height],
                'weight': [weight],
                'ap_hi': [ap_hi],
                'ap_lo': [ap_lo],
                'cholesterol': [cholesterol],
                'gluc': [gluc],
                'smoke': [smoke],
                'alco': [alco],
                'active': [active]
            }

            user_input_df = pd.DataFrame(user_input)

            with open('model.pickle', 'rb') as file:
                model = pickle.load(file)

            with open('preprocessor.pickle', 'rb') as file:
                preprocessor = pickle.load(file)

            preprocessed_df = preprocessor.transform(user_input_df)
            prediction = model.predict(preprocessed_df)

            if prediction == 0:
                output = '<span style="color:purple; font-weight:bold; font-size:20px;">According to Our Model You do not have Cardiovascular Disease....</span>'
            else:
                output = '<span style="color:purple; font-weight:bold; font-size:20px;">According to Our Model You do not have Cardiovascular Disease....</span>'

            st.subheader('Your entered data:')
            st.write(user_input_df)

            st.subheader('Your Result:')
            st.markdown(f'<div style="border:1px solid #33cc33; padding:10px">{output}</div>', unsafe_allow_html=True)
