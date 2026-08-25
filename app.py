import streamlit as st


st.title("BMI Calculator")
st.write("This application is used to calculate BMI ")

weight=st.number_input("Enter your Weight(in kg)",min_value=20,placeholder="type your weight here")
height=st.number_input("Enter your Height(in cm)",min_value=30,placeholder="type your height here")
bmi=weight/(height/100)**2
st.success(f"Your BMI is {bmi:.2f}")

if bmi<18.5 and bmi>0:
    st.warning("You are underweight")
elif bmi>=18.5 and bmi<25:
    st.success("You have a normal weight")
elif bmi>=25 and bmi<30:
    st.warning("You are overweight")
else:
    st.error("You are obese")