import streamlit as st
from skimage import data
import numpy as np

st.set_page_config(page_title="How is Computer Vision Accompished", page_icon="❓")

st.markdown(
    """
    # Harnessing the power of the matrix

    """
)

st.image("./pictures/matrix.jpg")

st.markdown(
    """

    ## Images are just a matrix of numbers! 

    ### Grey scale images are 2D (basically an excel sheet)
    ### Coloured images are 3D matrices

    #### Knowing how to manipulate these matrices is the foundation of computer vision!
    """
)

coins = data.coins()

st.dataframe(coins)
st.write(coins.shape)
st.image(coins)

cat = data.chelsea()
cat_matrix = []

i = 0
while i < cat.shape[0]:
    row = []
    j = 0
    while j < cat.shape[1]:
        cell = str(cat[i,j,:])
        row.append(cell)
        j +=1

    cat_matrix.append(row)
    i += 1

st.dataframe(cat_matrix)
st.write(cat.shape)
st.image(cat)
