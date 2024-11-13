from langchain.document_loaders import TextLoader, WebBaseLoader, PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma, FAISS
from pydantic import BaseModel
from dotenv import load_dotenv
import bs4
import os
from pathlib import Path

load_dotenv()
os.environ['OPENAI_API_KEY'] = os.getenv("OPENAI_API_KEY")

class GlobalConfig(BaseModel):
    class Config:
        arbitrary_types_allowed = True

def load_documents(file_paths):
    all_documents = []
    for path in file_paths:
        ext = Path(path).suffix.lower()
        if ext == ".txt":
            loader = TextLoader(path)
        elif ext == ".pdf":
            loader = PyPDFLoader(path)
        elif ext.startswith(("http://", "https://")):
            loader = WebBaseLoader(
                web_paths=(path,),
                bs_kwargs=dict(parse_only=bs4.SoupStrainer(class_=("post-title", "post-content", "post-header")))
            )
        else:
            print(f"Unsupported file format: {ext}")
            continue
        
        documents = loader.load()
        all_documents.extend(documents)
    
    return all_documents

file_paths = ["speech.txt", "attention.pdf", "https://lilianweng.github.io/posts/2023-06-23-agent/"]
all_documents = load_documents(file_paths)
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
chunked_documents = text_splitter.split_documents(all_documents)
embeddings = OpenAIEmbeddings()
chroma_db = Chroma.from_documents(chunked_documents, embeddings)
query = "What is the future work?"
retrieved_results = chroma_db.similarity_search(query)
print("Top Retrieved Result:", retrieved_results[0].page_content)
