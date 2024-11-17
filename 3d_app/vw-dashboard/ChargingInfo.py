import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.cluster import KMeans

# Set page configuration
st.set_page_config(
    page_title="Charging Infrastructure Optimization",
    page_icon="🔋",
    layout="wide",
    initial_sidebar_state="expanded",
)



# Sample data creation for charging stations optimization
np.random.seed(42)
num_locations = 100
data = {
    'location_id': np.arange(num_locations),
    'latitude': np.random.uniform(20.0, 40.0, num_locations),
    'longitude': np.random.uniform(70.0, 90.0, num_locations),
    'current_load': np.random.uniform(0, 100, num_locations),
}

df = pd.DataFrame(data)

# Streamlit app
st.title("🔋 Charging Infrastructure Optimization")

# Sidebar for selecting number of clusters (charging stations)
st.sidebar.header("Optimization Parameters")
num_clusters = st.sidebar.slider("Number of Charging Stations", min_value=1, max_value=20, value=5)

# K-Means Clustering for Optimal Charging Station Locations
kmeans = KMeans(n_clusters=num_clusters)
df['cluster'] = kmeans.fit_predict(df[['latitude', 'longitude']])

# Display data
st.subheader("Charging Station Locations and Load Distribution")
st.map(df[['latitude', 'longitude']])

# Plot clusters
st.subheader("Optimal Charging Station Locations")
plt.figure(figsize=(12, 6))
sns.scatterplot(data=df, x='longitude', y='latitude', hue='cluster', palette='viridis', legend='full')
plt.xlabel("Longitude", fontsize=14)
plt.ylabel("Latitude", fontsize=14)
plt.title("Optimal Charging Station Locations", fontsize=18)
st.pyplot(plt)

# Energy Distribution Management
st.subheader("Energy Load Distribution Across Charging Stations")
cluster_loads = df.groupby('cluster')['current_load'].sum().reset_index()
plt.figure(figsize=(12, 6))
sns.barplot(x=cluster_loads['cluster'], y=cluster_loads['current_load'], palette='viridis')
plt.xlabel("Charging Station Cluster", fontsize=14)
plt.ylabel("Total Energy Load", fontsize=14)
plt.title("Energy Load Distribution Across Charging Stations", fontsize=18)
st.pyplot(plt)

# Footer
st.markdown("""
<div style="text-align: center; padding: 20px;">
    <p>Charging Infrastructure Optimization Dashboard | Powered by AI & ML</p>
    <p>&#169; 2024 Your Company. All rights reserved.</p>
</div>
""", unsafe_allow_html=True)
