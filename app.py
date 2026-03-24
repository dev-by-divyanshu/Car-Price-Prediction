import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model + columns
model, columns = pickle.load(open("car_price_model.pkl", "rb"))

st.title("🚗 Car Price Prediction System")

st.sidebar.header("Enter Car Details")

# User inputs
year = st.sidebar.slider("Manufacturing Year", 2000, 2025, 2015)
km_driven = st.sidebar.number_input("Kilometers Driven", 0)
seats = st.sidebar.number_input("Seats", 2, 10, 5)
engine = st.sidebar.number_input("Engine (CC)", 500, 5000, 1200)
mileage = st.sidebar.number_input("Mileage", 5.0, 40.0, 18.0)
max_power = st.sidebar.number_input("Max Power (BHP)", 20.0, 300.0, 80.0)

fuel = st.sidebar.selectbox("Fuel Type", ["Petrol", "Diesel", "LPG"])
seller = st.sidebar.selectbox("Seller Type", ["Individual", "Trustmark Dealer"])
transmission = st.sidebar.selectbox("Transmission", ["Manual", "Automatic"])
owner = st.sidebar.selectbox("Owner Type", [
    "First Owner", "Second Owner", "Third Owner", "Fourth & Above Owner", "Test Drive Car"
])

brand = st.sidebar.selectbox("Car Brand", [
    "Ford", "Honda", "Hyundai", "Mahindra", "Maruti", "Renault", "Tata", "Toyota", "Volkswagen"
])

if st.sidebar.button("Predict Price"):

    # Create input dataframe
    input_df = pd.DataFrame(np.zeros((1, len(columns))), columns=columns)

    # Fill numeric values
    if 'year' in columns:
        input_df['year'] = year

    if 'km_driven' in columns:
        input_df['km_driven'] = km_driven

    if 'seats' in columns:
        input_df['seats'] = seats

    if 'Engine (CC)' in columns:
        input_df['Engine (CC)'] = engine

    if 'Mileage' in columns:
        input_df['Mileage'] = mileage

    if 'max_power (in bph)' in columns:
        input_df['max_power (in bph)'] = max_power

    # One-hot encoding
    input_df[f'fuel_{fuel}'] = 1
    input_df[f'seller_type_{seller}'] = 1

    if transmission == "Manual":
        input_df['transmission_Manual'] = 1

    if owner != "First Owner":
        input_df[f'owner_{owner}'] = 1

    input_df[f'name_{brand}'] = 1

    # Predict
    prediction = model.predict(input_df)

    st.success(f"💰 Estimated Price: ₹ {prediction[0]:.2f} lakhs")