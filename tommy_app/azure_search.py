import os
from typing import Any

from langchain_openai import AzureOpenAIEmbeddings
from langchain_community.vectorstores import AzureSearch
from azure.search.documents.indexes import SearchIndexClient
from azure.core.credentials import AzureKeyCredential

import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# os.environ["AZURE_OPENAI_ENDPOINT"]= config.get("Azure_LLM", "OPENAI_ENDPOINT")
# os.environ["AZURE_OPENAI_API_KEY"]= config.get("Azure_LLM", "OPENAI_API_KEY")


class Azure_Search:
    def __init__(self,):
        self.embedding_model = AzureOpenAIEmbeddings(
            endpoint=config.get("Azure_Embedding", "ENDPOINT"),
            api_key=config.get("Azure_Embedding", "API_KEY"),
            deployment_name=config.get("Azure_Embedding", "DEPLOYMENT_NAME"), 
            api_version=config.get("Azure_Embedding", "API_VERSION"), 
            temperature=0)
        
        
    def get_embedding(self,):
        return self.embedding_model.embed_query


    def get_vector_store(self,):
        try:
            vector_store: AzureSearch = AzureSearch(
                azure_search_endpoint=config.get("Azure_Embedding", "ENDPOINT"),
                azure_search_key=config.get("Azure_Embedding", "KEY"),
                index_name=index_name,
                embedding_function=self.get_embedding(),
            )

            index_client: SearchIndexClient = SearchIndexClient(
                endpoint=search_secrets["endpoint"],
                credential=AzureKeyCredential(search_secrets["admin_key"]),
                user_agent="langchain",
        )

            return vector_store
        
    def retriever(self,)
        retriever = AzureCognitiveServices








def _get_table_info(vector_store, encoding, query, max_number_of_tables: int = DEFAULT_PROMPT_LIMIT_MAX_NUMBER_OF_TABLES,
                       token_threshold: int = DEFAULT_PROMPT_LIMIT_TOKEN_THRESHOLD,)-> str:


    retrieved_docs = vector_store.similarity_search(
        query, k=max_number_of_tables, search_type="similarity")

    docs = get_docs_below_token_threshold(encoding, retrieved_docs, token_threshold)
    formatted_docs = format_docs(docs)
    return formatted_docs