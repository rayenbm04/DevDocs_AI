import streamlit as st
import requests

# 1. Setup the Page
st.set_page_config(page_title="DevDocs AI", page_icon="🤖")
st.title("DevDocs AI Assistant 🤖")
st.write("Ask me anything about the DevDocs framework!")

# 2. Initialize Chat History
# Streamlit reruns the script on every interaction. We use session_state to remember the chat.
if "messages" not in st.session_state:
    st.session_state.messages = []

# 3. Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 4. Handle User Input
# This creates the chat box at the bottom of the screen
if prompt := st.chat_input("E.g., How do I authenticate?"):
    
    # Show the user's message immediately
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 5. Talk to the FastAPI Backend
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                # We send the question to the local server we built earlier
                response = requests.post(
                    "http://127.0.0.1:8000/chat",
                    json={"question": prompt}
                )
                response.raise_for_status()
                
                # Extract the answer and display it
                answer = response.json()["answer"]
                st.markdown(answer)
                
                # Save the AI's response to history
                st.session_state.messages.append({"role": "assistant", "content": answer})
                
            except requests.exceptions.ConnectionError:
                st.error("🚨 Cannot connect to the backend!")
                st.info("Make sure your FastAPI server is running in another terminal window.")