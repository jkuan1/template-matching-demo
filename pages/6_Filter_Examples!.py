import streamlit as st
from PIL import Image
from scipy import signal, ndimage
import numpy as np
import cv2

einstein_pic = Image.open("./pictures/einstein.jpeg")
einstein_matrix = np.asarray(einstein_pic, np.float32)
width = 200

st.markdown(
    """
    # Lets test out some filters!
    """
)

st.write("Example 1")
ex1_filter = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
st.image(einstein_pic, width=width)
st.table(ex1_filter)
if st.button("Answer to Example 1"):
    answer = signal.convolve2d(einstein_matrix, ex1_filter, 'same')
    answer = np.clip(einstein_matrix, 0, 255)
    answer = answer.astype('uint8')
    st.write("Nothing happens!")
    st.image(answer, width=width)

st.write("Example 2")
ex2_filter = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]
st.image(einstein_pic, width=width)
st.table(ex2_filter)
if st.button("Answer to Example 2"):
    st.write(
        "We get an effect called 'smoothing'. This filter is known as a box filter.")
    answer = signal.convolve2d(einstein_matrix, ex2_filter, 'same')
    answer = np.clip(answer, 0, 255)
    answer = answer.astype('uint8')
    st.image(answer, width=width)

st.write("Example 3")
sap_pic = Image.open("./pictures/salt-and-pepper-effect.png")
st.image(sap_pic)
st.write("Imagine a filter that takes the median of all the neighbouring pixels")
if st.button("Answer to Example 3"):
    st.write(
        "We get an effect called 'smoothing'. This filter is known as a box filter.")
    sap_matrix = np.asarray(sap_pic, np.float32)
    answer = ndimage.median_filter(sap_matrix, size=5)
    # answer = np.clip(answer, 0, 255)
    answer = answer.astype('uint8')
    st.image(answer)
