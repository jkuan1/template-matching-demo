import streamlit as st
from utils import show_code
from skimage import data


st.markdown(
    """
    # Lets try it out!
    """
)

cat_dims = data.chelsea().shape

# Interactive elements

red = st.number_input("RED VALUE", 0, 255, 255)
green = st.number_input("GREEN VALUE", 0, 255, 0)
blue = st.number_input("BLUE VALUE", 0, 255, 0)

filter_size = st.slider("Filter size", 5, 200, 5)

x_coord = st.slider("Move the filter left to right",
                    0, cat_dims[1] - filter_size, 0)
y_coord = st.slider("Move the filter top to bottom",
                    0, cat_dims[0] - filter_size, 0)


def render_cat():
    cat = data.chelsea()
    cat[y_coord:y_coord + filter_size,
        x_coord:x_coord + filter_size, :] = [red, green, blue]
    return cat


st.image(render_cat())
show_code(render_cat)