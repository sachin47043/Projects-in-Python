import streamlit as st
st.title("Streamlit app of vgu")
st.text("welcome to my dashboard")
st.header("I am header")
st.write("you can write",20+20)

name = st.text_input("enter your name:\n")
age = st.number_input("enter your age:")
st.write("your name is:", name , "your age is:", age)