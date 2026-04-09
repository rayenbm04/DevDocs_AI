#!/bin/bash

# 1. Start the FastAPI backend on port 8000 in the background (the '&' is crucial)
uvicorn main:app --host 0.0.0.0 --port 8000 &

# 2. Wait a few seconds to let the backend fully load the ~300MB model
sleep 15

# 3. Start the Streamlit frontend on port 7860 (Hugging Face requires this exact port)
streamlit run frontend.py --server.port 7860 --server.address 0.0.0.0