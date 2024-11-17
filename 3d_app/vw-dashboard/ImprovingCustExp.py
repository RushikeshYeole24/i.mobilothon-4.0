import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Predictive Maintenance Dashboard",
    page_icon=":car:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Sample data creation
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", end="2023-12-31", freq='D')
data = {
    'date': dates,
    'vehicle_id': np.random.randint(1, 10, size=len(dates)),
    'component_temperature': np.random.normal(75, 10, size=len(dates)),
    'vibration_level': np.random.normal(1.5, 0.5, size=len(dates)),
    'operating_hours': np.random.randint(1, 24, size=len(dates)),
    'maintenance_required': np.random.choice([0, 1], size=len(dates), p=[0.95, 0.05])
}
df = pd.DataFrame(data)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Streamlit app
st.title("🚗 Predictive Maintenance Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
vehicle_id = st.sidebar.selectbox("Select Vehicle ID", df['vehicle_id'].unique())
start_date = st.sidebar.date_input("Start Date", datetime(2023, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime(2023, 12, 31))

# Filter data based on user input
filtered_data = df[(df['vehicle_id'] == vehicle_id) & (df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

# Display filtered data in a beautiful table
st.subheader(f"Data for Vehicle ID: {vehicle_id}")
st.dataframe(filtered_data.style.format(precision=2).background_gradient(cmap="coolwarm"))

# Maintenance Prediction
st.subheader("Maintenance Prediction")
maintenance_prob = filtered_data['maintenance_required'].mean()
st.metric(label="Probability of Maintenance Required", value=f"{maintenance_prob:.2%}")

# Component Temperature Over Time
st.subheader("Component Temperature Over Time")
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_data['date'], y=filtered_data['component_temperature'], marker='o', color='b')
plt.xlabel("Date")
plt.ylabel("Temperature (°F)")
plt.title("Component Temperature Over Time")
plt.grid(True)
st.pyplot(plt)

# Vibration Level Over Time
st.subheader("Vibration Level Over Time")
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_data['date'], y=filtered_data['vibration_level'], marker='o', color='r')
plt.xlabel("Date")
plt.ylabel("Vibration Level")
plt.title("Vibration Level Over Time")
plt.grid(True)
st.pyplot(plt)

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>Predictive Maintenance Dashboard | Powered by AI & ML</p>
    <p>&#169; 2023 Your Company. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
