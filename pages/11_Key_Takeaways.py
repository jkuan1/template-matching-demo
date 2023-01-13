import streamlit as st

st.markdown("""
# Key Takeaways for template matching:
## Pros:
### - Very little needed training data
### - Very easy to set up
### - Relatively fast
### - Can be very robust in niche scenarios:
##### - Satellite imaging
##### - Fingerprint matching
##### - Iris scans   
# 
## Cons:
### - Not great in broader, less controlled, more general scenarios
### - Testing hard to do automatically (boundaries are hard to define)
### - Performance does not scale well with resolution
# 
# Where it can be improved:
### - Don't use normalized cross-correlation because it is not robust in respect to orientation, scale, and illumination changes. 
### - What if I:
#### - Used binary images?
#### - Use rotated templates?
#### - Use colour channels but lower the contrast?
#### - What should we alter and change and when should we just use a new procedure?
# 
## Lessons learned
### - You don't need a lot of data to create a machine learning model
### - This is just one method out of many - and can be combined / altered to be better""")
