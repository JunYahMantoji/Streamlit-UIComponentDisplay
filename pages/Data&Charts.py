import streamlit as st
import pandas as pd
import numpy as np

st.title("Data Display and Charts (7 more new components)")

st.header("Data Display Using Pandas (Data is Randomly Generated)")

data = pd.DataFrame(
    np.random.randn(10,3),
    columns=["A","B","C"]
)

st.dataframe(data)
st.table(data)

st.metric("Temperature", "25°C", "+1.2°C")


st.subheader("These are different types of charts you can use to visualize data")
st.text("We're using the random data generated above for these charts")
st.line_chart(data)
st.bar_chart(data)
st.area_chart(data)

st.divider()


