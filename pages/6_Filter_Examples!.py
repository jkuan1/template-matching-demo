import streamlit as st
from PIL import Image
from scipy import signal
import numpy as np
from utils import gauss2d, show_code

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
st.markdown(
    """
    | 0    | 0    | 0    |
    | ---  | ---  | ---  |
    | 0    | 1    | 0    |
    | 0    | 0    | 0    |
    """
)
if st.button("Answer to Example 1"):
    answer = signal.convolve2d(einstein_matrix, ex1_filter, 'same')
    answer = np.clip(einstein_matrix, 0, 255)
    answer = answer.astype('uint8')
    st.write("Nothing happens!")
    st.image(answer, width=width)

st.write("Example 2")
ex2_filter = [[1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1 /
                                                                                                                                                   49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49], [1/49, 1/49, 1/49, 1/49, 1/49, 1/49, 1/49]]
st.image(einstein_pic, width=width)
st.markdown(
    """
    | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 |
    | ---  | ---  | ---  | ---  | ---  | ---  | ---  | 
    | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 |
    | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 |
    | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 |
    | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 |
    | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 |
    | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 | 1/49 |
    """
)
einstein_box = signal.convolve2d(
    einstein_matrix, ex2_filter, 'same').astype('uint8')
if st.button("Answer to Example 2"):
    st.write(
        "We get an effect called 'smoothing'. This filter is known as a box filter.")
    st.image(einstein_box, width=width)

st.write("Example 3")
# sap_pic = Image.open("./pictures/salt-and-pepper-effect.png")
st.image(einstein_pic, width=width)
gauss_kernel = gauss2d(1)
st.markdown(
    """
    | 0.0000 | 0.0002 | 0.0011 | 0.0018 | 0.0011 | 0.0002 | 0.0000 |
    | ---    | ---    | ---    | ---    | ---    | ---    | ---    | 
    | 0.0002 | 0.0029 | 0.0131 | 0.0216 | 0.0131 | 0.0029 | 0.0002 | 
    | 0.0011 | 0.0131 | 0.0586 | 0.0966 | 0.0586 | 0.0131 | 0.0011 | 
    | 0.0018 | 0.0216 | 0.0966 | 0.1592 | 0.0966 | 0.0216 | 0.0018 | 
    | 0.0011 | 0.0131 | 0.0586 | 0.0966 | 0.0586 | 0.0131 | 0.0011 | 
    | 0.0002 | 0.0029 | 0.0131 | 0.0216 | 0.0131 | 0.0029 | 0.0002 | 
    | 0.0000 | 0.0002 | 0.0011 | 0.0018 | 0.0011 | 0.0002 | 0.0000 |
    """
)
einstein_gauss = signal.convolve2d(
    einstein_matrix, gauss_kernel, 'same').astype('uint8')

if st.button("Answer to Example 3"):
    st.write(
        "We still get 'smoothing'. But this is using a filter that replicates the gaussian distribution (bell curve). The formula is: ")
    st.image("./pictures/gaussian_formula.jpg")
    st.write("Visually, this is what it looks like for a 2D domain: ")
    st.image("./pictures/gaussian_distribution.png")
    st.image(einstein_gauss)
    show_code(gauss2d)

st.markdown(
    """
    # BONUS: Box vs Gaussian - Where is the smoothing different?
    """
)
comparison = np.concatenate((einstein_box, einstein_gauss), axis=1)
st.image(comparison)


st.markdown(
    """
    # QUICK DISCLAIMER: Correlations vs Convolutions

    ### This is called cross-correlation:
    """
)

st.image("./pictures/linear_filter_example.png")

st.markdown(
    """
    ### In filtering operations, convolutions are mostly used instead.
    """
)
st.image("./pictures/convolution_demo.jpg")

st.markdown(
    """
    ### Basically correlation but the filter is first rotated 180 degrees. This is because let us have:

    ### A Discrete Unit:
    | 0   | 0   | 0   | 0   | 0   | 
    | --- | --- | --- | --- | --- | 
    | 0   | 0   | 0   | 0   | 0   |
    | 0   | 0   | 1   | 0   | 0   |
    | 0   | 0   | 0   | 0   | 0   |
    | 0   | 0   | 0   | 0   | 0   |
    
    ### A non-symmetric filter:
    | 1   | 2   | 3   |
    | --- | --- | --- |
    | 4   | 5   | 6   | 
    | 7   | 8   | 9   |

    ### Correlated result:
    | 0   | 0   | 0   | 0   | 0   | 
    | --- | --- | --- | --- | --- | 
    | 0   | 9   | 8   | 7   | 0   |
    | 0   | 6   | 5   | 4   | 0   |
    | 0   | 3   | 2   | 1   | 0   |
    | 0   | 0   | 0   | 0   | 0   |

    ### But if we rotated the filter first so that it is:
    | 9   | 8   | 7   |
    | --- | --- | --- |
    | 6   | 5   | 4   | 
    | 3   | 2   | 1   |

    ### Then the (convoluted) result is:
    | 0   | 0   | 0   | 0   | 0   | 
    | --- | --- | --- | --- | --- | 
    | 0   | 1   | 2   | 3   | 0   |
    | 0   | 4   | 5   | 6   | 0   |
    | 0   | 7   | 8   | 9   | 0   |
    | 0   | 0   | 0   | 0   | 0   |

    ### So in conclusion, its easier to use convolutions when the filters are not symmetric. If the filters are symmetric, then both types of operations have the same result. As such, we always do convolutions by default.
    """
)
