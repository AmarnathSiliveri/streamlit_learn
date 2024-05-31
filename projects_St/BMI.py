import streamlit as st

# Set page title and icon
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️",)


# Title of the app
st.title("BMI Calculator")

# Sidebar for input
st.sidebar.title("📝Input your details ")

# User inputs for height and weight
height = st.sidebar.number_input("Enter your height in centimeters:", min_value=0.0, format="%.3f")
weight = st.sidebar.number_input("Enter your weight in kilograms:", min_value=0.0, format="%.3f")

# Calculate BMI
if height > 0 and weight > 0:
    height_m = height / 100  # convert height to meters
    bmi = weight / (height_m ** 2)
    st.subheader(f"Your BMI is: {bmi:.2f}")
    
    # Interpretation of the BMI
    if bmi < 18.5:
        st.error("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        st.success("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")
else:
    st.write("Please enter valid height and weight to calculate your BMI.")

# Footer
st.write("""
### About
BMI (Body Mass Index) is a measure of body fat based on height and weight that applies to adult men and women. Use this tool to calculate and interpret your BMI.
""")





