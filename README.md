# DevDocs AI: Localized RAG Microservice 🤖

![Python](https://img.shields.io/badge/Python-3.11-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Spaces-F9AB00?logo=huggingface)

**Live Demo:** [Click here to chat with the AI](https://huggingface.co/spaces/rayenbm/DevDocs-AI)

## 📌 Overview
DevDocs AI is a fully localized Retrieval-Augmented Generation (RAG) application. It allows users to query documentation and receive highly accurate, context-aware answers without relying on paid, closed-source APIs like OpenAI. 

This project demonstrates a production-ready microservice architecture, separating the inference backend from the user interface, unified via Docker for cloud deployment.

## 🏗️ Architecture & Tech Stack
This application bypasses monolithic design in favor of a decoupled microservice approach:

* **Frontend (UI):** [Streamlit](https://streamlit.io/) — Provides a responsive, real-time chat interface.
* **Backend (API):** [FastAPI](https://fastapi.tiangolo.com/) — Handles the inference logic, model loading, and database querying.
* **Vector Database:** [ChromaDB](https://www.trychroma.com/) — Stores document embeddings for high-speed similarity search and context retrieval.
* **LLM & Embeddings:** [Hugging Face](https://huggingface.co/) — Utilizes `SmolLM2` (135M) for local text generation and `sentence-transformers` for embedding generation.
* **Deployment:** Containerized using a custom `Dockerfile` and bash scripting to run dual network ports simultaneously on Hugging Face Spaces.

## 🚀 Features
* **Zero External API Costs:** Runs completely on open-source models.
* **Hallucination Mitigation:** Grounded purely in the ingested `chroma_db` vector store; it only answers based on provided documentation.
* **Asynchronous Backend:** FastAPI ensures non-blocking requests for faster generation.
* **Unified Containerization:** A custom `run.sh` script manages background/foreground processes, allowing a multi-service app to run in a single lightweight Docker container.

## 💻 How to Run Locally

### 1. Clone the repository
```bash
git clone [https://github.com/](https://github.com/)rayenbm04/DevDocs-AI.git
cd DevDocs-AI
