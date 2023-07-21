
# 30-sec Video Automation

This is a Python-based application designed to automate the process of creating 30-second highlight videos from YouTube. The application downloads a video, transcribes it, analyzes the transcript to find the most engaging parts, adds captions, edits the video, and adds background music. This application uses Streamlit for the user interface and Python for the backend.

## Workflow

1. **Download a video from YouTube**: Using the `pytube` library.
2. **Transcribe the video with OpenAI Whisper ASR**: Extract the audio from the video file using the `moviepy` library, then transcribe it using OpenAI's Whisper ASR.
3. **Analyze the transcriptions to find the most engaging parts**: Use natural language processing (NLP) libraries like `transformers` from Hugging Face, possibly fine-tuned with your own data.
4. **Add captions to the video**: Once the most engaging parts of the video are identified, add captions to the video using `moviepy`.
5. **Edit the video and add background music**: Perform basic video editing tasks and attach an audio file to the video clip using `moviepy`.
6. **Export the video**: Finally, export your edited video using `moviepy`.

## Dependencies

1. Python
2. Libraries: `pytube`, `moviepy`, `transformers` (Hugging Face), `streamlit`

## How to Run

To run this application:

1. Clone this repository to your local machine.
2. Navigate to the repository directory in your terminal.
3. Install the required dependencies with `pip install -r requirements.txt`.
4. Run the Streamlit app with `streamlit run app.py`.

## Limitations

As of the last update in 2021, YouTube's Terms of Service generally prohibit downloading videos. Make sure to respect copyright and usage agreements when developing applications. OpenAI also has usage policies which you should familiarize yourself with. 

## Future Development

Further enhancement of the app can involve more sophisticated NLP analysis and more complex video editing features. Python is a powerful language with an extensive ecosystem of libraries, and new tools and features can always be incorporated into this project.

## Contributions

Contributions are always welcome! Feel free to open a pull request or branch out from this project.

## License

(Mention the type of license used for your project)

## Contact

(Provide contact information)

Always keep up with the latest official documentation of the APIs and libraries used for the most accurate and up-to-date methods.
