from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema
from dotenv import load_dotenv
load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

schema = {
  ResponseSchema(name="opposite", description="Good * Bad"),
  ResponseSchema(name="opposite", description="Beautiful * Ugly"),
}

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
  template="You are a helpful assistant. Provide me 5 opposite values \n {format_instruction}.",
  input_variables=[],
  partial_variables={"format_instruction": parser.get_format_instructions()},
)

prompt = template.invoke({})

result = llm.invoke(prompt)

print(result)