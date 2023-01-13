import streamlit as st

st.set_page_config(page_title="What is Computer Vision?", page_icon="❓")

st.markdown(
    """
        # What is Computer Vision ❓
        
        #### Generally speaking, its the field of research aimed at enabling computers to process and interpret visual data, as sighted humans do*

        """
)

st.image("./pictures/pareidolia.jpg", width = 600)
st.image("./pictures/checkered-board-question.jpg", width = 600)
st.image("./pictures/checkered-board-answer.jpg", width = 600)
st.markdown("#### Wait... what exactly is visual data?")

# st.markdown(
#     """
#     ## Well, how well have we done?

#     #### It has been over 50 years... and there are a few things that we have learned along the way

#     ## Computer Vision _can_ be better than human vision
#     Examples:

#         1. Checker board (humans base interpretations off past experiences - can be good or bad)
#         2. Finding specfic instances in visual clutter
#         3. Calculating quantitative values in calibrated environments (e.g. biometrics)
       
#     """
# )



# st.markdown(
#     """
#     ## But Computer Vision is usually worse than Human Vision. Problems include:

    
#     ### 1. Measurement of properties of the 3D world from visual data
#     ##### Image capture is 3D to 2D... impossible to invert the image formation process.

#     ### 2. Algorithms used for image recognition is generally very computationally intensive and expensive. 

#     ### 3. We ourselves do not yet fully understand the processing mechanisms involved in image interpretation.

#     ### 4. Creative, ethical, moral questions
#     """
# )

# """
# Speaker Notes:

# Marvin Minsk (MIT)  - first instance of computer vision -> in 1966 spent a summer hooking a camera up to a computer and trying to get the computer to describe what it saw

# """
