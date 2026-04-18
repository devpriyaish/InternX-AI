from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-5")

st.header("AI Litrature Assistant")

topic = st.text_input("Enter topic")
number_of_lines = st.text_input("Enter number of lines")
style = st.text_input("Enter style")
language = st.text_input("Enter language")

system_prompt = f"""
  You are a helpful litrature assistant. 
  You need to answer the questions in {style} form and in {number_of_lines} lines only about topic {topic}. 
  Response in only {language} language. Analyze your answer before printing it.
"""

if st.button("Generate"):
  result =cm.invoke(system_prompt)
  st.write(result.content)
