import streamlit as st
from src.helper import voice_input, llm_model_object, text_to_speech

def main():
    # Sidebar
    with st.sidebar:
        st.image("https://via.placeholder.com/150", caption="Your Logo Here")
        st.markdown("### Settings")
        st.radio("Select Input Mode", ["Voice", "Text"], index=0)
        st.markdown("---")
        st.write("👋 Welcome to the AI Assistant!")
        st.markdown(
            "This multilingual assistant can help you interact in various languages. "
            "Feel free to ask anything!"
        )

    # Header
    st.title("🌍 Multilingual AI Assistant")
    st.markdown("*Your smart AI companion for multilingual conversations!*")

    # Main Content
    st.markdown("### 🎙 Ask Me Anything")
    if st.button("Start Listening"):
        with st.spinner("Listening..."):
            # Simulate input and response
            text = voice_input()
            response = llm_model_object(text)
            text_to_speech(response)

            # Display Response
            st.success("Response received!")
            st.text_area("Assistant's Response:", value=response, height=300)

            # Display Audio
            try:
                with open("speech.mp3", "rb") as audio_file:
                    audio_bytes = audio_file.read()
                    st.audio(audio_bytes)

                    # Download Button
                    st.download_button(
                        label="📥 Download Speech",
                        data=audio_bytes,
                        file_name="speech.mp3",
                        mime="audio/mp3"
                    )
            except FileNotFoundError:
                st.error("Audio file not found. Please check the text-to-speech process.")

    # Footer
    st.markdown("---")
    st.markdown(
        """
        *Developed with ❤ by [Gladiators/1st year]*
        """
    )

if __name__ == "__main__":
    # Custom Page Configurations
    st.set_page_config(
        page_title="Multilingual AI Assistant",
        page_icon="🤖",  # Use actual emoji instead of Unicode surrogate pairs
        layout="wide",
        initial_sidebar_state="expanded"
    )
    main()
