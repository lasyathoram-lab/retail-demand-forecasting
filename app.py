import streamlit as st
import pandas as pd
import joblib


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📈",
    layout="centered"
)


# --------------------------------------------------
# Load Model and Dataset
# --------------------------------------------------

model = joblib.load(
    "outputs/retail_demand_model.pkl"
)

df = pd.read_csv(
    "data/retail_sales_features.csv"
)

df["Date"] = pd.to_datetime(df["Date"])


# --------------------------------------------------
# App Title
# --------------------------------------------------

st.title("📈 Retail Demand Forecasting")

st.write(
    "Predict expected retail demand using a "
    "Machine Learning model."
)


# --------------------------------------------------
# Store and Product Selection
# --------------------------------------------------

st.subheader("Select Store and Product")

store = st.selectbox(
    "Select Store",
    [
        "Store_1",
        "Store_2",
        "Store_3",
        "Store_4",
        "Store_5"
    ]
)

product = st.selectbox(
    "Select Product",
    [
        "Product_A",
        "Product_B",
        "Product_C",
        "Product_D",
        "Product_E",
        "Product_F",
        "Product_G",
        "Product_H"
    ]
)


# --------------------------------------------------
# Find Selected Store + Product Data
# --------------------------------------------------

selected_data = df[
    (df["Store"] == store) &
    (df["Product"] == product)
].sort_values("Date")


if selected_data.empty:

    st.error(
        "No data found for the selected Store and Product."
    )

    st.stop()


latest = selected_data.iloc[-1]


st.info(
    f"Latest available data: "
    f"{latest['Date'].strftime('%Y-%m-%d')}"
)


# --------------------------------------------------
# Forecast Information
# --------------------------------------------------

st.subheader("Forecast Information")

forecast_date = st.date_input(
    "Forecast Date"
)

price = st.number_input(
    "Product Price",
    min_value=1.0,
    value=float(latest["Price"]),
    step=10.0
)

promotion = st.selectbox(
    "Promotion",
    [0, 1],
    format_func=lambda x: (
        "Yes" if x == 1 else "No"
    )
)

holiday = st.selectbox(
    "Holiday",
    [0, 1],
    format_func=lambda x: (
        "Yes" if x == 1 else "No"
    )
)


# --------------------------------------------------
# Historical Sales Features
# --------------------------------------------------

st.subheader("Historical Sales Information")

st.write(
    "The following values are automatically "
    "taken from the latest available data."
)

lag_1 = latest["Lag_1"]

lag_7 = latest["Lag_7"]

lag_14 = latest["Lag_14"]

rolling_mean_7 = latest["Rolling_Mean_7"]

rolling_mean_14 = latest["Rolling_Mean_14"]


col1, col2 = st.columns(2)

with col1:

    st.metric(
        "Sales 1 Day Ago",
        round(lag_1, 2)
    )

    st.metric(
        "Sales 7 Days Ago",
        round(lag_7, 2)
    )

    st.metric(
        "Sales 14 Days Ago",
        round(lag_14, 2)
    )


with col2:

    st.metric(
        "7-Day Average",
        round(rolling_mean_7, 2)
    )

    st.metric(
        "14-Day Average",
        round(rolling_mean_14, 2)
    )


# --------------------------------------------------
# Prediction
# --------------------------------------------------

st.subheader("Demand Prediction")


if st.button(
    "🔮 Predict Demand",
    use_container_width=True
):

    input_data = pd.DataFrame([{

        "Price": price,

        "Promotion": promotion,

        "Holiday": holiday,

        "Year": forecast_date.year,

        "Month": forecast_date.month,

        "Day_of_Week": forecast_date.weekday(),

        "Lag_1": lag_1,

        "Lag_7": lag_7,

        "Lag_14": lag_14,

        "Rolling_Mean_7": rolling_mean_7,

        "Rolling_Mean_14": rolling_mean_14
    }])


    prediction = model.predict(
        input_data
    )[0]


    prediction = max(
        0,
        round(prediction)
    )


    st.success(
        f"Predicted Units Sold: {prediction}"
    )


    st.write(
        f"For **{store} - {product}**, "
        f"the model predicts approximately "
        f"**{prediction} units**."
    )