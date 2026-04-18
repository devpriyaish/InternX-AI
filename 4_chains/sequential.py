from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, JsonOutputParser
from dotenv import load_dotenv

load_dotenv()

# model
model1 = ChatOpenAI(model="gpt-4o")
model2 = ChatOpenAI(model="gpt-5")

# parser
parser1 = StrOutputParser()
parser2 = JsonOutputParser()

# prompt
prompt1 = PromptTemplate(
  template="You are a helpful assistant. You need to provide detailed description on topic {topic}.",
  input_variables=["topic"]
)
prompt2 = PromptTemplate(
  template="You are a helpful assistant. Generate 3 lines summary on {text}. \n {format_instruction}",
  input_variables=["text"],
  partial_variables={"format_instruction": parser2.get_format_instructions()},
)

# chain
chain = prompt1 | model1 | parser1 | prompt2 | model2 | parser2

result = chain.invoke({"topic": "Rivers of the world", "number_of_lines": 5})

print(result)

chain.get_graph().print_ascii()