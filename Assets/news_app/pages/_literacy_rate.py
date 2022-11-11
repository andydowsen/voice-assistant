import streamlit as st
import pandas as pd
import numpy as np
import pyttsx3

voice_engine = pyttsx3.init("sapi5")
voice_engine__voices = voice_engine.getProperty("voices")
voice_engine_set_voice = voice_engine.setProperty("voice", voice_engine__voices[1].id)
voice_engine.setProperty("rate", 160)


def __speak_funC__Audio(audio):
    if not voice_engine.inLoop:
        voice_engine.say(audio)
        voice_engine.runAndWait()
        voice_engine.endLoop()
        voice_engine.stop()

    elif voice_engine.inLoop:
        voice_engine.runAndWait()
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
    __speak_funC__Audio("Chart visualization")


__chart_visualization()
_sidebar_data__()

if __name__ == "__main__":
    print(__name__)
