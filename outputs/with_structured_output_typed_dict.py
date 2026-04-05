from typing import Literal, TypedDict, Annotated


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-4o")

class Review(TypedDict):
  summary: Annotated[str, "Summary of the review in not more than 15 words"]
  sentiment: Annotated[Literal["Pos", "Neg"], "Return the sentiment of the review as positive or negative"]

structured_model = cm.with_structured_output(Review)

result =structured_model.invoke("This phone is really excellent. The camera is outstanding — I compared it side by side with other phones around the ₹30,000 range, but this one clearly has a much better camera. The pictures are very clear with great quality, and the OIS works really well. It is visibly better than other brands. The display is also excellent. The colors are very vibrant and the screen is extremely smooth. Using the phone feels very enjoyable and smooth. The battery performance is also very good. One full charge easily lasts a full day even with heavy usage. Apps open very fast and the phone feels very smooth overall. Games like BGMI also run smoothly; I have played it without any issues. One small drawback is that it has a single speaker. However, it is not bad at all — the speaker is loud and the sound quality is good. Still, if it had stereo speakers, it would have been even better. I am giving this phone 4 stars only because of the single speaker. Overall phone is very good and Balanced around 25,000.")

print(result["summary"])
print(result["sentiment"])


















"""
Heating Stops after approximately 6months of usage, and service is worst,I registered complaint 3 times 
but no one comes to repair the product, and 3rd time they gave the service guy number, and he took the 
product since 3 months to repair 'saying parts are delayed', and at present 1 year completed since the 
date of purchase, still problem not resolved.
"""

"""
I recently purchased the Kent Sunstar 2000W Infrared Cooktop and after receiving product, the unit 
immediately displays an E6 error code and stops heating. I have followed the troubleshooting steps, but 
the error persists, indicating a faulty internal sensor. Disappointing performance from Kent

"""

"""
This door mat is really very good quality I bought it for my home entrance and it looks so nice and 
clean. It traps dust very nicely and dosent move much. The material feels strong and thick. I am happy 
with this purchse totally worth money
"""

"""
Totally does the opposite thing. The wools stats coming out from the first day use.Makes the whole house more dirty.
"""

"""
Stitching is terrible and threading. So costly for this product.
"""