from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

parser = StrOutputParser()

prompt1 = PromptTemplate(
  template="You are a helpful assistant. You need to provide detailed notes on {ppt}.",
  input_variables=["ppt"]
)
prompt2 = PromptTemplate(
  template="You are a helpful assistant. You need to provide 5 quiz on {ppt}.",
  input_variables=["ppt"]
)
prompt3 = PromptTemplate(
  template="Merge the quiz and notes to a single document. \n notes -> {notes} and quiz -> {quiz}",
  input_variables=["notes", "quiz"]
)
 
parallel_chain = RunnableParallel({
  "notes": prompt1 | model | parser,
  "quiz": prompt2 | model | parser
})
sequential_chain = prompt3 | model | parser
chain = parallel_chain | sequential_chain

ppt = """ Add your text here """

result = chain.invoke({"ppt": ppt})
print(result)
chain.get_graph().print_ascii()