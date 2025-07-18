import streamlit as st

st.title("streamlit workshop")
name=st.text_input("enter ")
st.write(f"Hello {name}")