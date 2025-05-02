# streamlit_traffic_prediction.py

import streamlit as st
import pyttsx3
import trafficprediction as tp  # Make sure this module exists and is in the same directory

# Set up the Streamlit page
st.set_page_config(page_title="Traffic Prediction App", layout="centered")
st.title("🚦 Traffic Prediction App")

# Input fields
date = st.text_input("Date (e.g., 2025-05-01)")
time = st.text_input("Time (e.g., 14:30)")
dotw = st.text_input("Day of the Week (e.g., Monday)")
carcount = st.number_input("Car Count", min_value=0, step=1)
bikecount = st.number_input("Bike Count", min_value=0, step=1)
buscount = st.number_input("Bus Count", min_value=0, step=1)
truckcount = st.number_input("Truck Count", min_value=0, step=1)

# Button to trigger prediction
if st.button("Predict"):
    # Input validation (basic)
    if not date or not time or not dotw:
        st.warning("Please fill in all the required fields.")
    else:
        try:
            total = carcount + bikecount + buscount + truckcount
            prediction = tp.function(time, date, dotw, carcount, bikecount, buscount, truckcount, total)

            st.success(f"🚗 Predicted Traffic Situation: {prediction}")

            # Speak the result
            engine = pyttsx3.init()
            engine.say(f"Predicted traffic situation: {prediction}")
            engine.runAndWait()
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")

