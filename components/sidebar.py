import streamlit as st
def render_sidebar():
    with st.sidebar:
        st.write("## About")
        st.write("NeuraReels is a application designed to automate the \
            process of creating 30-second highlight videos from YouTube...")
        st.markdown("### How it works")
        st.markdown("The application downloads a video -> transcribes it ->\
            analyzes the transcript to find the most engaging parts ->\
            adds captions, edits the video, and adds background music.") 
