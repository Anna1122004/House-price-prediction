import streamlit as st
import joblib
model = joblib.load("🤡house_price_prediction.pkl")
st.title("House Price Prediction")
Area = st.number_input(
    "Enter Area",
    min_value=0.0,
    value=400.0
)
Bedrooms = st.number_input(
    "Enter number of bedrooms",
    min_value=0.0,
    value=4.0
)
Age = st.number_input(
    "Enter the age of the House",
    min_value=0.0,
    value=7.0
)
if st.button("Predict"):
    if Area < 200:
        st.error("Area cannot be less than 200.")
    
    elif Area > 600:
        st.error("Area cannot be more than 600.")
    elif Bedrooms < 1:
        st.error("Number of bedrooms must be at least 1.")

    elif Bedrooms > 7:
        st.error("Number of bedrooms cannot be more than 7.")
    elif Age < 5:
        st.error("House age cannot be less than 5 years.")

    elif Age > 25:
        st.error("House age cannot be more than 25 years.")

    else:
        prediction = model.predict([[Area, Bedrooms, Age]])

        st.success(
            f"Predicted House Price: ${prediction[0]:,.2f}"
        )
