import streamlit as st
import numpy as np
from PIL import Image

st.set_page_config(
    page_title="How is Computer Vision Accompished", page_icon="❓")

st.markdown(
    """
    # Harnessing the power of the matrix

    """
)

st.image("./pictures/matrix.jpg")

st.markdown(
    """

    # Images are just a matrix of numbers! 

    ### Grey scale images are 2D (basically an excel sheet)
    ### Coloured images are 3D matrices

    ### All pixel intensities will always be in the range of 0 to 255
    """
)

tofu_pic = Image.open("./pictures/tofu.jpg").resize((300, 400), Image.BICUBIC)
tofu_bw = tofu_pic.convert("L")
tofu_matrix = np.asarray(tofu_pic)

st.dataframe(np.asarray(tofu_bw))
st.write(tofu_bw.size)
st.image(tofu_bw)

tofu_list = np.ndarray.tolist(tofu_matrix)

st.dataframe(tofu_list)
st.write(tofu_matrix.shape)
st.image(tofu_pic)
