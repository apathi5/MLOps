import streamlit as st
st.write("Streamlit Basic Calculator")

#input 2 numbers
number1 = st.number_input("Enter first number")
number2 = st.number_input("Enter second number")

#perform the calculations
addition = number1 + number2
subtraction = number1 - number2
multiplication = number1 * number2


st.write(f"The addition of {number1} & {number2} is {addition}")
st.write(f"The subtraction of {number1} & {number2} is {subtraction}")
st.write(f"The multiplication of {number1} & {number2} is {multiplication}")


