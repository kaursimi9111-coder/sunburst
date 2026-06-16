import pandas as pd
import plotly.express as px
import streamlit as st

df=pd.DataFrame({
    "Name":["Nanita","Balraj","Simarjit","David","Amit"],
    "class":["10th","10th","10th","10th","10th"],
    "Roll Number":[101,102,103,104,105],
    "Obtained_Marks":[85,90,78,92,88]
})
fig=px.sunburst( df,path=["class","Name"],values="Roll Number",title="Student by class and Roll Number")
st.plotly_chart(fig)