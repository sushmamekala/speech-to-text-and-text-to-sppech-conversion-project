# Converting text to speech using GTTS library and frontend streamlit
import streamlit as st
from gtts import gTTS
import tempfile

# Streamlit app title
st.title("Text-to-Speech Converter")

# Input text from the user
text_input = st.text_area("Enter the desired text to convert to speech:")

# Language selection
language = st.selectbox("Select language:", ["en", "es", "fr", "de", "hi"])

# Button to generate speech
if st.button("Generate Speech"):
    if text_input.strip():
        try:
            # Generate speech
            tts = gTTS(text=text_input, lang=language, slow=False)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
                tts.save(temp_audio_file.name)
                temp_audio_file.seek(0)
                audio_bytes = temp_audio_file.read()
            
            # Play the audio file
            st.audio(audio_bytes, format="audio/mp3")

            # Option to download the audio file
            st.download_button(label="Download Audio", data=audio_bytes, file_name="output.mp3", mime="audio/mp3")
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter some text to convert to speech.")

# Footer
