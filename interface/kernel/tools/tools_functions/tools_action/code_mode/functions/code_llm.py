import ollama
import re
from kernel.tools.tools_functions.tools_action.code_mode.CONFIG_TOOL import *


def code_llm_prompt(prompt, conversation_history):
    # Add current prompt to history
    conversation_history.append(f"User: {prompt}")

    # Limit history size
    if len(conversation_history) > CODE_LLM_MAX_HISTORY_LENGTH:
        conversation_history.pop(0)

    # Create the complete prompt including the history
    full_prompt = "\n".join(conversation_history)

    # Choose the LLM Server API you want:
    """ Local Ollama (on your computer) """
    client = ollama.Client()  

    """ API Ollama (on server) """
    # client = ollama.Client(host="http://172.17.0.1:11434/")

    response = client.generate(
        model=CODE_LLM,  # Local Model
        # model=CODE_LLM,  # Online API Model
        prompt=full_prompt
    )
    response_text = response['response']

    # Extract code blocks from the response
    code_blocks = re.findall(r'```(.*?)```', response_text, re.DOTALL)
    code_response = "\n".join(code_blocks)
    
    # Add only the generated code to history
    conversation_history.append(f"Assistant: ```{code_response}```")
    
    return code_response