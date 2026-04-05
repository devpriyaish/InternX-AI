from langchain_huggingface import HuggingFaceEmbeddings

em = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

user_docs = [
  "Climate change is mainly caused by greenhouse gases released from burning fossil fuels and industrial activities.",   # 0.78
  "The effects of climate change include rising global temperatures, melting glaciers, and increasing sea levels.",      # 0.95
  "Climate change leads to extreme weather events such as heatwaves, floods, droughts, and stronger storms.",            # 0.94
  "Climate change disrupts ecosystems, damages agriculture, and increases risks to human health worldwide.",             # 0.92
  "Using renewable energy, planting trees, and reducing emissions are key solutions to slow climate change.",            # 0.70
  "Climate change causes rising temperatures, melting ice caps, and sea level rise, impacting life globally.",           # 0.96
  "Global warming results in extreme weather like droughts, floods, and heatwaves, which are major climate impacts.",    # 0.93
  "Reducing carbon emissions through clean energy and sustainability can help control climate change effects."           # 0.72
]

user_query = "What are the effects of climate change?"


user_docs_embeding = em.embed_documents(user_docs)
user_query_embeding = em.embed_query(user_query)

# cosine similarity

from sklearn.metrics.pairwise import cosine_similarity

scores = cosine_similarity([user_query_embeding], user_docs_embeding)[0]
print(list(enumerate(scores)))
index, score = sorted(list(enumerate(scores)),key=lambda x:x[1])[-1]

# max_score, idx = 0, 0     # 0.868, 1
# for index, score in list(enumerate(scores)):
#   if score > max_score:
#     max_score = score
#     idx = index

print("---------START----------------")
print("Question: ", user_query)
print("LLM Result: ", user_docs[index])
print("Confidance: ", score)
print("-----------END---------------")