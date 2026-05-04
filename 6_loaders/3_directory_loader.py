from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader = DirectoryLoader(
  path="6_loaders/notes",
  glob="*.pdf",
  loader_cls=PyPDFLoader
)

docs = loader.lazy_load()

for doc in docs:
  print(doc.metadata)