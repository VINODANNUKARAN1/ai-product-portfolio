"""
RAG Engine - Core retrieval and generation logic
Uses free tools: sentence-transformers + ChromaDB + HuggingFace

Architecture:
Document → Chunk → Embed → Store → Retrieve → Generate → Response
"""

import os
import tempfile
from typing import List, Dict
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


class RAGEngine:
    """
    RAG (Retrieval Augmented Generation) Engine
    
    Product Decision Log:
    - Embedding model: all-MiniLM-L6-v2 (free, fast, 384 dimensions)
    - Vector store: ChromaDB (free, local, no API needed)
    - Generation: Template-based (for free demo) or HuggingFace API
    - Chunk size: 500 tokens (balance between context and precision)
    - Overlap: 50 tokens (prevents cutting mid-sentence)
    """
    
    def __init__(self, chunk_size: int = 500, top_k: int = 3):
        self.chunk_size = chunk_size
        self.top_k = top_k
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=50,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
        # Free embedding model - runs locally, no API needed
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        self.vectorstore = None
        self.documents = []
    
    def add_document(self, uploaded_file) -> None:
        """Process and store a PDF document."""
        # Save uploaded file temporarily
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
            tmp.write(uploaded_file.getvalue())
            tmp_path = tmp.name
        
        # Load and split
        loader = PyPDFLoader(tmp_path)
        pages = loader.load()
        chunks = self.text_splitter.split_documents(pages)
        
        # Add source metadata
        for chunk in chunks:
            chunk.metadata['source'] = uploaded_file.name
        
        self.documents.extend(chunks)
        
        # Build/rebuild vector store
        self.vectorstore = Chroma.from_documents(
            documents=self.documents,
            embedding=self.embeddings
        )
        
        # Cleanup
        os.unlink(tmp_path)
    
    def query(self, question: str) -> Dict:
        """
        Query the knowledge base and generate an answer.
        
        Returns:
            dict with 'answer', 'sources', and 'confidence'
        """
        if not self.vectorstore:
            return {
                'answer': "No documents loaded. Please upload a PDF first.",
                'sources': [],
                'confidence': 0.0
            }
        
        # Retrieve relevant chunks
        results = self.vectorstore.similarity_search_with_score(
            question, k=self.top_k
        )
        
        if not results:
            return {
                'answer': "I couldn't find relevant information in the documents.",
                'sources': [],
                'confidence': 0.0
            }
        
        # Extract context from retrieved chunks
        context_parts = []
        sources = []
        total_score = 0
        
        for doc, score in results:
            context_parts.append(doc.page_content)
            sources.append({
                'content': doc.page_content,
                'metadata': doc.metadata
            })
            total_score += score
        
        context = "\n\n".join(context_parts)
        
        # Generate answer (using template-based approach for free demo)
        # In production: Replace with HuggingFace API or OpenAI
        answer = self._generate_answer(question, context)
        
        # Calculate confidence (inverse of average distance)
        avg_score = total_score / len(results)
        confidence = max(0.0, min(1.0, 1.0 - (avg_score / 2.0)))
        
        return {
            'answer': answer,
            'sources': sources,
            'confidence': confidence
        }
    
    def _generate_answer(self, question: str, context: str) -> str:
        """
        Generate answer from context.
        
        For FREE demo: Uses extractive approach (pulls best matching text).
        For PRODUCTION: Would use HuggingFace Inference API or OpenAI.
        
        To upgrade to HuggingFace API (still free tier):
        1. Get API key from huggingface.co
        2. Set HF_TOKEN environment variable
        3. Uncomment the API-based generation below
        """
        # === FREE VERSION: Extractive answer ===
        # Returns the most relevant context with formatting
        answer = f"Based on the documents, here's what I found:\n\n"
        answer += f"> {context[:1000]}\n\n"
        answer += f"*This answer is synthesized from {len(context.split())} words of source material.*"
        
        return answer
        
        # === PRODUCTION VERSION (Uncomment when you have HF API key): ===
        # from huggingface_hub import InferenceClient
        # client = InferenceClient(token=os.environ.get("HF_TOKEN"))
        # 
        # prompt = f"""Based on the following context, answer the question accurately.
        # If the answer is not in the context, say "I cannot find this information in the documents."
        # 
        # Context: {context[:2000]}
        # 
        # Question: {question}
        # 
        # Answer:"""
        # 
        # response = client.text_generation(
        #     prompt,
        #     model="mistralai/Mistral-7B-Instruct-v0.2",
        #     max_new_tokens=500
        # )
        # return response
