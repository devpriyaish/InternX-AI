from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-4o")

json_review = {
  "title": "Review",
  "type": "object",
  "properties": {
    "summary": {
      "type": "string",
      "description": "Summary of the review in not more than 15 words"
    },
    "sentiment": {
      "type": "string",
      "enum": ["Pos", "Neg", "Ntrl"],
      "description": "Return the sentiment of the review as positive, negative or neutral"
    }
  },
  "required": ["summary", "sentiment"]
}

structured_model = cm.with_structured_output(json_review)

result =structured_model.invoke("This smartphone provides a basic experience that may be suitable for users with minimal performance expectations. The design is simple and functional, though it does not particularly stand out in terms of build quality or premium feel.")

print(result['summary'])
print(result['sentiment'])
