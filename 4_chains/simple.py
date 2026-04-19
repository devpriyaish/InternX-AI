from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# model
model = ChatOpenAI(model="gpt-4o")

# parser
parser = StrOutputParser()

# prompt
prompt = PromptTemplate(
  template="You are a helpful assistant. You need to provide {number_of_lines} lines on topic {topic}.",
  input_variables=["number_of_lines", "topic"]
)

# chain
chain = prompt | model | parser

result = chain.invoke({"number_of_lines": 5, "topic": "Rivers of the world"})

print(result)

chain.get_graph().print_ascii()