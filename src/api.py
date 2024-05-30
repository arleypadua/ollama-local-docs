import os
from flask import Flask, request, jsonify
from model import Model
from settings import Settings
from vectorStore import DocumentVectorStore
from sourceDocuments import SourceDocuments

# start up the model and vector store
settings = Settings()
source = SourceDocuments(settings)
llmModel = Model(settings)
vectorStore = DocumentVectorStore(settings)

app = Flask(__name__)

@app.route('/query', methods=['GET'])
def query():
    query = request.args.get('q')
    answer, docs = llmModel.ask(query)
    response = {
        "query": query,
        "answer": answer,
        "source_documents": docs
    }
    return jsonify(response)

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    if file:
        source.save_file(file)
        return jsonify({"message": f"File successfully uploaded"}), 200
    
@app.route('/store/update', methods=['POST'])
def update_store():
    chunks = vectorStore.updateStore()
    return jsonify({"message": f"Store updated with {len(chunks)} chunks"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5353)