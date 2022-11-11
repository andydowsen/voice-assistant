import streamlit as st
import pandas as pd
import numpy as np
import components.sidebar as root_component

st.title("New summaries")
st.caption("Some content is here")

sidebar_headline = st.sidebar.title("Friday,")
root_component.streamLit_sidebar()

