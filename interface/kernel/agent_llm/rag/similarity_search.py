import streamlit as st
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

from CONFIG import *
from kernel.agent_llm.llm.llm_embeddings import generate_embedding


# Function to find the most similar tool
def get_most_similar_tool(user_prompt, embeddings_data):
    # Generates the embedding for the user prompt and resizes it
    user_embedding = np.array(generate_embedding(user_prompt)).reshape(1, -1)

    # Keep tool_embeddings base value to keep info like ids on the dict
    tool_embeddings = embeddings_data
    
    # Conversion of embeddings to float32
    tool_embeddings = tool_embeddings['embeddings']
    tool_embeddings = np.array(tool_embeddings).astype(np.float32)

    # Calculation of cosine similarities between user embedding and tool embedding
    cosine_similarities = cosine_similarity(user_embedding, tool_embeddings)[0]

    # Find the maximum similarity index
    max_similarity_index = cosine_similarities.argmax()

    # [SAW SIMILARITY BETWEEN USER PROMPT & TOOLS DESCRIPTION]
    # st.warning(str(cosine_similarities))
    
    # Checks if maximum similarity exceeds a defined threshold
    if cosine_similarities[max_similarity_index] >= SIMILARITY:  # Similarity threshold
        # Returns the ID of the most similar tool
        return embeddings_data['ids'][max_similarity_index]

    # Returns None if no sufficient similarity is found
    return None