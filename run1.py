import streamlit as st
import pandas as pd
import numpy as np
import pickle
import base64
 
# --- Helper Function ---
# Removed get_fvalue as it was redundant. This one function can handle all mappings.
@st.cache_data  # Updated from st.cache
def get_mapped_value(val, mapping_dict):
    """Fetches the numerical value from a dictionary based on the user's selection."""
    for key, value in mapping_dict.items():
        if val == key:
            return value
 
# --- App Navigation ---
app_mode = st.sidebar.selectbox('Select Page', ['Home', 'Prediction'])
 
# --- Home Page ---
if app_mode == 'Home':
    st.title('LOAN PREDICTION :')
    st.image('loan_image.jpg')  # Make sure this image is in the same folder
    st.write('@DSU for learning purposes only')
 
# --- Prediction Page ---
elif app_mode == 'Prediction':
    # You can remove these two lines if you don't need to display the CSV
    csv = pd.read_csv("informations.csv")
    st.write(csv)
 
    st.subheader('Sir/Mme , YOU need to fill all neccesary informations in order to get a reply to your loan request !')
    st.sidebar.header("Informations about the client :")
 
    # --- Input Mappings ---
    # Dictionaries to map user-friendly text to numerical values for the model
    gender_map = {"Male": 1, "Female": 2}
    binary_map = {"No": 1, "Yes": 2}  # For "Married" and "Self Employed"
