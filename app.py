import streamlit as st
from langchain.document_loaders import YoutubeLoader
from youtube_transcript_api import YouTubeTranscriptApi
from helpers.get_title import get_video_title

from helpers.categorize import categ_video



st.title("NeuraReels")
# # Must be a single transcript.
# url = st.text_input("## Enter a YouTube video URL")
# if st.button("Generate video") and url:
#     video_id = url.split('watch?v=')[-1]
#     transcript = YouTubeTranscriptApi.get_transcript(video_id)
#     st.write(transcript)
#     sentences = [chunk['text'] for chunk in transcript]
#     # transcript is already a list of strings (sentences)
#     plain_text_transcript = " ".join(sentences)  
#     st.markdown("---")
#     st.write(plain_text_transcript.capitalize())
#     title = get_video_title(video_id)
#     st.markdown("---")
#     st.write(title)
#     st.markdown("---")
#     categ_video(title, plain_text_transcript)
    




