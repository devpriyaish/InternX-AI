from langchain_openai import OpenAI
# from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")
# llm = GoogleGenerativeAI(model='gemini-2.5-pro')

parser = StrOutputParser()

template1 = PromptTemplate(
  template="You are a helpful assistant. You need to answer the questions in {number_of_lines} lines on topic {topic}.",
  input_variables=["number_of_lines", "topic"]
)

template2 = PromptTemplate(
  template="You are a helpful assistant. You need to summerize the folling text in single line. {text}",
  input_variables=["text"]
)

chain = template1 | llm | parser | template2 | llm | parser

result = chain.invoke({"number_of_lines": 5, "topic": "How to kill a hen?"})

print(result)
