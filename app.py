import streamlit as st
import pandas as pd
import numpy as np



#displaying text content
st.title("My First Streamlit App")
st.write("Hello, Akshay")
st.text("Lets start!")

#creating charts using pandas and numpy
df=pd.DataFrame(np.random.randn(10,2),columns=['A','B'])
st.line_chart(df)
st.bar_chart(df)

#sidebar ,image and video
st.sidebar.title("Navigation")
st.image("https://www.google.com/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png")
st.caption("Google Logo")
st.video("https://youtu.be/SbP1CN4rTlo?si=zCXG2zHByDU1pweR")

#file upload (csv)
uploaded_file=st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data=pd.read_csv(uploaded_file)
    st.write(data)

#taking user input
name=st.text_input("Enter your name")
if st.button("Submit"):
    st.success(f"Hello, {name}!")

#text and markdown formatting
st.header("This is a header")
st.subheader("This is a subheader")
st.markdown("**Bold**,*Italic*, `Code`,[Link](https://www.google.com)")
st.code("for i in range(5):\n   print(i)",language="python")
