"""Streamlit app runner"""
import streamlit as st

from boom_text_summarizer.models.text_summarizer import TextSummarizer

text_summarizer = TextSummarizer()


def main():
    # Display a title for the Streamlit app
    st.title("BART Text Summarization Demo")
    st.markdown("> Underlying model: sshleifer/distilbart-cnn-12-6")

    # Create an input text box for text to summarize
    input_text = st.text_area("Enter your text", "")

    # Create a button to trigger model inference
    if st.button("Summarize"):
        # Perform inference using the loaded model
        result = text_summarizer.summarize(input_text)
        st.write("**Summary**:\n", result)
        st.snow()


if __name__ == "__main__":
    main()
