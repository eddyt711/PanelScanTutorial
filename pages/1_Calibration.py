import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Calibration")
st.header('Calibration Tutorial')

st.markdown(
    """
    This video explains how to calibrate the system. It covers:
    - What a calibration is and why we need it.
    - How to take an image for calibrating.
    - How to perform the calibration using the app.
"""
)

st.markdown("\n \n")


video_file = open('ComputerVisionCalibration.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)