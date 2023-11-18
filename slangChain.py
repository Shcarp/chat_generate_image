import logging
import os
import sys
from dotenv import load_dotenv
from langchain.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings

from langchain.chains.question_answering import load_qa_chain
from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chains import RetrievalQA
from langchain.chains import RetrievalQAWithSourcesChain

from langchain.chat_models import ChatOpenAI

load_dotenv()

API_KEY = os.getenv('API_KEY')

os.environ["OPENAI_API_KEY"] = API_KEY

loader = WebBaseLoader('https://stable-diffusion-art.com/prompt-guide/#Anatomy_of_a_good_prompt')

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1000,
    chunk_overlap  = 20,
)

data = loader.load()

texts = text_splitter.split_documents(data)

embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")

docsearch = Chroma.from_documents(texts, embeddings)

query = "Good tips include those"

docs = docsearch.similarity_search(query)

chatllm = ChatOpenAI(model_name='gpt-4', temperature=0.2)
# 1
# chain1 = load_qa_chain(chatllm, chain_type='stuff')
# res = chain1.run(input_documents=docs, question=query)
# print("1", res)
# 2
# chain2 = load_qa_with_sources_chain(chatllm, chain_type='stuff')
# res = chain2({"input_documents": docs, "question": query}, return_only_outputs=True)
# print("2", res)
# 3
chain3 = RetrievalQA.from_chain_type(llm=chatllm, chain_type='stuff', retriever=docsearch.as_retriever())
res = chain3.run(query)
print("3", res)
# 4
# chain4 = RetrievalQAWithSourcesChain.from_chain_type(llm=chatllm, chain_type='stuff', retriever=docsearch.as_retriever())
# res = chain4({"question": query}, return_only_outputs=True)
# print("4", res)