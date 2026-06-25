import streamlit as st
import ollama

# Configura il titolo della pagina nel browser
st.set_page_config(page_title="La mia AI Personale", page_icon="🤖")
st.title("🤖 RyzeOS(2.0)")
st.write("Interfaccia personalizzata per Ryze!")

# Inizializza la cronologia dei messaggi se non esiste
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra i messaggi precedenti in chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dell'utente
if prompt := st.chat_input("Scrivi qualcosa a Ryze..."):
    # Mostra il messaggio dell'utente nella chat
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Risposta dell'IA
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Parla con Ollama usando tinyllama
        response = ollama.chat(
            model='qwen2.5:1.5b',
            messages=st.session_state.messages,
            stream=True,
        )
        
        # Mostra la risposta un pezzettino alla volta (effetto streaming)
        for chunk in response:
            full_response += chunk['message']['content']
            message_placeholder.markdown(full_response + "▌")
        
        message_placeholder.markdown(full_response)
        
    st.session_state.messages.append({"role": "assistant", "content": full_response})