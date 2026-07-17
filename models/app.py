import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# Page Configuration
st.set_page_config(
    page_title="Crop Disease Detection System",
    page_icon="🌿",
    layout="centered"
)

st.title("🌿 Crop Disease Detection System")
st.write("Upload a leaf image to detect the disease using AI.")
import traceback
from tensorflow.keras.models import load_model

try:
    model = load_model("../models/mobilenet_final.keras")
    print("Model loaded successfully")
except Exception:
    traceback.print_exc()
