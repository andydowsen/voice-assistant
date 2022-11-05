import streamlit as st
import random
import numpy as np
import pandas as pd
import pyttsx3

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


def speakFunc(audio):
    engine.say(audio)
    engine.runAndWait()


random_Number_Graph = random.randint(1, 100)


def graph_visualization():
    st.title("Current, literacy rate")

    random_chart = pd.DataFrame(
        np.random.randn(10, 6),
        columns=["Ukraine", "Japan", "China", "Portugal", "India", "South Korea"]
    )
    st.area_chart(random_chart)
    speakFunc("Hello, I'm friday I created a graph for you")


graph_visualization()
