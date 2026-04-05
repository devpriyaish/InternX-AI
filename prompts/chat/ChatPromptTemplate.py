from langchain_core.prompts import ChatPromptTemplate

chat_template = ChatPromptTemplate([
  ('system', "You are a helpful {domain} expert"),
  ('human', "Explain in a line, what is {topic}")
  # SystemMessage(content="You are a helpful {domain} expert"),
  # HumanMessage(content="Explain in a line, what is {topic}")
])

prompt = chat_template.invoke({"domain": "Litrature", "topic": "ChatGPT"})

print(prompt)


"""
messages=[
  SystemMessage(content='You are a helpful {domain} expert', additional_kwargs={}, response_metadata={}), 
  HumanMessage(content='Explain in a line, what is {topic}', additional_kwargs={}, response_metadata={})
]

messages=[
  SystemMessage(content='You are a helpful Litrature expert', additional_kwargs={}, response_metadata={}), 
  HumanMessage(content='Explain in a line, what is ChatGPT', additional_kwargs={}, response_metadata={})
]
"""