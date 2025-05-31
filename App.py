# restaurant_dashboard.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data
df = pd.read_csv("semarang_resto_dataset.csv")

# Sidebar navigation
st.sidebar.title("📊 Restaurant Dashboard")
page = st.sidebar.radio("Pilih Halaman:", [
    "1. Background", 
    "2. Data Visualization", 
    "3. Clustering", 
    "4. Restaurant by Cluster", 
    "5. Profile"
])
