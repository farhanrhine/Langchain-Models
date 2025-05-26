from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', dimensions=300)

documents = [
    "Delhi is the capital of India",
    "Chandighar is the capital of Punjab",
    "Paris is the capital of France"
]

vector = embedding.embed_documents(documents)

print(str(vector))

