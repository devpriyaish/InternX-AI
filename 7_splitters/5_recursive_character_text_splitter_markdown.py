from langchain_text_splitters import RecursiveCharacterTextSplitter, Language

text_splitter = RecursiveCharacterTextSplitter.from_language(
  language=Language.MARKDOWN,
  chunk_size=45,
  chunk_overlap=0
)

text = """
# InternX-AI Repository Structure

This file provides a complete Markdown representation of the `InternX-AI` repository contents.

## Root Directory

- `.env`
- `.example.env`
- `.git/`
- `.gitignore`
- `1_models/`
- `2_prompts/`
- `3_outputs/`
- `3_parsers/`
- `4_chains/`
- `5_runables/`
- `6_loaders/`
- `7_splitters/`
- `chat_history.txt`
- `data.txt`
- `exam.txt`
- `requirements.txt`
- `response.json`
- `sumit.json`
- `venv/`
"""

result = text_splitter.split_text(text)

print("---------------------------------")
print(len(result))
print(result)