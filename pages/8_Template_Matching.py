import streamlit as st
from PIL import Image, ImageDraw
import numpy as np
from utils import MakeGaussianPyramid, ShowGaussianPyramid, FindTemplate
from scipy import ndimage

st.markdown("""
# Now lets apply everything we learned so far with some classic machine learning
#
### Let us consider the following problem: How do we create an algorithm that can detect faces?
#
### Well, maybe should re-look at an interesting property of correlations.
### In linear algebra, our correlation operation is mathematically equivalent of finding a dot product between two vectors
### The dot product can be used to find the angle between two vectors for any n-dimensions.
### In the context of computer vision, this means that the correlation operation can mathematically tell us how similar our filter is to our image.
""")

st.image("./pictures/template_matching.png")

st.markdown("""
# Welcome to a process called Template Matching!
### Basic idea - provide a generic face as a filter / template and create a correlation map between the filter and the image. Any intensity values above a certain threshold will be returned as a detected face.
### Some issues:
#### - Faces can be of different scales
#### - Faces can be in different orientations
#### - Images can have different lighting conditions
#### - There is a huge variety of faces
#### - Faces can be partially covered
#### - Faces can have different perspectives
#### - There may be motion / blur in the image

### What can we do to mitigate these issues?
#### - Why don't we provide the template face at different sizes and compare that?
#### - Why don't we turn everything into greyscale?
#### - We can finetune a good threshold to get an acceptable ratio of false positives and false negatives

# The template face:
""")
# org_template = Image.open("./pictures/template.jpeg")
org_template = Image.open("./pictures/tm_justin.png").convert("L")
st.image(org_template, width=300)
st.write(org_template.size)
template_test = Image.open(
    "./pictures/tm_group_pic_org3.jpg").convert("L")
# template_test = np.asarray(template_test)[::2, ::2]
st.image(template_test)
st.write(template_test.size)

gaussian_pyr = MakeGaussianPyramid(template_test, 0.80, 20)
st.image(ShowGaussianPyramid(gaussian_pyr))

threshold = st.slider("Match threshold", 0, 100, 67)


def find_template():
    thresh = float(threshold / 100)
    st.write(thresh)
    ans = FindTemplate(gaussian_pyr, org_template, thresh)
    return ans


st.image(find_template())
# test = Image.open("./pictures/template2.png").convert("L")
# st.image(test)
# st.write(test.size)

"What if we used a lower res image for the template?"
nick_template = Image.open("./pictures/tm_nick3.png").convert("L")
st.image(nick_template, width=300)
st.write(nick_template.size)
nick_threshold = st.slider("Nick threshold", 0, 100, 75)
nick_ans = FindTemplate(gaussian_pyr, nick_template,
                        float(nick_threshold / 100))
st.image(nick_ans)

"What if we used eyes and nose only?"
liam_threshold = st.slider("Liam threshold", 0, 100, 75)
liam_template = Image.open("./pictures/tm_liam_eyes.png").convert("L")
st.image(liam_template, width=300)
st.write(liam_template.size)
liam_ans = FindTemplate(gaussian_pyr, liam_template,
                        float(liam_threshold / 100))
st.image(liam_ans)
