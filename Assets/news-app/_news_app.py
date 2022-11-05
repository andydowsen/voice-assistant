import streamlit as slit
import pandas as pd
import numpy as np

slit.title("New summaries")

add_box = slit.sidebar.selectbox(
    "How many news articles you want",
    (2, 4, 8, 10)
)
