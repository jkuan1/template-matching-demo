import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
from utils import MakeGaussianPyramid, ShowGaussianPyramid, FindTemplate
from scipy import ndimage


# org_template = Image.open("./pictures/template.jpeg")
org_template = Image.open("./pictures/tm_justin_2.jpg").convert("L")
tm_height, tm_width = org_template.size
org_template = org_template.resize((int(tm_height / 3), int(tm_width / 3)), resample=Image.BICUBIC)
st.image(org_template, width=300)
st.write(org_template.size)
template_test = Image.open(
    "./pictures/tm_group_pic_org3.jpg").convert("L")
st.image(template_test, width=800)
st.write(template_test.size)

gaussian_pyr = MakeGaussianPyramid(template_test, 0.90, 100)
st.image(ShowGaussianPyramid(gaussian_pyr))

threshold = st.slider("Match threshold", 0.001, 1.000, 1.000)


def find_template():
    st.write(threshold)
    ans, _ = FindTemplate(gaussian_pyr, org_template, threshold)
    return ans


st.image(find_template())
# test = Image.open("./pictures/template2.png").convert("L")
# st.image(test)
# st.write(test.size)

"What if we used a lower res image for the template?"
nick_template = Image.open("./pictures/tm_nick3.png").convert("L")
st.image(nick_template, width=300)
st.write(nick_template.size)
nick_threshold = st.slider("Nick threshold", 0.01, 1.00, 0.75)
nick_ans, _ = FindTemplate(gaussian_pyr, nick_template, nick_threshold)
st.image(nick_ans)

"What if we used that other guy again?"
judy_template = Image.open("./pictures/judy_template.jpg").convert("L")
st.image(judy_template, width=300)
st.write(judy_template.size)
judy_threshold = st.slider("Judy threshold", 0.01, 1.00, 1.00)
judy_ans, _ = FindTemplate(gaussian_pyr, judy_template, judy_threshold)
st.image(judy_ans)

