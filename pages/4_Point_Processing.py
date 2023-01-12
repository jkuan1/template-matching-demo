import streamlit as st
from utils import show_code
from PIL import Image
import numpy as np
import math

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
                      ("None (Original)", "Invert", "Lower Contrast", "Increase Contrast", "Constant Darken", "Constant Lighten", "Sinusoidal Pattern"))


image_width = 600
image_transform = None

match option:
    case "None (Original)":
        st.write("Forumla: I'(X,Y) = I(X,Y)")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")
            return roxy

        image_transform = get_image

    case "Invert":
        st.write("Forumla: I'(X,Y) = 255 - I(X,Y)")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            # Turn image into numpy array (easier to do math operations)
            roxy_matrix = np.asarray(roxy, np.float32)
            roxy_inverted = 255 - roxy_matrix  # Invert operation

            # Turn matrix back into image
            roxy_inverted = roxy_inverted.astype('uint8')

            return roxy_inverted

        image_transform = get_image

    case "Lower Contrast":
        st.write("Forumla: I'(X,Y) = I(X,Y) * 0.5")
        st.write("Note: It can be any value! Not just 0.5!")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            roxy_matrix = np.asarray(roxy, np.float32)
            roxy_lower_contrast = roxy_matrix * 0.5  # contrast operation

            roxy_lower_contrast = np.clip(roxy_lower_contrast, 0, 255)
            roxy_lower_contrast = roxy_lower_contrast.astype('uint8')
            return roxy_lower_contrast

        image_transform = get_image

    case "Increase Contrast":
        st.write("Forumla: I'(X,Y) = I(X,Y) * 1.5")
        st.write("Note: It can be any value! Not just 1.5!")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            roxy_matrix = np.asarray(roxy, np.float32)
            roxy_increase_contrast = roxy_matrix * 1.5  # contrast operation

            roxy_increase_contrast = np.clip(roxy_increase_contrast, 0, 255)
            roxy_increase_contrast = roxy_increase_contrast.astype('uint8')
            return roxy_increase_contrast

        image_transform = get_image

    case "Constant Darken":
        st.write("Forumla: I'(X,Y) = I(X,Y) - 100")
        st.write("Note: It can be any value! Not just 100!")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            roxy_matrix = np.asarray(roxy, np.float32)
            roxy_darken = roxy_matrix - 100

            roxy_darken = np.clip(roxy_darken, 0, 255)
            roxy_darken = roxy_darken.astype('uint8')
            return roxy_darken

        image_transform = get_image

    case "Constant Lighten":
        st.write("Forumla: I'(X,Y) = I(X,Y) + 100")
        st.write("Note: It can be any value! Not just 100!")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            roxy_matrix = np.asarray(roxy, np.float32)
            roxy_lighten = roxy_matrix + 100

            roxy_lighten = np.clip(roxy_lighten, 0, 255)
            roxy_lighten = roxy_lighten.astype('uint8')
            return roxy_lighten

        image_transform = get_image

    case "Sinusoidal Pattern":
        st.write("Forumla: I'(X,Y) = (sin(X * 0.01) + 1) / 2 * I(X,Y)")

        def get_image():
            roxy = Image.open("./pictures/roxy.jpg")

            roxy_matrix = np.asarray(roxy, np.float32)
            sine_vector = (np.sin(
                [0.01 * x for x in range(0, roxy_matrix.shape[1])]) + 1) / 2
            roxy_sine = np.zeros(roxy_matrix.shape)

            for x in range(0, roxy_matrix.shape[1]):
                roxy_sine[:, x, :] = roxy_matrix[:, x, :] * sine_vector[x]

            roxy_sine = np.clip(roxy_sine, 0, 255)
            roxy_sine = roxy_sine.astype('uint8')
            return roxy_sine

        image_transform = get_image


st.image(image_transform(), width=image_width)
show_code(image_transform)
