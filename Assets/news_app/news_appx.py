import streamlit as st
import pandas as pd
import numpy as np
from streamlit_card import card
import components.sidebar as root_component
from components.__card import __header_Card

sidebar_headline = st.sidebar.title("Friday,")
root_component.streamLit_sidebar()


def __header__viewport():
    st.title("Summaries")


__header__viewport()
