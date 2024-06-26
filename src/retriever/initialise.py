from langchain_community.vectorstores import FAISS
from src.retriever.config import ANSWERS_CSV_PATH, EMBEDDINGS_MODEL
from langchain_core.documents.base import Document
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_cohere import CohereEmbeddings
import dotenv

dotenv.load_dotenv()

def initialize_vector_db():
    """
    Initializes the vector database by loading documents, splitting text into chunks,
    and creating embeddings for each chunk.

    Returns:
        FAISS: The initialized vector database.
    """
    loader = PyPDFLoader(file_path=ANSWERS_CSV_PATH)
    raw_documents = loader.load()
    
    documents = []
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    for raw_doc in raw_documents:
        chunks = text_splitter.split_text(raw_doc.page_content)
        for chunk in chunks:
            documents.append(Document(page_content=chunk))

    # Create embeddings for each chunk
    embeddings = CohereEmbeddings(model="embed-english-light-v3.0")

    # Initialize the FAISS vector database with the documents and their embeddings
    vector_db = FAISS.from_documents(
        documents,
        embeddings,
    )
    return vector_db

vector_db = initialize_vector_db()
