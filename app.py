import streamlit as st
from groq import Groq

# Configurazione della pagina
st.set_page_config(page_title="Rides OS", page_icon="🤖", layout="centered")

st.title("🤖 RyzeOS(2.0)")
st.subheader("Come posso aiutarti oggi?")

# Recupera la chiave segreta di Groq dai Secrets di Streamlit
if "GROQ_API_KEY" in st.secrets:
    api_key = st.secrets["GROQ_API_KEY"]
else:
    st.error("Manca la chiave API di Groq! Inseriscila nei Secrets di Streamlit con il nome GROQ_API_KEY.")
    st.stop()

# Inizializza il client Groq
client = Groq(api_key=api_key)

# Inizializza la cronologia dei messaggi in memoria se non esiste
if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra i messaggi precedenti nella chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dell'utente
if prompt := st.chat_input("Scrivi qualcosa a RyzeOS..."):
    # Mostra il messaggio dell'utente
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Salva il messaggio dell'utente nella cronologia
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Genera la risposta dell'IA con Groq
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        try:
            # Creiamo i messaggi includendo la cronologia e l'istruzione di sistema
            messages_history = [
                {"role": "system", "content": "Sei Rides OS, un'IA amichevole, sveglia e personalizzata. Rispondi SEMPRE in italiano in modo chiaro, fluido e naturale, evitando toni robotici."}
            ]
            
            # Aggiungiamo gli ultimi messaggi per mantenere il filo del discorso
            for msg in st.session_state.messages[-10:]:
                messages_history.append({"role": msg["role"], "content": msg["content"]})

            # Chiamata ai server veloci di Groq (Modello Llama 3)
            completion = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=messages_history,
            )
            
            response_text = completion.choices[0].message.content
            message_placeholder.markdown(response_text)
            
            # Salva la risposta dell'IA nella cronologia
            st.session_state.messages.append({"role": "assistant", "content": response_text})
            
        except Exception as e:
            st.error(f"Errore durante la generazione: {e}")
