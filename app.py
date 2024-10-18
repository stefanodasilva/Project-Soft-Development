import pandas as pd
import plotly.express as px
import streamlit as st

def load_data():
    df = pd.read_csv("Notebooks\Notvehicles_us.csv")
    return df

df=load_data()

st.title("Car Advertisement Dataset")

st.header("Vehicle Price Distribution")

fig_price = px.histogram(df, x="price", title="Distribution of Vehicle Prices", nbins=50)
st.plotly_chart(fig_price)

st.header("Price vs Odometer Scatter Plot")

fig_scatter = px.scatter(df, x="odometer", y="price",
                 title="Scatter Plot:Odometer vs Price",
                 labels={"year":"Year of Manufacture", "price": "Price (USD)"})
st.plotly_chart(fig_scatter)

if st.checkbox("Show Raw Data"):
    st.write("## Raw Dataset")
    st.dataframe(df)
