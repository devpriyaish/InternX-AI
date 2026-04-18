from langchain_openai import ChatOpenAI
from langchain_core.prompts import load_prompt
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-5")

st.header("AI Litrature Assistant")

topic = st.text_input("Enter topic")
number_of_lines = st.text_input("Enter number of lines")
style = st.text_input("Enter style")
language = st.text_input("Enter language")

template = load_prompt("sumit.json")

if st.button("Generate"):
  chain = template | cm

  result = chain.invoke({
    "style": style,
    "number_of_lines": number_of_lines,
    "topic": topic,
    "language": language
  })
  
  st.write(result.content)
