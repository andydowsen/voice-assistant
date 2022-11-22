import time
import numpy as np
import pandas as pd
import pyttsx3
import streamlit as st

voice_engine = pyttsx3.init("sapi5")
voice_engine__voices = voice_engine.getProperty("voices")
voice_engine_set_voice = voice_engine.setProperty("voice", voice_engine__voices[1].id)
voice_engine.setProperty("rate", 150)


def __speak_funC__Audio(audio):
    if not voice_engine.inLoop:
        voice_engine.say(audio)
        voice_engine.runAndWait()

    elif voice_engine.inLoop:
        voice_engine.endLoop()
        voice_engine.stop()

def _sidebar_data__():
    st.sidebar.selectbox(
        "How would you like to be contacted?",
        ("Email", "Home phone", "Mobile phone")
    )

    with st.sidebar:
        st.radio(
            "Choose a shipping method",
            ("Standard (5-15 days)", "Express (2-5 days)")
        )


def __chart_visualization():
    st.header("Current, Literacy rate")
    chart_data = pd.DataFrame(
        np.random.randn(50, 5),
        columns=["India", "China", "Japan", "North Korea", "South Korea"])

    st.bar_chart(chart_data)


__chart_visualization()
_sidebar_data__()
__speak_funC__Audio("Here you go")

if __name__ == "__main__":
    print(__name__)
