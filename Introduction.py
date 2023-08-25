import streamlit as st
import pandas as pd
import numpy as np

# Start here:

st.set_page_config(page_title="Getting Started")
st.header('Introduction to the panel scanning system:')

st.markdown(
    """
    This video introduces the TWC panel scanning system. It covers:
    - What the system is designed to do.
    - How the equipment works.
    - How to use the system and software.
"""
)

st.markdown("\n \n")


video_file = open('ComputerVisionIntroductionTutorial.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)