import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Cybersecurity Dashboard",
    page_icon="🔒",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Apply custom CSS for dark theme
# st.markdown("""
#     <style>
#     body {
#         background-color: #0e0e2c;
#         color: #ffffff;
#     }
#     .stApp {
#         background: linear-gradient(to bottom, #0e0e2c, #1a1a40);
#     }
#     .stSidebar {
#         background-color: #0e0e2c;
#     }
#     .css-1d391kg {  /* Filter options sidebar */
#         color: #cfcfcf;
#     }
#     .css-1f6ov9r {  /* Select box */
#         color: #000000;
#     }
#     .css-2trqyj a {  /* Title */
#         color: #ffffff;
#     }
#     .css-1f6ov9r p {  /* Paragraph */
#         color: #ffffff;
#     }
#     .stButton>button {
#         background-color: #292961;
#         color: #ffffff;
#     }
#     </style>
#     """, unsafe_allow_html=True)

# Sample data creation for cybersecurity
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq='D')
data = {
    'date': dates,
    'anomalies_detected': np.random.poisson(5, size=len(dates)),
    'suspicious_activities_blocked': np.random.poisson(3, size=len(dates)),
    'cyberattacks_prevented': np.random.poisson(2, size=len(dates)),
}
df = pd.DataFrame(data)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Streamlit app
st.title("🔒 Cybersecurity Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
start_date = st.sidebar.date_input("Start Date", datetime(2024, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime(2024, 12, 31))

# Filter data based on user input
filtered_data = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

# Display filtered data in a beautiful table
st.subheader("Filtered Data")
st.dataframe(filtered_data.style.format(precision=2).background_gradient(cmap="viridis"))

# Anomalies Detected Over Time
st.subheader("Anomalies Detected Over Time")
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_data['date'], y=filtered_data['anomalies_detected'], marker='o', color='r')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Anomalies Detected", fontsize=14)
plt.title("Anomalies Detected Over Time", fontsize=18)
st.pyplot(plt)

# Suspicious Activities Blocked Over Time
st.subheader("Suspicious Activities Blocked Over Time")
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_data['date'], y=filtered_data['suspicious_activities_blocked'], marker='o', color='g')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Suspicious Activities Blocked", fontsize=14)
plt.title("Suspicious Activities Blocked Over Time", fontsize=18)
st.pyplot(plt)

# Cyberattacks Prevented Over Time
st.subheader("Cyberattacks Prevented Over Time")
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_data['date'], y=filtered_data['cyberattacks_prevented'], marker='o', color='b')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Cyberattacks Prevented", fontsize=14)
plt.title("Cyberattacks Prevented Over Time", fontsize=18)
st.pyplot(plt)

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>Cybersecurity Dashboard | Powered by AI & ML</p>
    <p>&#169; 2024 Your Company. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
