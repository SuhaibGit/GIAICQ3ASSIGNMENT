import streamlit as st
import pandas as pd
import os
from io import BytesIO

st.set_page_config(page_title="💿Data sweeper",layout='wide')
st.title("💿Data sweeper")
st.write("Transform your file between CSV and Excel formats with built-in data cleaning and visulization!")
uploadFile=st.file_uploader("place you CSV or Excel file here",type=["csv","xlsx"],accept_multiple_files=True)
if uploadFile:
    for file in uploadFile:
        file_ext =os.path.splitext(file.name)[-1].lower()
        if file_ext==".csv":
            df=pd.read_csv(file)
        elif file_ext==".xlsx":
            df=pd.read_excel(file)
        else:
            st.write(f"Unsupported file type:{file_ext}")
            continue
        st.write(f"**File Name:**{file.name}")
        st.write(f"**File Size:**{file.size/1024}")
        st.write("Preview the head of the data")
        st.dataframe(df.head())
        st.subheader("Data cleaning options")
        if st.checkbox(f"Clean data for {file.name}"):
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"Remove Duplicates for {file.name}"):
                    df.drop_duplicates(inplace=True)
                    st.write("Duplicates Removed!")
            with col2:
                if st.button(f"Fill missing values for {file.name}"):
                    numericCols=df.select_dtypes(include=['number']).columns
                    df[numericCols]=df[numericCols].fillna(df[numericCols].mean())
                    st.write("Missing values have been filled")
        
        st.subheader("Select Columns to Convert")
        columns=st.multiselect(f"Choose Columns for {file.name}",df.columns,default=df.columns)
        df=df[columns]
        st.subheader("📈 Data Visualization")
        if st.checkbox(f"Show Visualization for {file.name}"):
            st.bar_chart(df.select_dtypes(include='number').iloc[:,:2])
        st.subheader("🔀Conversion Options")
        conType=st.radio(f"Convert {file.name} to:",["CSV","EXCEL"], key=file.name)
        if st.button(f"Convert{file.name}"):
            buffer =BytesIO()
            if conType=="CSV":
                df.to_csv(buffer,index=False)
                file_name= file.name.replace(file_ext,".csv")
                mimeType="text/csv"
            elif conType=="EXCEL":
                df.to_excel(buffer,index=False)
                file_name=file.name.replace(file_ext,".xlsx")
                mimeType="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            buffer.seek(0)

            st.download_button(
                label=f"⬇️ Download{file.name} as {conType}",
                data=buffer,
                file_name=file_name,
                mime=mimeType
            )
st.success("🎉All file processed!")
