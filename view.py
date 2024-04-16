import streamlit as st
def calculate_interest(principal, rate, time):
 # Suponha que esta função tenha uma lógica complexa
 return (principal * rate * time) / 100
principal = st.number_input("Principal Amount", value=1000)
rate = st.number_input("Interest Rate", value=5)
time = st.number_input("Time (in years)", value=1)
interest = calculate_interest(principal, rate, time)
st.write(f"The interest is {interest}")
