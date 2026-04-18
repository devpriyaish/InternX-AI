from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

# chat template
chat_template = ChatPromptTemplate([
  ('system', "You are a helpful {domain} expert"),
  MessagesPlaceholder(variable_name="chat_history"),
  ('human', "Explain in a line, {query}"),
])

# load chat history
chat_history = []
with open("chat_history.txt", "r") as f:
  chat_history.extend(f.readlines())

print(chat_history)

# create prompt
prompt = chat_template.invoke({"domain": "Customer Support", "chat_history": chat_history, "query": "When will I get my refund"})

print(prompt)






"""
messages=[
  SystemMessage(content='You are a helpful Customer Support expert', additional_kwargs={}, response_metadata={}), 
  HumanMessage(content="HumanMessage(content='I want refund for product 'RF001D'', additional_kwargs={}, response_metadata={})\n", additional_kwargs={}, response_metadata={}), 
  HumanMessage(content="AIMessage(content='You will get your refund within 48 hours.', additional_kwargs={}, response_metadata={}), ", additional_kwargs={}, response_metadata={}), 
  HumanMessage(content='Explain in a line, When will I get my refund', additional_kwargs={}, response_metadata={})
]
"""