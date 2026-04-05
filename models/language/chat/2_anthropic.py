from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv 

load_dotenv()

cm = ChatAnthropic(model="claude-2")

result = cm.invoke("Where is the Eiffel Tower?")

print(result)