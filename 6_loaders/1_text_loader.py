from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

parser = StrOutputParser()

prompt = PromptTemplate(
  template="You are a helpful assistant. You need to provide 4 line poem {wikipedia}",
  input_variables=["wikipedia"]
)

loader = TextLoader("data.txt", encoding="utf-8")

docs = loader.load()[0].page_content

chain = prompt | model | parser

result = chain.invoke({"wikipedia": docs})

print(result) 














"""
[
  Document(
    metadata={'source': 'data.txt'}, 
    page_content="The Delimitation Commission of India is a commission established by the Government of India under the provisions of the Delimitation Commission Act, tasked with redrawing the boundaries of legislative assembly and Lok Sabha constituencies based on the last census. The present delimitation of constituencies is based on the 2001 census under the provisions of the Delimitation Act, 2002.\n\nThe Commission is an independent body whose orders cannot be challenged in any court of law. The orders are laid before the Lok Sabha and the respective State Legislative Assemblies. However, modifications are not permitted. The next delimitation can not be held before 2026.\n\nHistory\nDelimitation commissions have been set up in India four times in the past — 1952, 1962, 1972 and 2002 — under Delimitation Commission Acts of 1952, 1962, 1972 and 2002.\n\nThe union government had suspended delimitation in 1976 until after the 2001 census so that states' family planning programs would not affect their political representation in the Lok Sabha. This had led to wide discrepancies in the size of constituencies, with the largest having over three million electors, and the smallest less than 50,000.[1]"
  )
]
"""















# chain = loader | prompt | model | parser
