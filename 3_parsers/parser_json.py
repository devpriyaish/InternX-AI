from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

parser = JsonOutputParser()

template = PromptTemplate(
  template="You are a helpful assistant. You need to generate 5 country and capital values. One of the value must be 'Australia': 'Canberra'\n {format_instruction}.",
  input_variables=[],
  partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | llm | parser

result = chain.invoke({})

print(result)



"""
{
  "Beautiful": "Ugly",
  "Good": "Bad"
}
"""