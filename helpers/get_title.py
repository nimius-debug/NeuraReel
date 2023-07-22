from googleapiclient.discovery import build
import streamlit as st

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def get_video_title(video_id):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=st.secrets["DEVELOPER_KEY"])

    request = youtube.videos().list(
        part="snippet",
        id=video_id
    )
    response = request.execute()

    return response['items'][0]['snippet']['title']

