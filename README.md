# Retail Demand Forecasting & Sales Prediction

## Project Overview

This project uses Machine Learning and time-series feature engineering to predict retail product demand.

The system analyzes historical sales patterns, product price, promotions, holidays, store information, and historical demand features to predict the expected number of units sold.

A Random Forest Regression model is trained and deployed through a Streamlit web application.

---

## Objectives

- Analyze historical retail sales data.
- Identify demand patterns and seasonality.
- Perform exploratory data analysis.
- Create time-series forecasting features.
- Train a Machine Learning regression model.
- Compare the ML model with a Lag-7 baseline.
- Evaluate model performance using MAE, RMSE, and R².
- Build an interactive Streamlit prediction application.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Random Forest Regression
- Time-Series Feature Engineering
- Streamlit
- Jupyter Notebook
- Joblib
- Git & GitHub

---

## Dataset

A synthetic retail sales dataset was created specifically for this project.

The dataset contains:

- Date
- Store
- Product
- Category
- Price
- Promotion
- Holiday
- Units Sold
- Revenue

The dataset covers multiple stores and products across several years.

---

## Exploratory Data Analysis

The project analyzes:

- Daily sales trends
- Monthly sales trends
- Category-level demand
- Store-level demand
- Promotion impact
- Holiday impact
- Price vs. demand
- Day-of-week demand patterns

---

## Feature Engineering

Time-series features were created to capture historical demand patterns:

- Lag-1 sales
- Lag-7 sales
- Lag-14 sales
- 7-day rolling average
- 14-day rolling average
- Year
- Month
- Day of Week

Rolling features were calculated using previous observations to avoid using the current target value as an input.

---

## Machine Learning Model

### Random Forest Regression

The project uses a Random Forest Regressor to predict:

**Target Variable: `Units_Sold`**

The data was divided chronologically into:

- 80% Training Data
- 20% Testing Data

A chronological split was used because this is a forecasting problem.

---

## Baseline Comparison

The Random Forest model was compared against a simple:

**Lag-7 Baseline**

The baseline predicts demand using sales from seven days earlier.

This provides a reference point for evaluating whether the Machine Learning model improves upon a simple forecasting strategy.

---

## Model Evaluation

The models are evaluated using:

### MAE

Mean Absolute Error measures the average absolute difference between actual and predicted demand.

### RMSE

Root Mean Squared Error gives greater weight to larger prediction errors.

### R²

R² measures the proportion of variation in demand explained by the model.

The detailed results are available in:

```text
outputs/model_performance.csv