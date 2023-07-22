import streamlit as st
from pytube import YouTube
import tempfile

def main():
    path = st.text_input('Enter URL of any youtube video')
    option = st.selectbox(
     'Select type of download',
     ('audio', 'highest_resolution', 'lowest_resolution'))
    
    if st.button("download"): 
        video_object =  YouTube(path)
        st.write("Title of Video: " + str(video_object.title))
        st.write("Number of Views: " + str(video_object.views))

        # Create a temporary file to download video
        temp_file = tempfile.NamedTemporaryFile(delete=False)
        
        if option=='audio':
            video_object.streams.get_audio_only().download(filename=temp_file.name)    
        elif option=='highest_resolution':
            video_object.streams.get_highest_resolution().download(filename=temp_file.name)
        elif option=='lowest_resolution':
            video_object.streams.get_lowest_resolution().download(filename=temp_file.name)

        # Provide a download link for the downloaded video
        st.markdown(get_binary_file_downloader_html(temp_file.name, 'Download video file'), unsafe_allow_html=True)

    if st.button("view"): 
        st.video(path) 

def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{file_label}">Download {file_label}</a>'
    return href

if __name__ == '__main__':
    main()