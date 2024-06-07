import streamlit as st
import numpy as np
import cv2 as cv
from PIL import Image

st.title("Image Blending with Trackbar")

# File upload for two images
uploaded_file1 = st.file_uploader("Choose the first image", type=["jpg", "jpeg", "png"])
uploaded_file2 = st.file_uploader("Choose the second image", type=["jpg", "jpeg", "png"])

if uploaded_file1 is not None and uploaded_file2 is not None:
    # Read the uploaded images
    image1 = np.array(Image.open(uploaded_file1))
    image2 = np.array(Image.open(uploaded_file2))
    
    # Resize images to the same dimensions
    dimensions = (500, 700)
    image1 = cv.resize(image1, dimensions)
    image2 = cv.resize(image2, dimensions)
    
    st.image(image1, caption="First Image", use_column_width=True)
    st.image(image2, caption="Second Image", use_column_width=True)
    
    # Alpha slider
    alpha = st.slider("Alpha", 0, 100, 50) / 100  # Default value is 50

    # Switch button
    blend_switch = st.checkbox("Blend Images")

    if blend_switch:
        # Blend the images
        blended_image = cv.addWeighted(image1, 1 - alpha, image2, alpha, 0)
        # Display the blended image
        st.image(blended_image, caption="Blended Image", use_column_width=True)
    else:
        st.write("Blending is turned off. Use the switch to enable blending.")
