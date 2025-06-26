from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document
import os
import pandas as pd

data  = pd.read_csv("realistic_restaurant_reviews.csv")

embeddings = OllamaEmbeddings(model="mxbai-embed-large")

db_location = "./restaurant_reviews_db"

if not os.path.exists(db_location):
    documents = []
    ids = []

    for i, row in data.iterrows():
        document = Document(
            page_content=row["Title"] + ""+row["Review"],
            metadata={
                "rating": row["Rating"],
                "date": row["Date"],
                "id": str(i)
            }
        )
        ids.append(str(i))
        documents.append(document)

vector_store = Chroma(
    collection_name="restaurant_reviews",
    embedding_function=embeddings,
    persist_directory=db_location
)

if not os.path.exists(db_location):
    vector_store.add_documents(documents=documents, ids=ids)

retirever = vector_store.as_retriever(
    search_kwargs={"k": 5}
    )