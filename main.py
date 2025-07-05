import chat_mind
import streamlit as st
from scraper import get_data
from chat_mind import find_similar_paragraphs

st.title("ISRO Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Load scraped data and embeddings once
if "ls" not in st.session_state:
    st.session_state.ls, st.session_state.embeddings, st.session_state.model = get_data()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything about all the ISRO Missions"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    results = find_similar_paragraphs(
    prompt,
    st.session_state.ls,
    st.session_state.embeddings,
    st.session_state.model  # ✅ Pass model here
)

    reply = "\n\n".join(
        [f"✅ Score: {score:.2f}\n{para}" for score, para in results]
    )

    with st.chat_message("assistant"):
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
