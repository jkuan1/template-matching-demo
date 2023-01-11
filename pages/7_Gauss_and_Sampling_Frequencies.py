import streamlit as st
from skimage import data
import numpy as np
from scipy import ndimage

page = data.brick()
width = 400
worst = 8
st.image("./pictures/gauss_meme.jpg")

st.markdown("""
### Since images are a discrete (or sampled) represenation of a continuous world....

### Lets consider the following problem:

### I want to make the following image smaller (compress it to half the size lets say).
""")

st.image(page, width=width)

st.markdown("""
### Should I just keep every second row and column and discard everything else?
""")

page_half = np.array(page)[::2, ::2]

st.image(page_half)
st.image(page_half, width=width)

st.markdown("""
### What if went further and kept every eighth row and column only?
""")

page_fifth = np.array(page)[::worst, ::worst]
st.image(page_fifth)
st.image(page_fifth, width=width)

st.markdown(
    """
    ### I certainly accomplished my goal of compressing the image... but at a large cost in data (Nyquist Sampling Theorem).
    ### Let's try the same thing but only after we apply a Gaussian filter first.
    """
)

page_gauss_half = ndimage.gaussian_filter(page, sigma=2 / 2)[::2, ::2]
st.image(page_gauss_half)
st.image(page_gauss_half, width=width)

page_gauss_worst = ndimage.gaussian_filter(
    page, sigma=worst / 2)[::worst, ::worst]
st.image(page_gauss_worst)
st.image(page_gauss_worst, width=width)
