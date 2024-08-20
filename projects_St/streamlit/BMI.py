import streamlit as st

# Set page title and icon
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️",)

page_bg = """
<style>
[data-testid='stAppViewContainer'] {
    background-image: url("https://images.unsplash.com/photo-1712979252795-20561805c217?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHx0b3BpYy1mZWVkfDM1fGlVSXNuVnRqQjBZfHxlbnwwfHx8fHw%3D");
    background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0,0,0,0);
}
</style>
"""

# Apply the styling using st.markdown
st.markdown(page_bg, unsafe_allow_html=True)
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





