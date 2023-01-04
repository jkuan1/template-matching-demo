import streamlit as st
import numpy as np
from skimage import data

st.markdown(
    """
    # Lets try it out!
    """
)

editable_cat = data.chelsea()

x_coord = st.slider("Move the filter left to right", 0, 100, 0)
y_coord = st.slider("Move the filter top to bottom", 0, 100, 0)

red = st.number_input("RED VALUE", 0, 255, 255)
green = st.number_input("GREEN VALUE", 0, 255, 0)
blue = st.number_input("BLUE VALUE", 0, 255, 0)

filter_size = st.slider("Filter size", 5, 50, 5)

colour = [red, green, blue]

filter = np.full((filter_size, filter_size, 3), [red, green, blue])

def run():
    editable_cat[x_coord:filter_size, y_coord:filter_size, :] = [red, green, blue]
    st.image(filter)
    st.image(editable_cat)

run()