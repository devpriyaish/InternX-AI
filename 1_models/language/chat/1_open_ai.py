from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

cm = ChatOpenAI(model="gpt-4o")

result = cm.invoke("How to kill a hen?")

print(result.content)
 






















"""
gpt-4
content='The Eiffel Tower is located in Paris, France.' 
additional_kwargs={'refusal': None} 
response_metadata={'token_usage': {'completion_tokens': 12, 'prompt_tokens': 15, 'total_tokens': 27, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-4-0613', 'system_fingerprint': None, 'id': 'chatcmpl-CwUkN48kZGt62c0Sdy2TXkudUKzK0', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019ba86c-a362-7bf3-8025-6ca8e7c105cb-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 15, 'output_tokens': 12, 'total_tokens': 27, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
"""

"""
gpt-5
content='Paris, France—on the Champ de Mars in the 7th arrondissement, near the Seine. Address: 5 Avenue Anatole France, 75007 Paris. Coordinates: 48.8584° N, 2.2945° E.' 
additional_kwargs={'refusal': None} 
response_metadata={'token_usage': {'completion_tokens': 125, 'prompt_tokens': 12, 'total_tokens': 137, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 64, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-5-2025-08-07', 'system_fingerprint': None, 'id': 'chatcmpl-CwUm1qmhU0aykS8FaYZoxEAaI4wG2', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--019ba86e-3403-7f23-9ea9-a8de49088622-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 12, 'output_tokens': 125, 'total_tokens': 137, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 64}}
"""




content='The Eiffel Tower is located in Paris, France.' 
additional_kwargs={'refusal': None} 
response_metadata={'token_usage': {'completion_tokens': 12, 'prompt_tokens': 15, 'total_tokens': 27, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0}, 'prompt_tokens_details': {'audio_tokens': 0, 'cached_tokens': 0}}, 'model_provider': 'openai', 'model_name': 'gpt-3.5-turbo-0125', 'system_fingerprint': None, 'id': 'chatcmpl-DQuqWpZwfZ96ivsv7yOMtMUXVnLFN', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} 
id='lc_run--019d5891-6006-7600-b2ae-cc5fc319d9e9-0' 
tool_calls=[] 
invalid_tool_calls=[] 
usage_metadata={'input_tokens': 15, 'output_tokens': 12, 'total_tokens': 27, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}