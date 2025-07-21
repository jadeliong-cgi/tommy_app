import os
from typing import Any

from langchain_openai import AzureChatOpenAI


from backend.langchain_custom.query import create_sql_rag_query_chain
from backend.question_generator import QuestionGenerator

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# os.environ["AZURE_OPENAI_ENDPOINT"]= config.get("Azure_LLM", "OPENAI_ENDPOINT")
# os.environ["AZURE_OPENAI_API_KEY"]= config.get("Azure_LLM", "OPENAI_API_KEY")

class Azure_LLM:
    def __init__(self,):
        self.llm = AzureChatOpenAI(
            endpoint=config.get("Azure_LLM", "ENDPOINT"),
            api_key=config.get("Azure_LLM", "API_KEY"),
            deployment_name=config.get("Azure_LLM", "DEPLOYMENT_NAME"), 
            api_version=config.get("Azure_LLM", "API_VERSION"), 
            temperature=0)
    
    def llm(self,):
        return self.llm
    




def get_chain():
    from backend.vectorization.service import get_vector_store # To avoid circular import
    encoding = get_encoding()
    llm = get_llm_langchain()
    vector_store = get_vector_store()
    chain = create_sql_rag_query_chain(
        llm, vector_store, encoding, "snowflake", user_role, k=k
    )
    return chain


def get_llm_generated_questions():
    from backend.vectorization.service import get_vector_store # To avoid circular import
    
    llm = get_llm_langchain()
    user_role = st.session_state.connection_parameters["role"]
    question_generator = QuestionGenerator(
        llm, get_vector_store(), get_encoding(), user_role
    )
    llm_generated_questions = question_generator.generate_questions()
    return llm_generated_questions
