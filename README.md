# RFPGPT

Welcome to RFPGPT, a generative AI application that uses Retreival-Augmented Generation (RAG) and custom ingestion pipelines to respond to defense-related Request for Proposals.

100% private, built with small and powerful open-source LLMs, and very accurate. Built with [LangChain](https://github.com/hwchase17/langchain) and [Vicuna-7B](https://huggingface.co/TheBloke/vicuna-7B-1.1-HF) and [InstructorEmbeddings](https://instructor-embedding.github.io/)

This project was inspired by the original [privateGPT](https://github.com/imartinez/privateGPT).



# Environment Setup
In order to set your environment up to run the code here, first install all requirements:

```shell
pip install -r requirements.txt
```

## Instructions for ingesting your own dataset

Put any and all of your .txt, .pdf, or .csv files into the SOURCE_DOCUMENTS directory
in the load_documents() function, replace the docs_path with the absolute path of your source_documents directory. 

The current default file types are .txt, .pdf, .csv, and .xlsx, if you want to use any other file type, you will need to convert it to one of the default file types.


Run the following command to ingest all the data.

```shell
python ingest.py
```

It will create an index containing the local vectorstore. Will take time, depending on the size of your documents.
You can ingest as many documents as you want, and all will be accumulated in the local embeddings database. 
If you want to start from an empty database, delete the `index`.

Note: When you run this for the first time, it will download take time as it has to download the embedding model. In the subseqeunt runs, no data will leave your local enviroment and can be run without internet connection.
