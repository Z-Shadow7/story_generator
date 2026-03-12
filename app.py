import streamlit as st
from dotenv import load_dotenv
import os
from components.ui import render_header, render_story

load_dotenv(override=True)
api_key = os.getenv("GROQ_API_KEY")
hf_api_key = os.getenv("HF_API_KEY")

render_header()
render_story(api_key, hf_api_key)