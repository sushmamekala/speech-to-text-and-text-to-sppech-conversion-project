# Converting text to speech using pyttsx3 library and frontend streamlit

import streamlit as st
import pyttsx3
import threading
import os
from time import sleep

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

# Function to change voice to male or female
def set_voice(gender):
    voices = engine.getProperty('voices')
    
    # Set voice based on gender choice
    if gender == "Male":
        engine.setProperty('voice', voices[0].id)  # Male voice (usually)
    elif gender == "Female":
        engine.setProperty('voice', voices[1].id)  # Female voice (usually)

# Function to generate and save speech to a file
def save_speech_to_file(text, gender, filename):
    set_voice(gender)
    engine.save_to_file(text, filename)
    engine.runAndWait()

# Streamlit frontend
def main():
    st.title("Text-to-Speech App created by Sushma Ramchander")
    #st.markdown("This is a simple text-to-speech app using pyttsx3 and Streamlit.")

    # Input field for text
    text_input = st.text_area("Enter the desired text to convert to speech:")

    # Voice selection dropdown
    voice_option = st.selectbox("Select Voice", ["Male", "Female"])

    # Button to trigger text-to-speech
    if st.button("Convert to Speech"):
        if text_input:
            # Define the audio filename
            audio_filename = "speech_output.wav"

            # Start the speech generation in a new thread to avoid blocking Streamlit's event loop
            threading.Thread(target=save_speech_to_file, args=(text_input, voice_option, audio_filename)).start()

            # Sleep to allow the file to be saved before trying to play it
            sleep(2)

            # Play the generated audio file in Streamlit
            if os.path.exists(audio_filename):
                st.audio(audio_filename, format="audio/wav")
                
        else:
            st.error("Please enter some text!")


if __name__ == "__main__":
    main()
    
# Footer
st.markdown("Developed using Streamlit and pyttsx3")
