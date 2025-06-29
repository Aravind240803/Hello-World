import streamlit as st
from demo import area_of_circle

st.title("Hello, Streamlit!")
st.write("This is a simple Streamlit app to demonstrate the setup.")


page = st.sidebar.selectbox("Select a page:", ["Home", "Circle Area Calculator"])
if page == "Home":
    st.write("Welcome to the home page!")

if page == "Circle Area Calculator":
    st.write("Calculate the area of a circle by entering its radius.")  
    radius = st.slider("Enter the radius of the circle:", min_value=0.0, value=100.0, step=0.1)
    area = area_of_circle(radius)
    st.write(f"The area of the circle with radius {radius:.2f} is: {area:.2f}")