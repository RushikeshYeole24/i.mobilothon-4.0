import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Load Dataset (simulated)
def load_data():
    data = {
        "Vehicle_ID": ["V123", "V124", "V125", "V126", "V127"],
        "Mileage": [25000, 40000, 5000, 18000, 30000],
        "Engine_Hours": [1200, 1600, 400, 1000, 1400],
        "Component": ["Brakes", "Engine", "Transmission", "Suspension", "Brakes"],
        "Last_Maintenance": pd.to_datetime(["2023-01-20", "2023-02-15", "2023-03-01", "2023-01-10", "2023-04-05"]),
        "Component_Health_Score": [78, 60, 85, 74, 67],
        "Temperature": [85, 90, 65, 80, 88],
        "Vibration_Level": [0.05, 0.15, 0.02, 0.10, 0.08],
        "Predicted_Failure": [1, 0, 0, 1, 1]
    }
    df = pd.DataFrame(data)
    return df

data = load_data()

# Layout
st.title("Vehicle Maintenance Prediction App")
st.write("Predict component failures based on vehicle data.")

# Display data
st.subheader("Vehicle Data")
st.dataframe(data)

# Data Visualization
st.subheader("Data Visualizations")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# Mileage vs. Health Score
sns.scatterplot(x='Mileage', y='Component_Health_Score', data=data, ax=axes[0], hue='Predicted_Failure')
axes[0].set_title("Mileage vs Component Health Score")

# Temperature vs Vibration Level
sns.scatterplot(x='Temperature', y='Vibration_Level', data=data, ax=axes[1], hue='Predicted_Failure')
axes[1].set_title("Temperature vs Vibration Level")

st.pyplot(fig)

# Train a simple model for prediction
st.subheader("Predict Component Failure")

# Features and Labels
X = data[['Mileage', 'Engine_Hours', 'Component_Health_Score', 'Temperature', 'Vibration_Level']]
y = data['Predicted_Failure']

# Train/Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# Prediction Metrics
st.write("Classification Report:")
st.text(classification_report(y_test, y_pred))

# User Input for Prediction
st.subheader("Custom Prediction")

mileage = st.number_input("Enter Mileage:", value=20000)
engine_hours = st.number_input("Enter Engine Hours:", value=1000)
component_health_score = st.slider("Component Health Score:", min_value=0, max_value=100, value=80)
temperature = st.number_input("Temperature (°C):", value=80)
vibration_level = st.number_input("Vibration Level:", value=0.05)

if st.button("Predict Failure"):
    user_data = np.array([[mileage, engine_hours, component_health_score, temperature, vibration_level]])
    prediction = model.predict(user_data)
    if prediction == 1:
        st.error("Warning: Component Likely to Fail")
    else:
        st.success("Component Unlikely to Fail")

# Styling
st.markdown("""
<style>
    .stButton>button {
        color: white;
        background-color: #4CAF50;
    }
    .stDataFrame, .stTextInput, .stNumberInput, .stSlider {
        font-size: large;
    }
</style>
""", unsafe_allow_html=True)
