import streamlit as st


def run():
    st.set_page_config(
        page_title="Computer Vision Demo",
        page_icon="👓"
    )

    st.markdown(
        """
        # A QUICK INTERACTIVE INTRODUCTION TO COMPUTER VISION 
        ## By Justin Kuan

        Disclaimer: This is an ungodly attempt to do justice to the vast field known as computer vision

        # General Purpose:
        - Test the waters - give us a conceptual foundation to build off of
       
    """
    )

    st.image("./pictures/stats-joke.jpeg")


if __name__ == "__main__":
    run()
