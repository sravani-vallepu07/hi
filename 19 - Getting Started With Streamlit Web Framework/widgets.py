import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")

name=st.text_input("enter your name:")


age=st.slider("select your age:",0,100,15)

st.write(f"your age is {age}.")

options=["python","java","c++","javascript"]
choice=st.selectbox("choose your favourite language",options)
st.write(f"you selected{choice}")

if name:
    st.write(f"hello {name}")


data={
        "name":["john","jane","jake","jill"],
        "age":[28,24,35,40],
        "city":["new york","los angles","chicago","houston"]
     }

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)


uploaded_file=st.file_uploader("choose a csv file",type='csv')

if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)