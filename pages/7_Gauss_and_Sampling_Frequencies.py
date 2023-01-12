import streamlit as st
from skimage import data
import numpy as np
from scipy import ndimage
from PIL import Image

bricks = data.brick()
width = 400
scale_down = 8
st.image("./pictures/gauss_meme.jpg")

st.markdown("""
### Since images are a discrete (or sampled) represenation of a continuous world....

### Lets consider the following problem:

### I want to make the following image smaller (compress it to half the size lets say).
""")

st.image(bricks, width=width)

st.markdown("""
### Should I just keep every second row and column and discard everything else?
""")

bricks_half = np.array(bricks)[::2, ::2]

st.image(bricks_half)
st.image(bricks_half, width=width)

st.markdown("""
### What if went further and kept every eighth row and column only?
""")

bricks_fifth = np.array(bricks)[::scale_down, ::scale_down]
st.image(bricks_fifth)
st.image(bricks_fifth, width=width)

st.markdown(
    """
    ### I certainly accomplished my goal of compressing the image... but at a large cost in data (Nyquist Sampling Theorem).
    ### Let's try the same thing but only after we apply a Gaussian filter first.
    """
)

bricks_gauss_half = ndimage.gaussian_filter(bricks, sigma=2 / 2)[::2, ::2]
st.image(bricks_gauss_half)
st.image(bricks_gauss_half, width=width)

bricks_gauss_scale_down = ndimage.gaussian_filter(
    bricks, sigma=scale_down / 2)[::scale_down, ::scale_down]
st.image(bricks_gauss_scale_down)
st.image(bricks_gauss_scale_down, width=width)

st.markdown("# Lets keep trying other values!")
resize = st.slider("How much to scale the image down by", 1, 50, 1)

bricks_gauss_resize = ndimage.gaussian_filter(bricks, sigma = resize / 2)[::resize, :: resize]
border = np.zeros((bricks_gauss_resize.shape[0], int( 10 / resize)),dtype=np.int8)
bricks_resize = np.array(bricks)[::resize, :: resize]

bricks_comparison = np.concatenate((bricks_gauss_resize, border, bricks_resize), axis=1)
st.image(bricks_comparison)
st.image(bricks_comparison, width=width)

st.write("""# But Justin, re-sampling after using a gaussian distribution still doesn't replicate what happens when I resize something on my computer!
# Well, that's because our resizing filters have become even more sophisticated. Many more complex algorithms have been created for resampling. For example: Bicubic Interpoloation.""")
st.image(Image.fromarray(bricks).resize((int(bricks.shape[0]/resize), int(bricks.shape[1]/resize)), resample=Image.BICUBIC), width=width)