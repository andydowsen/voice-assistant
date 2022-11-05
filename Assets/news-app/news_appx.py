import streamlit as st
import pandas as pd
import numpy as np

st.title("New summaries")
st.caption("Some content is here")

sidebar_headline = st.sidebar.title("Friday Newsapp")

add_box = st.sidebar.text_input(
    "How many news articles you want",
)
check_box = st.sidebar.checkbox(
    "Top Headlines"
)
check_box_2 = st.sidebar.checkbox(
    "Global Headlines"
)

quantity_title = st.sidebar.slider(
    "Quantity of news articles",
    0, 10
)
