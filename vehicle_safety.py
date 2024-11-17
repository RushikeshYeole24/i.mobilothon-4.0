import streamlit as st
import pandas as pd
import numpy as np
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from datetime import datetime

st.set_page_config(page_title="Vehicle Safety Assistant", layout="centered")

st.title("Vehicle Safety Assistant")
st.subheader("Real-Time Analysis for Autonomous Driving Safety")

# Placeholder for real-time data display
placeholder = st.empty()

# Data simulation function
def generate_real_time_data():
    while True:
        yield {
            "speed": np.random.uniform(0, 120),  # Speed in km/h
            "latitude": np.random.uniform(-90, 90),
            "longitude": np.random.uniform(-180, 180),
            "obstacle_proximity": np.random.uniform(0, 100),  # Distance in meters
            "light_level": np.random.choice(['day', 'night']),
            "road_condition": np.random.choice(['wet', 'dry']),
            "driver_fatigue": np.random.choice([0, 1]),  # 0 - Not fatigued, 1 - Fatigued
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        time.sleep(1)

# Real-time data generator
data_stream = generate_real_time_data()

# Training a basic model with label encoding initialized to prevent unseen label errors
def train_model():
    df = pd.DataFrame({
        "speed": np.random.uniform(0, 120, 100),
        "obstacle_proximity": np.random.uniform(0, 100, 100),
        "light_level": np.random.choice(['day', 'night'], 100),
        "road_condition": np.random.choice(['wet', 'dry'], 100),
        "driver_fatigue": np.random.choice([0, 1], 100),
        "safety_alert": np.random.choice([0, 1], 100)  # 0 - Safe, 1 - Alert
    })
    
    # Initialize label encoders with all possible values
    le_light = LabelEncoder()
    le_light.fit(['day', 'night'])  # Fit with possible values
    
    le_road = LabelEncoder()
    le_road.fit(['wet', 'dry'])  # Fit with possible values
    
    # Apply encoding to training data
    df['light_level'] = le_light.transform(df['light_level'])
    df['road_condition'] = le_road.transform(df['road_condition'])
    
    X = df[['speed', 'obstacle_proximity', 'light_level', 'road_condition', 'driver_fatigue']]
    y = df['safety_alert']
    
    model = RandomForestClassifier()
    model.fit(X, y)
    return model, le_light, le_road

model, le_light, le_road = train_model()

# Stream real-time data and make predictions
for data in data_stream:
    # Encode categorical data for model input
    data_encoded = data.copy()
    data_encoded['light_level'] = le_light.transform([data_encoded['light_level']])[0]
    data_encoded['road_condition'] = le_road.transform([data_encoded['road_condition']])[0]

    # Display real-time data without encoding (for user readability)
    data_df = pd.DataFrame([data])
    placeholder.dataframe(data_df)

    # Prepare data for prediction (encoded data)
    X_real_time = pd.DataFrame([data_encoded])[['speed', 'obstacle_proximity', 'light_level', 'road_condition', 'driver_fatigue']]
    
    # Prediction using model
    prediction = model.predict(X_real_time)
    
    # Display safety alert
    if prediction[0] == 1:
        st.error("⚠️ Safety Alert: Action Recommended!")
    else:
        st.success("✔️ Safe Driving Conditions")
        
    # Delay to simulate real-time streaming
    time.sleep(1)
