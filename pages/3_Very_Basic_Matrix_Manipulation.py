import streamlit as st
from utils import show_code


st.set_page_config(
    page_title="Let Chelsea show us how its done", page_icon="")

st.markdown(
    """
    # Lets try it out!
    """
)


def render_cat():
    from skimage import data
    import numpy as np

    cat = data.chelsea()
    cat_dims = cat.shape

    # Interactive elements

    red = st.number_input("RED VALUE", 0, 255, 255)
    green = st.number_input("GREEN VALUE", 0, 255, 0)
    blue = st.number_input("BLUE VALUE", 0, 255, 0)

    filter_size = st.slider("Filter size", 5, 200, 5)

    filter = np.full((filter_size, filter_size, 3), [red, green, blue])

    st.write("The filter that has been configured:")
    st.image(filter)

    x_coord = st.slider("Move the filter left to right",
                        0, cat_dims[1] - filter_size, 0)
    y_coord = st.slider("Move the filter top to bottom",
                        0, cat_dims[0] - filter_size, 0)

    # matrix manipulation
    cat[y_coord:y_coord + filter_size,
        x_coord:x_coord + filter_size, :] = [red, green, blue]

    return cat


st.image(render_cat())
show_code(render_cat)
