import streamlit as st
import time

st.title("Health management")

st.sidebar.title(f"Welcome")


def user_utility_component():
    user_name = st.text_input("Enter your name Please : ")
    try:
        with open(f"./reports/{user_name}.txt", "x", encoding='utf-8') as append_file:
            st.caption(f"welcome, {user_name}")
            print(append_file)
    except FileExistsError as file_already_incurred:
        st.text(f"Welcome, {user_name} ")
        with open(f"./reports/{user_name}.txt", 'r', encoding='utf-8') as read_file_:
            st.text(read_file_.read())
        print("File is already init")
        print(file_already_incurred)
    else:
        return "Not found"


user_utility_component()
