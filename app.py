import streamlit as st 

st.title("Assignment 8")
a=st.number_input("Enter First Number")
b=st.number_input("Enter Second Number")
c=st.number_input("Enter Third Number")

max=max(a,b,c)
st.text("")
st.text("")
st.text("")
st.write(max)