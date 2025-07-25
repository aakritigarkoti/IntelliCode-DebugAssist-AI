import streamlit as st
import google.generativeai as genai

# Gemini API key configure karo
genai.configure(api_key="yourapikey")
model = genai.GenerativeModel("gemini-pro")

st.title("Gemini AI Chat")

user_input = st.text_input("Ask something...")

if user_input:
    response = model.generate_content(user_input)
    st.write("💬 Gemini says:")
    st.success(response.text)
