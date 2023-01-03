# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd 
import streamlit as st 
import xgboost as xgb 
from pickle import dump
from pickle import load

st.title('Model Deployment: Customer Churn Predictor')
st.sidebar.header('User Input Parameters')
html_temp = """
<div style="background-color:tomato;padding:10px">
<h2 style="color:white;text-align:center;">Streamlit Bank Authenticator ML App </h2>
</div>
"""

def prediction(account_length, intl_mins, intl_calls, day_mins, day_calls, eve_mins, eve_calls, night_mins, night_calls, customer_calls, states_label, voice_plan_label, intl_plan_label):    
    if intl_plan_label == "No":
     intl_plan_label = 0
    else:
     intl_plan_label = 1

    if voice_plan_label == "No":
     voice_plan_label = 0
    else:
     voice_plan_label = 1

    if states_label >= 51:
     states_label= "Invalid"
 
def user_input_features():
    account_length = st.sidebar.number_input("Insert the Account length")
    intl_mins= st.sidebar.number_input("Insert the Intl Mins.")
    intl_calls= st.sidebar.number_input("Insert the Intl calls.")
    day_mins= st.sidebar.number_input("Insert the Day Mins.")
    day_calls= st.sidebar.number_input("Insert the Day calls.")
    eve_mins= st.sidebar.number_input("Insert the Eve Mins.")
    eve_calls= st.sidebar.number_input("Insert the Eve calls.")
    night_mins= st.sidebar.number_input("Insert the Night Mins.")
    night_calls= st.sidebar.number_input("Insert the Night calls.")
    customer_calls= st.sidebar.number_input("Insert the  Cust calls.")
    states_label= st.sidebar.number_input("Insert the  States ID.")
    voice_plan_label= st.sidebar.selectbox('Voice plan',(0, 1))
    intl_plan_label= st.sidebar.selectbox('International plan',(0, 1))
   
    data= {'account.length':account_length,
            'intl.mins':intl_mins,
            'intl.calls':intl_calls,
            'day.mins':day_mins,
            'day.calls':day_calls,
            'eve.mins':eve_mins,
            'eve.calls':eve_calls,
            'night.mins':night_mins,
            'night.calls':night_calls,
            'customer.calls':customer_calls,
            'states_label':states_label,
            'voice.plan_label':voice_plan_label,
            'intl.plan_label':intl_plan_label
          }
    
     
    features = pd.DataFrame(data,index = [0])
    return features 
 
df = user_input_features()
st.subheader('User Input parameters')
st.write(df)


# load the model from disk
loaded_model = load(open('final_model.pkl', 'rb'))

prediction = loaded_model.predict(df)

st.subheader('Predicted Result')
if prediction == 0 :
   string = "No"
else:
   string ="Yes"

st.subheader('Prediction Probability')
st.write(prediction)

    
    
   



