import streamlit as st #use streamlit for the UI
import os
from embedchain import App #need this for EmbedChain

# Create a bot instance
os.environ["OPENAI_API_KEY"] = "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" #Add in your OpenAI API key here
gibson_bot = App()

# # Embed online resources
gibson_bot.add("datasource/Profile.pdf", data_type="pdf_file");

question = st.text_input('Enter your question')

if st.button('Submit query'):
	wait_text = st.title("Please wait ...")
	print("Submitting query '" + question + "'")
	answer = gibson_bot.query(question)
	wait_text.empty()
	print(answer)
	st.title(answer)