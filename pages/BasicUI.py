import streamlit as st
import pandas as pd
import numpy as np
from datetime import datetime, date, time

st.set_page_config(
    page_title="Streamlit UI Examples",
    layout="wide"
)


# BASIC TEXT ELEMENTS

st.title("Streamlit UI Examples")
st.header(" | In here 24 basic streamlit UI component examples. |")
st.subheader("This is a Subheader example")

st.text("This is plain text.")
st.markdown("**Markdown text** with _formatting_.")
st.code("print('Hello Streamlit')", language="python")
st.latex(r"This-is-LaTex-syntax: E=mc^2")

st.divider()


# INPUT COMPONENTS

st.header("Input Components")

text = st.text_input("A Text Input")
textarea = st.text_area("A Text Area")

num = st.number_input("A Number Input", min_value=0, max_value=100)

slider = st.slider("A slider", 0, 100, 50)

checkbox = st.checkbox("A checkbox")

toggle = st.toggle("A Toggle Switch")

radio = st.radio(
    "These are radio buttons",
    ["Option 1", "Option 2", "Option 3"]
)

select = st.selectbox(
    "Selectbox",
    ["Python", "Java", "C++"]
)

multi = st.multiselect(
    "Multiselect",
    ["HTML", "CSS", "JavaScript", "Python"]
)

color = st.color_picker("Picking a color")

date_input = st.date_input("Select Date", date.today())

time_input = st.time_input("Select Time", datetime.now().time())

file = st.file_uploader("Upload File")

st.divider()


# BUTTONS

st.header("Buttons")

if st.button("Click Me"):
    st.success("Button clicked!")

st.download_button(
    "Download Sample File",
    data="Hello, this is a sample file.",
    file_name="sample.txt"
)


