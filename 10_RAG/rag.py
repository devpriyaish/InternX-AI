from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import load_prompt
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter, Language
from dotenv import load_dotenv

load_dotenv()


## INFORMATION RETRIEVAL 
# loader
loader = UnstructuredMarkdownLoader("10_RAG/doc.md")

docs = loader.load()

# splitters
text_splitter = RecursiveCharacterTextSplitter.from_language(
  language=Language.MARKDOWN,
  chunk_size=500,
  chunk_overlap=0
)

text = docs[0].page_content

chunks = text_splitter.split_text(text)

# embeddings
em = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=32)

# vector store
vectorstore = FAISS.from_texts(
    texts=chunks,
    embedding=em
)

# retrivers
query = "Gorilla has a sharper canine, are they carnivores?"
results = vectorstore.similarity_search(query, k=3)


## PROMPT AUGMENTATION
# prompt
template = load_prompt("rag.json")

# augumented prompt
prompt = template.format(
  context="\n\n".join([r.page_content for r in results]),
  question=query
)


## TEXT GENERATION
# model
cm = ChatOpenAI(
    model="gpt-4.1-mini",
    temperature=0
)

# generation
response = cm.invoke(prompt)

# rag output
print("\n\n-----------------------------\n\n")
print(response.content)

