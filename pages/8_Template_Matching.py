import streamlit as st

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
