import streamlit as st
import requests
from time import sleep

def generate_image(image_prompt: str, api_key: str) -> bytes:
    API_URL = "https://router.huggingface.co/hf-inference/models/stabilityai/stable-diffusion-xl-base-1.0"
    headers = {"Authorization": f"Bearer {api_key}"}
    
    for attempt in range(3):
        try:
            response = requests.post(
                API_URL,
                headers=headers,
                json={"inputs": image_prompt},
                timeout=60
            )
            if response.status_code == 200:
                return response.content
            elif response.status_code == 503:
                st.info(f"Model loading, retrying... ({attempt+1}/3)")
                sleep(10)
            else:
                st.warning(f"Error: {response.status_code}")
                return None
        except requests.exceptions.Timeout:
            sleep(2)
    return None

def render_image(image_prompt: str, scene_number: int, api_key: str) -> bytes:
    with st.spinner(f"Generating image for scene {scene_number}..."):
        image_bytes = generate_image(image_prompt, api_key)
        if image_bytes:
            st.image(image_bytes, width='stretch')
            return image_bytes
        else:
            st.warning(f"⚠️ Could not generate image for scene {scene_number}.")
            return None