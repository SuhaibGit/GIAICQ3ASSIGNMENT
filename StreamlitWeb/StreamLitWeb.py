import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
st.title("Simple Data Dashboard")
uploaded_file=st.file_uploader("Choose a CSV file",type="csv")
if uploaded_file is not None:
    df= pd.read_csv(uploaded_file)
    st.subheader("Data Preview")
    st.write(df.head())
    st.subheader("Data Summary")
    st.write(df.describe())
    st.subheader("Filter Data")
    columns=df.columns.tolist()
    selectedColumn=st.selectbox("Select column to filter by",columns)
    uniqueValues=df[selectedColumn].unique()
    selectedValue=st.selectbox("Select Value",uniqueValues)
    filtered=df[df[selectedColumn]==selectedValue]
    st.write(filtered)
    st.subheader("Plot Data")
    x_col=st.selectbox("Select the x-axis columns",columns)
    y_col=st.selectbox("Select the y-axis columns",columns)
    if st.button("Generate plot"):
        st.line_chart(filtered.set_index(x_col)[y_col])
else:
    st.write("Waiting on file upload...")
