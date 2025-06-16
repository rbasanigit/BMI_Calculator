import streamlit as st

# Set app title
st.title("BMI Calculator 💪")

# User inputs
st.subheader("Enter your details:")
height = st.slider("Height (in cm)", min_value=100, max_value=250, value=170)
weight = st.number_input("Weight (in kg)", min_value=10.0, max_value=300.0, value=70.0)

# Calculate BMI
height_m = height / 100
bmi = weight / (height_m ** 2)

# Determine BMI category
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight", "blue"
    elif 18.5 <= bmi < 24.9:
        return "Normal", "green"
    elif 25 <= bmi < 29.9:
        return "Overweight", "orange"
    else:
        return "Obese", "red"

category, color = classify_bmi(bmi)

# Display Results
st.subheader("Results:")
st.markdown(f"**Your BMI is:** `{bmi:.2f}`")
st.markdown(f"<h4 style='color:{color};'>Category: {category}</h4>", unsafe_allow_html=True)

# Optional: Add helpful info
with st.expander("ℹ️ What is BMI?"):
    st.write("""
    BMI (Body Mass Index) is a number calculated using your height and weight.
    
    - Underweight: BMI < 18.5  
    - Normal: BMI 18.5–24.9  
    - Overweight: BMI 25–29.9  
    - Obese: BMI ≥ 30  
    """)
