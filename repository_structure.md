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

## 1_models/

- `embeding/`
  - `1_openai_query.py`
  - `2_openai_docs.py`
  - `3_hf.py`
  - `project/`
    - `v1.py`
    - `v2.py`
- `language/`
  - `chat/`
    - `1_open_ai.py`
    - `2_anthropic.py`
    - `3_google.py`
    - `4_hf.py`
    - `5_hf_offline.py`
  - `llm/`
    - `llm.py`

## 2_prompts/

- `basic/`
  - `1_basic_prompt_hf.py`
  - `2_basic_prompt_openai.py`
  - `3_basic_prompt_streamlit.py`
- `chat/`
  - `ChatPromptTemplate.py`
  - `message_placeholder.py`
- `langchain/`
  - `4_lc_prompt.py`
  - `5_lc_dp.py`
  - `6_lc_chain_prompt.py`
  - `prompt_generator.py`
  - `__pycache__/`

## 3_outputs/

- `__pycache__/`
- `new_pydantic.py`
- `typed_dict.py`
- `with_structured_output_json.py`
- `with_structured_output_pydantic.py`
- `with_structured_output_typed_dict.py`

## 3_parsers/

- `conventional_str.py`
- `parser_json.py`
- `parser_pydantic.py`
- `parser_str.py`
- `parser_structured_output.py`

## 4_chains/

- `conditional.py`
- `parallel.py`
- `sequential.py`
- `simple.py`

## 5_runables/

- (empty directory)

## 6_loaders/

- `1_text_loader.py`
- `2_pdf_loader.py`
- `3_directory_loader.py`
- `4_web_based_loader.py`
- `5_csv_loader.py`
- `notes/`
  - `1652519762002_PythonNotesForProfessionals.pdf`
  - `GitNotesForProfessionals.pdf`

## 7_splitters/

- `1_length_based_text.py`
- `2_length_based_docs.py`
- `3_recursive_character_text_splitter.py`
- `4_recursive_character_text_splitter_language.py`
- `5_recursive_character_text_splitter_markdown.py`
- `6_semantic_splitter.py`
- `online_splitter.txt`
