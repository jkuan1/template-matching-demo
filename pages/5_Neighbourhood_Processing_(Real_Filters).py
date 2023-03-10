import streamlit as st


st.set_page_config(
    page_title="Neighbourhood Operations", page_icon="")

st.markdown(
    """
    # Let's get a little more hardcore with our filtering now ;) 
    """
)

st.markdown(
    """
    # What if the neighbouring pixels of a point affects the output image? 
    """
)

st.image("./pictures/neighbourhood_operation.png")

st.image("./pictures/linear_filter_example.png")

st.image("./pictures/cat_grad_filter.jpg")
