import streamlit as st
import pandas as pd
import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier

model = joblib.load('obesity_model.pkl')
st.title('Obesity level prediction')
st.subheader('A Machine Learning model to predict the level of Obesity by checking important features of the targeted person.')

value_map = {1 : 'Normal weight', 2 : 'Overweight Level I', 3: 'Overweight Level II', 4 : 'Obesity Level I', 0: 'Insuffecient weight', 5 : 'Obesity Level II', 6 : 'Obesity Level III'}

with st.sidebar:
    st.header('Data Requirements')
    st.caption('Data Requirements are a prerequesites to let the AI model work properly, without any errors in terms of data types and mispredictions')
    with st.expander("Data Format"):
        st.markdown('- utf-8')
        st.markdown('- seperated by comma')
        st.markdown('- delimited by \".\"')
        st.markdown('- first row -- heaer')
    
    st.divider()
    st.write('<p style = "text-align: center"> Devolped by Noor Elden</p>', unsafe_allow_html= True)

if 'clicked' not in st.session_state:
    st.session_state.clicked = {1:False}

def clicked(button):
    st.session_state.clicked[button] = True

st.button('Let\'s get started', on_click = clicked, args=[1])

if st.session_state.clicked[1]:
    height = st.text_input("what is your height?(in metric)")
    age = st.number_input("How old are you?", min_value=7, max_value=110)
    weight = st.text_input("How much do you weigh?")
    meals = st.text_input("How many meals do you usually eat per day?")

    if not height or not age or not weight or not meals:
        st.error("Please fill all the fields")
    if height and age and weight and meals:
        height = float(height)
        age = float(age)
        weight = float(weight)
        meals = float(meals)
        st.success('Valid input')
        if st.button('Predict'):
            input_data = np.array([height, age, weight, meals])
            prediction = model.predict(input_data.reshape(1, -1))
            result = value_map[prediction[0]]
            st.write('The predicted level of obesity is: ', result)