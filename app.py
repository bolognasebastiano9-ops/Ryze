import streamlit as st
import google.generativeai as genai

# Grafica semplice e pulita
st.set_page_config(page_title="Ryze OS", page_icon="🤖")
st.title("🤖 RyzeOS")
st.write("Sistemi online. Benvenuto, Sebastiano. 🚀")

# Configurazione diretta del cervello
CHIAVE_API = "AQ.Ab8RN6LqjPNJREF9TuHW4r-2ioPlNa2PY8vl0CDtKo1Ly-3PfQ"
genai.configure(api_key=CHIAVE_API)

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
