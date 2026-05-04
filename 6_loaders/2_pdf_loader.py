from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("GitNotesForProfessionals.pdf")

docs = loader.load()[0].page_content

print(len(docs))
