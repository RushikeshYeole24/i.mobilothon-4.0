import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Set page configuration
st.set_page_config(
    page_title="Regulatory Compliance Dashboard",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded",
)



# Sample data creation for regulatory compliance
np.random.seed(42)
dates = pd.date_range(start="2024-01-01", end="2024-12-31", freq='D')
data = {
    'date': dates,
    'new_regulations': np.random.randint(0, 10, size=len(dates)),
    'compliance_updates': np.random.randint(0, 10, size=len(dates)),
    'non_compliance_cases': np.random.poisson(2, size=len(dates)),
}
df = pd.DataFrame(data)

# Convert date column to datetime
df['date'] = pd.to_datetime(df['date'])

# Streamlit app
st.title("⚖️ Regulatory Compliance Dashboard")

# Sidebar filters
st.sidebar.header("Filter Options")
start_date = st.sidebar.date_input("Start Date", datetime(2024, 1, 1))
end_date = st.sidebar.date_input("End Date", datetime(2024, 12, 31))

# Filter data based on user input
filtered_data = df[(df['date'] >= pd.to_datetime(start_date)) & (df['date'] <= pd.to_datetime(end_date))]

# Display filtered data in a beautiful table
st.subheader("Filtered Data")
st.dataframe(filtered_data.style.format(precision=2).background_gradient(cmap="viridis"))

# New Regulations Over Time
st.subheader("New Regulations Over Time")
sns.set_theme(style="darkgrid")
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_data['date'], y=filtered_data['new_regulations'], marker='o', color='b')
plt.xlabel("Date", fontsize=14)
plt.ylabel("New Regulations", fontsize=14)
plt.title("New Regulations Over Time", fontsize=18)
st.pyplot(plt)

# Compliance Updates Over Time
st.subheader("Compliance Updates Over Time")
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_data['date'], y=filtered_data['compliance_updates'], marker='o', color='g')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Compliance Updates", fontsize=14)
plt.title("Compliance Updates Over Time", fontsize=18)
st.pyplot(plt)

# Non-Compliance Cases Over Time
st.subheader("Non-Compliance Cases Over Time")
plt.figure(figsize=(12, 6))
sns.lineplot(x=filtered_data['date'], y=filtered_data['non_compliance_cases'], marker='o', color='r')
plt.xlabel("Date", fontsize=14)
plt.ylabel("Non-Compliance Cases", fontsize=14)
plt.title("Non-Compliance Cases Over Time", fontsize=18)
st.pyplot(plt)

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>Regulatory Compliance Dashboard | Powered by AI & ML</p>
    <p>&#169; 2024 Your Company. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
