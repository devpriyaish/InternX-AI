from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text_splitter = SemanticChunker(
    OpenAIEmbeddings(), breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=3
)

sample = """
Weather changes quickly, shifting between sunshine, rain, wind, and storms across different seasons.
It influences daily life, affecting travel, farming, clothing, and outdoor activities.
When it rains, Helen Keller starts to dance with joy in the falling drops.
The rhythm of nature fills the air, making every moment feel alive.
Helen Keller was a remarkable woman who overcame blindness and deafness to inspire millions.
She became a famous writer, speaker, and advocate for people with disabilities.

A black hole is a region in space where gravity is so strong that nothing can escape it.
It forms when a massive star collapses at the end of its life cycle.
Black holes can bend light and distort space and time around them.
Scientists study black holes to understand the mysteries of the universe.
"""

docs = text_splitter.create_documents([sample])
print(len(docs))
print(docs)