import datetime
import pyttsx3
import streamlit as st
import time
import datetime

st.title("Add your diet")

current_time = str(time.asctime(time.localtime(time.time())))
print(current_time)

voice_engine = pyttsx3.init("sapi5")
engine_Voice = voice_engine.getProperty("voices")
set_engine_voice = voice_engine.setProperty("voice", engine_Voice[1])
voice_engine.setProperty("rate", 180)


def _speak_func__audio(audio):
    voice_engine.say(audio)
    voice_engine.runAndWait()
    voice_engine.endLoop()
    voice_engine.stop()


def append_diet_data():
    user_name = st.text_input("Kindly enter your name")
    voice_engine.startLoop()
    _speak_func__audio("Kindly, enter your name")
    voice_engine.stop()

    try:
        with open(f"./reports/{user_name}.txt", "x", encoding='utf-8') as append_file:
            st.caption(f"welcome, {user_name}")
            print(append_file)
            with open(f"./reports/{user_name}.txt", 'r+', encoding='utf-8') as read_file_:
                content_details = st.text_input("Add your details")
                st.text(read_file_.write(content_details))
                st.text(read_file_.read())

    except FileExistsError as file_already_incurred:
        st.text(f"Welcome, {user_name} ")
        with open(f"./reports/{user_name}.txt", 'r+', encoding='utf-8') as read_file_:
            st.time_input("Enter time", datetime.time(8, 45))
            content_details = st.text_input("Add your details")
            st.text(read_file_.write(f"[{current_time}] : {content_details}"))
        print("File is already init")
        print(file_already_incurred)
    else:
        return "Not found"


append_diet_data()
