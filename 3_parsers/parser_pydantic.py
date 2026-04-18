from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

class Person(BaseModel):
  name: str = Field(description="The name of the person")
  age: int = Field(description="The age of the person")
  country: str = Field(description="The country of the person")

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
  template="You are a helpful assistant. You need to create a single dummy identity \n {format_instruction}.",
  input_variables=[],
  partial_variables={"format_instruction": parser.get_format_instructions()},
)

chain = template | llm | parser

result = chain.invoke({})

print(result)