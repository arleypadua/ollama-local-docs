# Document Query API

This repository contains a Flask-based API for querying documents using a language model and storing document vectors. The API allows users to query a language model, upload documents, and update the document vector store.

## Features

- **Query Endpoint:** Allows querying a language model to get answers and source documents.
- **Upload Endpoint:** Supports uploading documents to be used as sources.
- **Store Update Endpoint:** Updates the document vector store with new documents.

## Endpoints

### Query

- **URL:** `/query`
- **Method:** `GET`
- **Description:** Accepts a query string and returns an answer along with source documents from the language model.

### Upload

- **URL:** `/upload`
- **Method:** `POST`
- **Description:** Allows users to upload documents. The uploaded documents are saved and can be used as sources for queries.

### Store Update

- **URL:** `/store/update`
- **Method:** `POST`
- **Description:** Updates the document vector store with new document chunks.

## Local setup

1. **Setup Ollama:**
    ```bash
    # install ollama
    brew install ollama

    # install the default model (llama3)
    # you can optionally use another model with the api 
    # by running the API with the environment variable "MODEL"
    ollama pull llama3
    ```

2. **Create environment (optional):**
    ```bash
    conda create -n ollama-private-files
    conda activate ollama-private-files
    conda install pip
    ```

3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the application:**
    ```bash
    python ./src/api.py
    ```

Refer to [requests.http](./requests.http) file to interact with the API.

## Credits

This project was forked from the [PromptEngineer48/Ollama](https://github.com/PromptEngineer48/Ollama) repository and has been significantly modified to meet specific needs. Kudos to the original author for the foundation.