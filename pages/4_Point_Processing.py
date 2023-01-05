import streamlit as st
from utils import show_code
from PIL import Image
import numpy as np

st.markdown(
    """
    # Matrix Manipulation but with Actual Math Notation Now

    ## As demonstrated just now, it is very easy to transform an image.
    ## There are two types of transformations we can do generally:

    """
)

st.image("./pictures/transformers_meme.jpg")

st.markdown(
    """
  # Point Processing

  ### We will not concern ourselves with warp transformations (usually involves changing the dimensions of any image)
  ### We will instead focus on filtering (changing the pixel values)
  ### Let us first consider... Point operations!

  ### These operations are pretty straightforward... the original value of a pixel is correlated to the new value in the output
  ### We can showcase some of these operations using an image of Roxy!
  """
)

option = st.selectbox("Type of Point Transformation",
                      ("None (Original)", "Invert", "Lower Contrast", "Increase Contrast"))

match option:
    case "None (Original)":
        st.write("Forumla: I'(X,Y) = I(X,Y)")

        def get_original_image():

            roxy = Image.open("./pictures/roxy.jpg")  # Get image
            return roxy

        show_code(get_original_image)
        st.image(get_original_image())

    case "Invert":
        st.write("Forumla: I'(X,Y) = 255 - I(X,Y)")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            # Turn image into numpy array (easier to do math operations)
            roxy_matrix = np.asarray(roxy, np.float32)
            roxy_inverted = 255 - roxy_matrix  # Invert operation

            # Make sure only valid pixel intensities are kept
            roxy_inverted = np.clip(roxy_inverted, 0, 255)

            # Turn matrix back into image
            roxy_inverted = roxy_inverted.astype('uint8')

            return roxy_inverted

        show_code(get_image)
        st.image(get_image())

    case "Lower Contrast":
        st.write("Forumla: I'(X,Y) = I(X,Y) * 0.5")
        st.write("Note: It can be any value! Not just 0.5!")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            roxy_matrix = np.asarray(roxy, np.float32)
            roxy_darkened = roxy_matrix * 0.5  # contrast operation

            roxy_darkened = np.clip(roxy_darkened, 0, 255)
            roxy_darkened = roxy_darkened.astype('uint8')
            return roxy_darkened

        show_code(get_image)
        st.image(get_image())

    case "Increase Contrast":
        st.write("Forumla: I'(X,Y) = I(X,Y) * 1.5")
        st.write("Note: It can be any value! Not just 1.5!")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            roxy_matrix = np.asarray(roxy, np.float32)
            roxy_lightened = roxy_matrix * 1.5  # contrast operation

            roxy_lightened = np.clip(roxy_lightened, 0, 255)
            roxy_lightened = roxy_lightened.astype('uint8')
            return roxy_lightened

        show_code(get_image)
        st.image(get_image())
