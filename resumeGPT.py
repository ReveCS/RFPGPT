import os
# import langchain
# import pypdf
from langchain.document_loaders import PyPDFLoader
# import fitz
from langchain.document_loaders import PyMuPDFLoader, JSONLoader
from langchain.docstore.document import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.llms import HuggingFaceHub
import json
import jsonschema
from langchain.document_loaders import JSONLoader
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings


from pathlib import Path
from pprint import pprint

from langchain.llms import LlamaCpp
from huggingface_hub import hf_hub_download
from transformers import (
    AutoModelForCausalLM,
    LlamaForCausalLM
)
from bardapi import Bard


# import llama_cpp
# import openai
# Load the PDF file
loader = PyMuPDFLoader("C:/nai_localgpt/localGPT/Resume CS.pdf")
pdfData = loader.load()

# loader = PyPDFLoader("C:/Users/InvisiHands/AI/resumeGPT/Resume CS.pdf")
# pages = loader.load_and_split()
#  open(pdf_path, "rb") as f:
#   pdf = pypdf.PdfFileReader(f)

def read_json(file_path):
    with open(file_path, "r") as f:
        json_object = json.load(f)
        json_string = json.dumps(json_object)
    return json_string


def validate_json_with_schema(json_data, schema):
    validator = jsonschema.Draft7Validator(schema)

    try:
        validator.validate(json_data)
    except jsonschema.ValidationError as e:
        raise ValueError(e)
    return json_data


json_path = "C:/nai_localgpt/localGPT/Resume.json"

# documents = []
# with open(json_path, "r") as f:
#     json_object = json.load(f)
#     for i in json_object.items():
#         json_string = json.dumps(i)
#         document = Document(page_content=json_string)
#         documents.append(document)
# pprint(documents)
# print("This is documents")


# schema = read_json(json_schema_path)
resumeJson = read_json(json_path)
#print("This is resume json string")
#pprint(resumeJson)
jsonData = []
document = Document(page_content=resumeJson)
jsonData.append(document)
#print("This is document json")
#pprint(docs)


# Load the resume
# loader = PyMuPDFLoader("C:/Users/InvisiHands/AI/resumeGPT/Resume CS.pdf")
# data = loader.load()
# loader = JSONLoader(
#     file_path='./example_data/facebook_chat.json',
#     jq_schema='.messages[].content')
# data = loader.load()
# pprint(data)

# Split the text
text_splitter = RecursiveCharacterTextSplitter(chunk_size=5000, chunk_overlap=50)
texts = text_splitter.split_documents(pdfData)
for text in texts:
    print(text)

# Create an embedding model
# embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-large")
# embeddings = HuggingFaceEmbeddings(model_name="AutoModelForQuestionAnswering")
model_name = "sentence-transformers/all-mpnet-base-v2"
model_kwargs = {'device': 'cpu'}
encode_kwargs = {'normalize_embeddings': False}
embeddings = HuggingFaceEmbeddings(
    model_name=model_name,
    model_kwargs=model_kwargs,
    encode_kwargs=encode_kwargs
)

embedding_fn = OpenAIEmbeddings(openai_api_key="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")

# Create a vector database for the PDF
vectordb = Chroma.from_documents(texts, embedding=embedding_fn, persist_directory="C:/nai_localgpt/localGPT")
vectordb.persist()

# Get the LLM`  1`
# model_id = "TheBloke/vicuna-7B-1.1-HF"
# model_basename = None
# llm = LlamaForCausalLM.from_pretrained(model_id, low_cpu_mem_usage=True)
# cookie = 'ZAgsLu2VwiwE0LOtcMkN7as__mDAfhYTpYqlIk127gouTIXanCcyOB68E12xc2WYEBCwQw.'
# bard = Bard(token=cookie)
# question = "Explain Trinity"
# answer = bard.get_answer(question)
# print(answer)


# Set the HuggingFace API token.
# os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"

# Initialize the HuggingFaceHub LLM.
hf = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.8, "max_length": 16192})
# hf = HuggingFaceHub(repo_id="togethercomputer/LLaMA-2-7B-32K", model_kwargs={"temperature": 0.8, "max_length": 2014})
# hf = HuggingFaceHub(repo_id="stabilityai/StableBeluga2", model_kwargs={"temperature": 0.8, "max_length": 2014})
# hf = HuggingFaceHub(repo_id="TheBloke/Llama-2-13B-chat-GGML", model_kwargs={"temperature": 0.8, "max_length": 2014})
# hf = HuggingFaceHub(repo_id="NousResearch/Nous-Hermes-Llama2-13b", model_kwargs={"temperature": 0.8, "max_length": 2014})
# hf = HuggingFaceHub(repo_id="EleutherAI/gpt-neox-20b", model_kwargs={"temperature": 0.8, "max_length": 2014})
# hf = HuggingFaceHub(repo_id="meta-llama/Llama-2-7b", model_kwargs={"temperature": 0.8, "max_length": 2014})

# Nous-Hermes-Llama2-13b
# Generate some text.
# generated_text = hf.generate(["Explain Trinity"])

# Print the generated text.
# print(generated_text)
# model_path = hf_hub_download(repo_id=model_id, filename=model_basename)
# llm = LlamaCpp(
#    model_path=model_path,
#    n_ctx=2048,
#    max_tokens=2048,
#    temperature=0,
#    repeat_penalty=1.15,
#    n_gpu_layers=1000,
# )

# Create a memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

llm = OpenAI(openai_api_key="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")

# Create a question and answer chatbot
qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectordb.as_retriever(search_kwargs={"k": 1}))

# chatbot = ConversationalRetrievalChain.from_llm(
#     llm=hf, retriever=vectordb.as_retriever(), memory=memory,
# )

# Start the chatbot
while True:
    question = input("Enter your question: ")
    response = qa(question)
    print(response)