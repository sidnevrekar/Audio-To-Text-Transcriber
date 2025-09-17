# app.py
from google import genai
import streamlit as st

# Initialize Gemini client
client = genai.Client()

st.title("MP3 Audio Summarizer with Gemini AI")

# Drag and drop file uploader
uploaded_file = st.file_uploader("Drag and drop an MP3 file", type=["mp3"])

if uploaded_file is not None:
    # Save the uploaded file temporarily
    with open("temp.mp3", "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success(f"Uploaded file: {uploaded_file.name}")

    # Show loading spinner while processing
    with st.spinner("Processing audio, please wait..."):
        # Upload file to Gemini API
        myfile = client.files.upload(file="temp.mp3")

        # Use Gemini to transcribe and summarize the audio
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                "Your task is to listen to the audio file. Keep in mind that this audio file is being used for a virtual spanish 3 class, while some contents of the file might be in english most contents of the file will be in spanish. make sure to accurately get all parts of the conversation. If there is background noise or a pause do not record it inside the transcript. Make sure to add accents. Make sure to transcribe everything; dont leave anything out.",
                myfile
            ]
        )

    # Show the AI summary
    st.subheader("Audio Summary:")
    st.write(response.text)
