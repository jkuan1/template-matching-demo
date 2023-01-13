import streamlit as st
from PIL import Image
from utils import MakeGaussianPyramid, ShowGaussianPyramid, FindTemplate
import numpy as np
from scipy import ndimage

gpyr_image, template = None, None


st.set_page_config(
    page_title="DIY", page_icon="")


def resize_image(image, scale):
    new_image = image.resize(
        (image.shape[0] * scale, image.shape[1] * scale), resample=Image.BICUBIC)

    return new_image


template_file = st.file_uploader(
    "Choose a template (jpg, jpeg, png)", type=["png", "jpg", "jpeg"])

if template_file:
    template = Image.open(template_file).convert("L")
    width, height = template.size
    template_arr = np.asarray(template, np.float32)
    scale = st.slider("Did you want to resize the template?", 0.01, 1.00, 1.00)
    template = template.resize(
        (int(width * scale), int(height * scale)), Image.BICUBIC)

    st.image(template, width=200)
    st.write(template.size)

image_file = st.file_uploader(
    "Choose an image (jpg, jpeg, png)", type=["png", "jpg", "jpeg"])

if image_file:
    image = Image.open(image_file).convert("L")
    width, height = image.size
    image_scale = st.slider(
        "Did you want to resize the image?", 0.01, 1.00, 1.00)
    image = image.resize(
        (int(width * image_scale), int(height * image_scale)), Image.BICUBIC)
    st.image(image, width=600)
    st.write(image.size)

if image_file and template_file:
    scale = st.slider("Set pyramid scale", 0.10, 0.90, 0.7)
    min = st.slider("Set min dim", int(
        min(image.size) / 1000), min(image.size), int(min(image.size) / 4))
    gpyr_image = MakeGaussianPyramid(image, scale, min)
    st.image(ShowGaussianPyramid(gpyr_image))

    threshold = st.slider("What is the threshold", 0.00,
                          1.00, 0.70)

    ans = FindTemplate(gpyr_image, template, threshold)
    st.image(ans)
    st.write("DID YOU HAVE FUN")
