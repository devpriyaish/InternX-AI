from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

cm = ChatGoogleGenerativeAI(model="chat-bison-001")

result = cm.invoke("Where is the Eiffel Tower?")

print(result)