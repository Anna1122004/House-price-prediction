import streamlit as st
import joblib

model = joblib.load("house_price_prediction.pkl")

st.title("House Price Prediction")

Area = st.number_input(
    "Enter Area",
    min_value=0.0,
    value=1200.0
)

Bedrooms = st.number_input(
    "Enter number of bedrooms",
    min_value=0.0,
    value=3.0
)

Floor = st.number_input(
    "Enter the number of floors",
    min_value=0.0,
    value=2.0
)

if st.button("Predict"):

    if Area < 600:
        st.error("Area cannot be less than 600.")

    elif Area > 3000:
        st.error("Area cannot be more than 3000.")

    elif Bedrooms < 1:
        st.error("Number of bedrooms must be at least 1.")

    elif Bedrooms > 4:
        st.error("Number of bedrooms cannot be more than 4.")

    elif Floor < 1:
        st.error("Number of floors must be at least 1.")

    elif Floor > 10:
        st.error("Number of floors cannot be more than 10.")

    else:
        prediction = model.predict([[Area, Bedrooms, Floor]])

        st.success(
            f"Predicted House Price: ₹{prediction[0]:,.2f} Lakhs"
        )
