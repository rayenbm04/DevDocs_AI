from fastapi import FastAPI
from pydantic import BaseModel
from langchain_huggingface import HuggingFaceEmbeddings, HuggingFacePipeline
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. Initialize the FastAPI Web Server
app = FastAPI(title="DevDocs AI API")

# 2. Define the data format we expect from the frontend
class ChatRequest(BaseModel):
    question: str

# 3. Load Models & Database on Startup
print("Loading embedding model...")
embeddings_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

print("Connecting to ChromaDB...")
# We connect to the folder you just created in Step 2
vectorstore = Chroma(persist_directory="./chroma_db", embedding_function=embeddings_model)
# A retriever searches the DB and returns the top 2 most relevant chunks
retriever = vectorstore.as_retriever(search_kwargs={"k": 2})

print("Loading local LLM (This will download ~300MB the first time)...")
# We use a fast, local Hugging Face model to generate the text
llm = HuggingFacePipeline.from_model_id(
    model_id="HuggingFaceTB/SmolLM2-135M-Instruct",
    task="text-generation",
    pipeline_kwargs={"max_new_tokens": 100}
)

# 4. Build the RAG Chain (LangChain Expression Language - LCEL)
# This is the prompt that instructs the AI on how to behave
template = """Answer the question using ONLY the provided context. If you don't know, say "I don't know".
Context: {context}
Question: {question}
Answer:"""
prompt = PromptTemplate.from_template(template)

# Helper function to combine our retrieved documents into one string
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# The actual pipeline: Retrieve -> Insert into Prompt -> Send to LLM -> Output Text
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 5. Create the API Endpoint
@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    print(f"User asked: {request.question}")
    
    # Pass the user's question through our RAG chain
    response = rag_chain.invoke(request.question)
    
    return {"answer": response}