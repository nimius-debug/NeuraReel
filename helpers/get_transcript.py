import streamlit as st
from youtube_transcript_api import YouTubeTranscriptApi
@st.cache_data()
def get_transcript(video_id, language):
    try:
        # Retrieve the available transcripts
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Iterate over all available transcripts
        for transcript in transcript_list:
            if transcript.language_code == language:
                # Fetch the transcript directly if it's in the desired language
                sentences = [chunk['text'] for chunk in transcript.fetch()]
                return sentences

            elif transcript.is_translatable:
                # Check if the desired language is present in the translation_languages
                translation_languages = [lang['language_code'] for lang in transcript.translation_languages]
                if language in translation_languages:
                    # Fetch the translated transcript
                    translated_transcript = transcript.translate(language)
                    translated_sentences = [chunk['text'] for chunk in translated_transcript.fetch()]
                    return translated_sentences

        # If no suitable transcript is found
        st.write("No transcript available in the specified language.")
        return None

    except Exception as e:
        st.write(f"An error occurred: {str(e)}")
        return None
