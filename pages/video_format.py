import io
import tempfile
from pytube import YouTube
from youtube_transcript_api import YouTubeTranscriptApi
from moviepy.editor import VideoFileClip, TextClip, CompositeVideoClip
import streamlit as st

def download_and_transcribe(video_url):
    # Download the video from YouTube
    yt = YouTube(video_url)
    stream = yt.streams.first()

    # Download the video to a temporary file
    temp_video_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    stream.download(filename=temp_video_file.name)

    # Get the video id from the url
    video_id = video_url.split('=')[-1]

    # Get the transcription of the video
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Convert the transcript into one long string
    transcript_text = " ".join([i['text'] for i in transcript_list if i['start'] < 30])

    # Load your video from the temporary file
    video = VideoFileClip(temp_video_file.name)

    # Clip the video to the first 30 seconds
    video = video.subclip(0, 30)

    # Create a TextClip for your transcription
    transcription = TextClip(transcript_text, fontsize=24, color='white')

    # Place the transcription in the center of the video
    transcription = transcription.set_pos('center').set_duration(30)

    # Overlay the text clip on your video
    video = CompositeVideoClip([video, transcription])

    # Write the result to another temporary file
    temp_result_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp4')
    video.write_videofile(temp_result_file.name, codec='libx264')

    # Display the video with streamlit
    st.video(temp_result_file.name)
    result_video = open(temp_result_file.name, "rb")
    st.download_button(label="Download video file", data=result_video, file_name='video_clip.mp4')

# Provide the URL of the YouTube video
video_url = st.text_input("Enter a YouTube video URL")
if st.button("Generate video") and video_url:
    download_and_transcribe(video_url)
    st.success("Video generated successfully!")
