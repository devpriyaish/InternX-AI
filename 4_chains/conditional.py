from typing import Literal
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser, PydanticOutputParser
from langchain_core.runnables import RunnableBranch, RunnableLambda
from dotenv import load_dotenv

load_dotenv()

class Review(BaseModel):
  sentiment: Literal["Pos", "Neg"] = Field(description="Return the sentiment of the review as positive or negative")

cm = ChatOpenAI(model="gpt-4o")

parser1 = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Review)

prompt1 = PromptTemplate(
  template="Classify the sentiments of the following feedback as positive or negative. \n {feedback}. \n {format_instruction}",
  input_variables=["feedback"],
  partial_variables={"format_instruction": parser2.get_format_instructions()},
)
prompt2 = PromptTemplate(
  template="Write an appropriate response for the following positive feedback. \n {feedback}.",
  input_variables=["feedback"]
)
prompt3 = PromptTemplate(
  template="Write an appropriate response for the following negative feedback. \n {feedback}.",
  input_variables=["feedback"]
)

classifier_chain = prompt1 | cm | parser2
branch_chain = RunnableBranch(
  (lambda x: x.sentiment == "Pos", prompt2 | cm | parser1),
  (lambda x: x.sentiment == "Neg", prompt3 | cm | parser1),
  RunnableLambda(lambda x: "Invalid sentiment")
)
chain = classifier_chain | branch_chain

result = chain.invoke({
  "feedback": """Thank you for your thoughtful feedback! We're glad to hear that the smartphone delivers a reliable and straightforward experience that suits users with basic needs. Its simple and functional design is intended to make everyday use easy and accessible, and we appreciate you recognizing that. Your input helps us continue improving while keeping usability at the core of our products."""
})

print(result)
chain.get_graph().print_ascii()