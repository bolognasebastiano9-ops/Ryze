import streamlit as st
import google.generativeai as genai

# Grafica semplice e pulita per il tuo chatbot
st.set_page_config(page_title="Ryze OS", page_icon="🤖")
st.title("🤖 Ryze Personal AI v1.0")
st.write("Sistemi online. Benvenuto, Capo Sebastiano. 🚀")

# Utilizziamo la cassaforte dei Secrets di Streamlit per la massima stabilità
CHIAVE_API = st.secrets["CHIAVE_GEMINI"]
genai.configure(api_key=CHIAVE_API)

# Configurazione del modello di ultima generazione 2.0
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    system_instruction="Tu sei Ryze, l'assistente robot personale di Sebastiano. Rivolgiti a lui chiamandolo 'Signor Sebastiano' o 'Capo'. Il tuo tono deve essere educato, amichevole e futuristico. Usa sempre le emoji robotiche (🤖🚀⚙️). Rispondi in italiano."
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "🤖 Sistemi inizializzati alla perfezione. Sono Ryze, il tuo assistente robot privato. Come posso aiutarti oggi, Capo Sebastiano?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Invia un comando a Ryze..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        try:
            response = model.generate_content(prompt)
            risposta_reale = response.text
        except Exception as e:
            risposta_reale = f"🤖 [Errore di Connessione]: {str(e)}"
        
        st.markdown(risposta_reale)
        st.session_state.messages.append({"role": "assistant", "content": risposta_reale})
