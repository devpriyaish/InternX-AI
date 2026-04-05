from langchain_huggingface import HuggingFaceEmbeddings

em = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

user_docs = [
  "Taj Mahal is in Agra, India.",                # 0.35
  "The Eiffel Tower is in Paris, France.",       # 0.99
  "The Colosseum is in Rome, Italy."             # 0.75
]

user_query = "Where is the Eiffel Tower?"

user_docs_embeding = em.embed_documents(user_docs)

user_query_embeding = em.embed_query(user_query)

# cosine similarity

from sklearn.metrics.pairwise import cosine_similarity

result = cosine_similarity([user_query_embeding], user_docs_embeding)

print(result)