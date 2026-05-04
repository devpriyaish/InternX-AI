from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
  separator="",
  chunk_size=15,
  chunk_overlap=5,
)

text = """The quick brown fox jumps over the lazy dog.Then the fox jumps over the lazy dog. There comes the tiger."""

result = text_splitter.split_text(text)

print(result)