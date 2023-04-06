
import pandas as pd
import plotly.express as px
import streamlit as st
import numpy as np
df = pd.read_csv("Sales_Store_Preprocessed.csv")
st.title("Sales_Store_Dashboard")

c1 , c2 = st.columns(2)


with c1 :
    st.metric("Total Sales Revenue in M$" , (df["Sales"].sum() / (10 ** 6)).round(3))
    df_sub_profit = df.groupby("Sub-Category").sum()["Profit"].sort_values(ascending=  False).head(10).reset_index()
    fig = px.bar(data_frame= df_sub_profit , x  = "Sub-Category" , y = "Profit" , title = "Top 10 Profited Sub_Category" , width=450)
    st.plotly_chart(fig)

with c2 :
    st.metric("Total Profit in K$" ,(df["Profit"].sum() / (10 ** 3)).round(3) )
    df_month_sales_profit = df.groupby("Month").mean()[["Sales" , "Profit"]].reset_index()
    st.plotly_chart(px.line(data_frame = df_month_sales_profit , x = "Month" , y =["Profit","Sales"] ,width = 450) )

df_pivot = pd.pivot_table(data= df , index = "Year" , columns = "Month" , values = "Profit" , aggfunc=sum)
st.plotly_chart(px.imshow(df_pivot ,text_auto=True))
    

    



