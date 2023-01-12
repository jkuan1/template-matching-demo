import streamlit as st
from PIL import Image
from utils import MakeGaussianPyramid, ShowGaussianPyramid, FindTemplate

st.markdown("""
# Now lets apply everything we learned so far with some classic machine learning
#
### Let us consider the following problem: How do we create an algorithm that can detect certain objects?
#
### Well, maybe should re-look at an interesting property of correlations.
### In linear algebra, our correlation operation is mathematically equivalent of finding a dot product between two vectors
### The dot product can be used to find the angle between two vectors for any n-dimensions.
### In the context of computer vision, this means that the correlation operation can mathematically tell us how similar our filter is to our image.
""")

st.image("./pictures/template_matching.png")

st.markdown("""
# Welcome to a process called Template Matching!
### Basic idea - provide a generic object as a filter / template and create a correlation map between the filter and the image. Any intensity values above a certain threshold will be returned as a detected object.
### Some issues:
#### - objects can be of different scales
#### - objects can be in different orientations
#### - Images can have different lighting conditions
#### - There is a huge variety of objects
#### - objects can be partially covered
#### - objects can have different perspectives
#### - There may be motion / blur in the image

### What can we do to mitigate these issues?
#### - Why don't we provide the template object at different sizes and compare that?
#### - Why don't we turn everything into greyscale?
#### - We can finetune a good threshold to get an acceptable ratio of false positives and false negatives

# The template object:
""")

template = Image.open("./pictures/Taipei_101_layer2.jpg").convert("L")
st.image(template, width = 300)

image = Image.open("./pictures/Taipei_101.jpg").convert("L")
st.image(image)

gaussian_pyr = MakeGaussianPyramid(image, 0.90, 40)
st.image(ShowGaussianPyramid(gaussian_pyr))

ans, matches = FindTemplate(gaussian_pyr, template, 0.85)
st.image(ans, width = 500)