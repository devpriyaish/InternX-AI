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

review = """
  This phone is really excellent. The camera is outstanding — I compared it side by side with other phones around the ₹30,000 
  range, but this one clearly has a much better camera. The pictures are very clear with great quality, and the OIS works 
  really well. It is visibly better than other brands. The display is also excellent. The colors are very vibrant and the 
  screen is extremely smooth. Using the phone feels very enjoyable and smooth. The battery performance is also very good. One 
  full charge easily lasts a full day even with heavy usage. Apps open very fast and the phone feels very smooth overall. Games 
  like BGMI also run smoothly; I have played it without any issues. One small drawback is that it has a single speaker. However, 
  it is not bad at all — the speaker is loud and the sound quality is good. Still, if it had stereo speakers, it would have been 
  even better. I am giving this phone 4 stars only because of the single speaker. Overall phone is very good and Balanced around 
  25,000.
"""

result =structured_model.invoke(review)

print(result['summary'])
print(result['sentiment'])
