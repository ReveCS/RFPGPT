# RFPGPT

This project was inspired by the original [privateGPT](https://github.com/imartinez/privateGPT). Most of the description here is inspired by the original privateGPT. 

For detailed overview of the project, Watch this [Youtube Video](https://youtu.be/MlyoObdIHyo). 

In this model, I have replaced the GPT4ALL model with Vicuna-7B model and we are using the InstructorEmbeddings instead of LlamaEmbeddings as used in the original privateGPT. Both Embeddings as well as LLM will run on GPU instead of CPU. It also has CPU support if you do not have a GPU (see below for instruction). 

Ask questions to your documents without an internet connection, using the power of LLMs. 100% private, no data leaves your execution environment at any point. You can ingest documents and ask questions without an internet connection!

Built with [LangChain](https://github.com/hwchase17/langchain) and [Vicuna-7B](https://huggingface.co/TheBloke/vicuna-7B-1.1-HF) and [InstructorEmbeddings](https://instructor-embedding.github.io/)


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



## Ask questions to your documents, locally!
In order to ask a question, run a command like:

```shell
python run_localGPT.py
```

And wait for the script to require your input. 

```shell
> Enter a query:
```

Hit enter. Wait while the LLM model consumes the prompt and prepares the answer. Once done, it will print the answer and the 4 sources it used as context from your documents; you can then ask another question without re-running the script, just wait for the prompt again. 

Note: When you run this for the first time, it will need internet connection to download the vicuna-7B model. After that you can turn off your internet connection, and the script inference would still work. No data gets out of your local environment.

Type `exit` to finish the script.

# Run it on CPU
By default, localGPT will use your GPU to run both the `ingest.py` and `run_localGPT.py` scripts. But if you do not have a GPU and want to run this on CPU, now you can do that (Warning: Its going to be slow!). You will need to use `--device_type cpu`flag with both scripts. 

For Ingestion run the following: 
```shell
python ingest.py --device_type cpu
```
In order to ask a question, run a command like:

```shell
python run_localGPT.py --device_type cpu
```
