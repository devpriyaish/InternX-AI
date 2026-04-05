from typing import Literal
from pydantic import BaseModel, Field

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-4o")

class Review(BaseModel):
  summary: str = Field(description="Summary of the review in not more than 15 words")
  sentiment: Literal["Pos", "Neg", "Ntrl"] = Field(description="Return the sentiment of the review as positive, negative or neutral")

structured_model = cm.with_structured_output(Review)

result =structured_model.invoke("This smartphone provides a basic experience that may be suitable for users with minimal performance expectations. The design is simple and functional, though it does not particularly stand out in terms of build quality or premium feel.")

print(result.summary)
print(result.sentiment)


















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