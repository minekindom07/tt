import streamlit as st
import json
from streamlit_webrtc import webrtc_streamer
import whisper
import tempfile
import os
audio_value=st.audio_input("Record the voice")
if audio_value:
    st.audio(audio_value)
