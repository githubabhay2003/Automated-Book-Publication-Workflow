# chroma_manager.py

import chromadb

# ✅ Use the new PersistentClient instead of deprecated Client + Settings
client = chromadb.PersistentClient(path="chroma_storage")

# ✅ Get or create the collection
collection = client.get_or_create_collection(name="book_versions")

def add_versioned_text(doc_id, text, metadata):
    """
    Adds a document to ChromaDB with versioning metadata.
    """
    collection.add(
        documents=[text],
        metadatas=[metadata],
        ids=[doc_id]
    )
    print(f"[✓] Added versioned text with ID: {doc_id}")

def semantic_search(query_text, top_k=3):
    """
    Performs semantic search across the stored documents.
    """
    results = collection.query(
        query_texts=[query_text],
        n_results=top_k
    )
    return results
