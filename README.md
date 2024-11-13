# Retrieval-Augmented-Generation
Retrieval Augmented Generation for all kind of data sources.
# Flexible Document Ingestion and Vector Search System with LangChain

This repository provides a flexible solution for document ingestion and vectorized search using the LangChain library. The system supports loading data from multiple document formats (e.g., text files, PDFs, web pages), chunking large documents into manageable pieces, embedding these chunks as vectors, and storing them in a vector database for similarity search. This setup can handle a wide range of formats and is designed for easy expansion.

## Features

- **Multi-format Document Ingestion**: Load data from text files, PDFs, and web pages with a universal loader function.
- **Document Chunking**: Split documents into smaller, manageable parts for optimized embedding and retrieval.
- **Vector Embedding and Storage**: Use OpenAI embeddings to vectorize document chunks and store them for efficient search.
- **Flexible Vector Store Options**: Store vectors in Chroma or FAISS, with FAISS optimized for larger datasets.
- **Environment Management**: Securely handle API keys with `.env` configuration.

## Setup

### Prerequisites

- Python 3.8+
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- Required Python packages in `requirements.txt` (see below)

### Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/shivanshu007/Retrieval-Augmented-Generation.git
   cd document-ingestion-vector-search

