import os
from typing import Any

from langchain_openai import AzureChatOpenAI

from backend.langchain_custom.query import create_sql_rag_query_chain
from backend.question_generator import QuestionGenerator

import configparser
config = configparser.ConfigParser()
config.read('config.ini')
 

def get_chain():
    from backend.vectorization.service import get_vector_store # To avoid circular import
    encoding = get_encoding()
    llm = get_llm_langchain()
    vector_store = get_vector_store()
    chain = create_sql_rag_query_chain(
        llm, vector_store, encoding, "snowflake", user_role, k=k
    )
    return chain



