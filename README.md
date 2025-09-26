# Shopper-Spectrum : Customer Segmentation and Product Recommendations in E-Commerce


### Project Overview

This project implements a customer segmentation system using RFM (Recency, Frequency, Monetary) analysis and a collaborative filtering-based product recommendation system for an e-commerce dataset. It includes a Jupyter notebook for data processing and analysis and a Streamlit web application for real-time predictions.


### 📣 Problem Statement

    The global e-commerce industry generates vast amounts of transaction data daily, offering valuable insights into customer purchasing behaviors. Analyzing this data is essential for identifying meaningful customer segments and recommending relevant products to enhance customer experience and drive business growth. 
    This project aims to examine transaction data from an online retail business to uncover patterns in customer purchase behavior, segment customers based on Recency, Frequency, and Monetary (RFM) analysis, and develop a product recommendation system using collaborative filtering techniques


### 📌 Real-time Business Use Cases:

    ●	Customer Segmentation for Targeted Marketing Campaigns
    
    ●	Personalized Product Recommendations on E-Commerce Platforms
    
    ●	Identifying At-Risk Customers for Retention Programs
    
    ●	Dynamic Pricing Strategies Based on Purchase Behavior
    
    ●	Inventory Management and Stock Optimization Based on Customer Demand Patterns
    
  
### 📌Dataset Description


| Column          | Description |
------------------|-----------
| InvoiceNo     	| Transaction number |
| StockCode	      | Unique product/item code |
| Description	    | Name of the product |
| Quantity	      | Number of products purchased |
| InvoiceDate	    | Date and time of transaction (2022–2023) |
| UnitPrice	      | Price per product |
| CustomerID	    | Unique identifier for each customer |
| Country	        | Country where the customer is based |


### 🛠️ Skills & Tools Used

    Python, Pandas, NumPy
    
    EDA & Visualization: Matplotlib, Seaborn
    
    Preprocessing: Outlier Handling, Transformation
    
    Feature Engineering: Derived Recency(R), Frequency(F), Monetary(M)
    
    Clustering Models: K-Means, Silhouette Score, Elbow Curve
    
    Model Deployment: Streamlit
    
    Model Saving: Pickle


### 🔍 Workflow & Tasks

1️⃣ Data Understanding & Cleaning

    Loaded and explored dataset using pandas
    
    Checked data types, missing values, duplicates

2️⃣ Exploratory Data Analysis

    Distribution plots based on Countries With No.of.Orders, Products with Quantity, Monthly Sale Trend, CustomerID with Total_amount_spent

3️⃣ Feature Engineering

    Recency by using CustomerID and InvoiceDate column were able to find the recent of customer visit.
    
    Frequency by using CustomerID and Number of InvoiceNo column were able to find of often the customer visit.
    
    Monetary by using CustomerID and Total_amount column were able to find the how much the customer spent on total.

4️⃣ Data Transformation

    Outlier removal (IQR)

5️⃣ Clustering Techniques:
 
    Used Elbow Curve, Silhouette Score to find the optimal cluster group.

6️⃣ Model Deployment

    Saved the best model using pickle
    
    Built an interactive Streamlit app
    
    App used to determine the customer segmentation and provide the product recommendation.


### 🚀 Streamlit App Demo User can input:

  #### Product Recommedation
    Provide Product name and get similar product as recommendation.
  
  #### Customer Segmentation
    Provide the Recency, Frequency, Monetary and get the customers segment.
  
