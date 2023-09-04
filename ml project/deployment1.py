### Don't Forget to save python file before RUN

import streamlit as st
import requests
from streamlit_lottie import st_lottie
import joblib
import numpy as np
import pandas as pd


st.set_page_config(page_title='Water Quality', page_icon=':ocean:')


##### CHANGE THE icon

# def load_lottie(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()


## VALIDATION LL URL


loaded_model = joblib.load(open("water_potability_model1", 'rb'))
## EL SAVED FILE MN EL JOBLIB (WANA B3ML SAVE LL MODEL), w b3melo read "rb"


st.write('# Water Quality Prediction')

lottie_link = "https://assets8.lottiefiles.com/packages/lf20_ax5yuc0o.json"
lottie_link1= "https://lottie.host/2e114f28-866b-4cce-8aa7-72fc9e6c270c/l2LTaJQQyL.json"
####### GET LOTTIE ANIM FOR WATER
# animation = load_lottie(lottie_link)
# animation = load_lottie(lottie_link1)
st.write('---')
st.subheader('Please provide the following details about the water for quality prediction')
# Please provide the following details about the water to predict its quality:
# Enter more details for water quality prediction
# To predict the quality of water, please enter the required details below:

with st.container():
    rightCol, leftCol = st.columns(2)
    # SPLITTING CONTAINER TO 2 COLUMNS (Left: Text, Right: GUI)

with rightCol:
    pHval = st.slider('Pick a pH value', min_value=0.0, max_value=14.0, value=0.0, step=0.01)

    hardness = st.number_input('Hardness : ', min_value=0.0, max_value=325.0, value=0.0, step=0.001)

    solids = st.number_input('Solids : ', min_value=0.0, max_value=62000.0, value=0.0, step=0.01)

    chloramines = st.number_input('Chloramines : ', min_value=0.0, max_value=14.0, value=0.0, step=0.001)
    
    sulfates = st.number_input('Sulfate : ', min_value=0.0, max_value=485.0, value=0.0, step=0.01)


    ###### CHECK DECIMAL PTS.

with leftCol:
     
    Organic_carbon = st.number_input('Organic_carbon : ', min_value=0.0, max_value=30.0, value=0.0, step=0.01)
    
    Trihalomethanes = st.number_input('Trihalomethanes : ', min_value=0.0, max_value=130.0, value=0.0, step=0.01)
    
    a=[pHval, hardness, solids, chloramines, sulfates, Organic_carbon, Trihalomethanes]
    sample = np.array(a).reshape(-1,len(a))

    # st_lottie(animation, speed=1, height=400, key="initial")
    ## On the left side of the column, place the chosen lottie

if st.button('Predict'):
    
    pred_Y = loaded_model.predict(sample)

    if pred_Y == 1:
        # st.write("## Predicted Potability : ", result)
        st.write('### The water with pH', pHval, 'is potable.')
        st.balloons()
    else :
        st.write('### Unfortunately, water with pH ', pHval, 'is not potable.')
        st.warning('Not suitable for drinking!')

