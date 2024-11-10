from agent_llm.rag.similarity_search import get_most_similar_tool
from agent_llm.llm.llm import llm_prompt


conversation_history = []

def analyze_tool_to_use(user_prompt, tools, tool_embeddings):
    global conversation_history
    if conversation_history != []:
        conversation_history = conversation_history
    else:
        conversation_history = []

    similar_tool = get_most_similar_tool(user_prompt, tool_embeddings)
    if similar_tool:
        conversation_history = []
        tool_function = tools[similar_tool]["function"]
        
        #------------ Adapt here and paste the code depending on tools downloaded --------
        # Set parameters based on selected tool
        if similar_tool == "other_function_tool_selected": 
            # For Example:
            # param = extract_info_prompt(user_prompt)
            pass
        elif similar_tool in ["search_ytb", "search_google", "search_wikipedia", "search_bing", "vocal_note"]:
            # For Example:
            # param = user_prompt
            pass
        else:
            param = None
        # --------------------------------------------------------------------------------
        
        # Call the tool function with the appropriate parameter
        if param is not None:
            response = tool_function(param)
        else:
            response = tool_function()
        
        return response
    else:
        # If no tool correspond, enter prompt in classic LLM to have discussion
        response = llm_prompt(user_prompt, conversation_history)
        return response