import streamlit as st
import pandas as pd
import pickle
import warnings

# Suppress warnings
warnings.filterwarnings("ignore")

# --- Load models and data ---
similarity_df = pd.read_pickle("product_recommendation.pkl")

# --- Page setup ---
st.set_page_config(page_title="Shopper Spectrum App", layout="centered")
st.title("🛍️ Shopper Spectrum Customer and Recommendations Assistant")

# --- Module 1: Product Recommendation ---

st.subheader("Find Similar Products")
product_name = st.text_input("Enter a Product Name")

if st.button("Get Recommendations"):
    if product_name in similarity_df.columns:
        sim_scores = similarity_df[product_name].sort_values(ascending=False)
        top_similar = sim_scores.iloc[1:6]  # skip itself
        st.success("Top 5 Similar Products:")
        for i, (prod, score) in enumerate(top_similar.items(), 1):
            st.write(f"{i}. {prod} (Similarity: {score:.2f})")
    else:
        st.error("Product not found. Please try another.")
