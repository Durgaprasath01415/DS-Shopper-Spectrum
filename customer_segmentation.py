import streamlit as st
import numpy as np
import pickle
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# --- Load models and data ---
kmeans = pickle.load(open("kmeans_model.pkl", "rb"))
scaler = pickle.load(open("rfm_scaler.pkl", "rb"))

# --- Module 2: Customer Segmentation ---

st.subheader("Predict Customer Segment (RFM Based)")

recency = st.number_input("Recency (days since last purchase)", min_value=0, value=30)
frequency = st.number_input("Frequency (number of purchases)", min_value=1.0, value=5.0)
monetary = st.number_input("Monetary Value (total spend)", min_value=1.0, value=100.0)


def predict_cluster(recency, frequency, monetary):
    rfm_scaled = scaler.transform([[recency, frequency, monetary]])
    cluster = kmeans.predict(rfm_scaled)[0]
    st.write("Predicted Cluster ID:", cluster)  
    
    cluster_labels = {
        0: 'Regular',
        1: 'High-Value',
        2: 'At-Risk'
    }

    segment = cluster_labels.get(cluster)
    st.success(f"Predicted Customer Segment: **{segment}**")

if st.button("Predict Customer Segment"):
    segment = predict_cluster(recency, frequency, monetary)