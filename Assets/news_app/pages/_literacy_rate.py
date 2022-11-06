import streamlit as st
import random
import numpy as np
import pandas as pd
import pyttsx3
import asyncio

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)


async def speakFunc(audio):
    engine.say(audio)
    engine.runAndWait()
    engine.endLoop()


random_Number_Graph = random.randint(1, 100)


async def graph_visualization():
    st.title("Current, literacy rate")
    random_chart = pd.DataFrame(
        np.random.randn(10, 6),
        columns=["Ukraine", "Japan", "China", "Portugal", "India", "South Korea"]
    )
    st.area_chart(random_chart)
    async_audio = await asyncio.gather(speakFunc(audio="Streams"))
    asyncio.run(async_audio)


asyncio.run(graph_visualization())


engine.endLoop()