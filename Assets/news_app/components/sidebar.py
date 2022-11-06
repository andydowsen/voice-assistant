import streamlit as st
import time


def streamLit_sidebar():
    st.sidebar.slider(
        "How many results you want",
        0, 10
    )
    category_value = ["News", "sports", "Entertainment"]
    len(category_value)
    st.sidebar.selectbox(
        "Choose your category",
        category_value
    )
    col1, col2 = st.columns([2, 1])
    with col1:
        st.sidebar.button(
            "Login now",
            type="primary"
        )
    with col2:
        st.sidebar.button(
            "Sign up",
            type="secondary"
        )


if __name__ == "__main__":
    print(__name__)
