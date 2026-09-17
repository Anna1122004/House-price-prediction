import streamlit as st
import joblib
model = joblib.load("house_price_prediction.pkl")
st.title("House Price Prediction")
Area= st.number_input(
    "Enter Area",
    min_value=200.0,
    max_value=600.0,
    value=400.0
)
Bedrooms=st.number_input(
    "Enter number of bedrooms",
    min_value=1.0,
    max_value=7.0,
    value=4.0
)
Age=st.number_input(
  "Enter the age of the House",
  min_value=5.0,
  max_value=25.0,
  value=7.0
)


if st.button("Predict"):
   
    
    if Area > 600:
        st.error("Area cannot be more than 600.")
    else:
        prediction = model.predict([[Area, Bedrooms, Age]])

        st.success(f"Predicted House Price: ${prediction[0]:,.2f}")
