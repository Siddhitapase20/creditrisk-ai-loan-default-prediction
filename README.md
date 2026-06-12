# 🏦 CreditRisk AI – Loan Approval Prediction System

A Machine Learning-powered web application that predicts whether a loan application is likely to be approved based on applicant financial and demographic information.

## 🚀 Live Demo

Streamlit App: https://creditrisk-ai-loan-default-prediction-knwg9g6apelv3aqfv8y9mr.streamlit.app/

## 📌 Project Overview

CreditRisk AI helps financial institutions assess loan approval probability using historical loan application data. The system leverages Machine Learning models and feature engineering techniques to predict loan approval outcomes and provide approval probability scores.

## 🎯 Features

* Interactive Streamlit Web Application
* Real-time Loan Approval Prediction
* Approval Probability Score
* Automated Feature Engineering
* Clean and User-Friendly Interface
* Machine Learning-Based Risk Assessment

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-Learn
* XGBoost
* Random Forest Classifier
* Logistic Regression

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Deployment

* Streamlit Cloud

## 📊 Dataset Information

* Total Records: 614
* Features Used: 17
* Target Variable: Loan Approval Status

## ⚙️ Feature Engineering

The following engineered features were created to improve model performance:

* Total Income
* Loan-Income Ratio
* Log Income Transformation
* One-Hot Encoding for Categorical Variables

## 🤖 Models Evaluated

| Model               | Accuracy |
| ------------------- | -------- |
| Logistic Regression | 78.05%   |
| Random Forest       | 78.86%   |
| XGBoost             | 74.80%   |

### Best Performing Model

Random Forest Classifier

## 📈 Input Features

* Gender
* Marital Status
* Dependents
* Education
* Self Employment Status
* Property Area
* Credit History
* Applicant Income
* Coapplicant Income
* Loan Amount
* Loan Term

## 🏗️ Project Structure

CreditRisk-AI/

├── app/

│   └── app.py

├── data/

│   └── loan_data.csv

├── models/

│   └── loan_default_model.pkl

├── notebooks/

│   └── phase1_data_understanding.ipynb

├── requirements.txt

└── README.md

## 📚 Key Learnings

* Data Cleaning and Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Model Training and Evaluation
* Hyperparameter Tuning
* Model Deployment using Streamlit
* End-to-End Machine Learning Pipeline

## 👩‍💻 Author

**Siddhi Tapase**

Computer Engineering Student | Machine Learning Enthusiast | Open Source Contributor

If you found this project useful, feel free to ⭐ the repository.
