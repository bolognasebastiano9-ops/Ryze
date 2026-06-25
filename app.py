import streamlit as st
import google.generativeai as genai

# Configura l'interfaccia grafica
st.set_page_config(page_title="Ryze OS", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    stTextInput input { background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Ryze Personal AI v1.0")
st.write("Sistemi online. Benvenuto, Sebastiano. 🚀")

# ⚠️ INSERISCI QUI LA TUA CHIAVE API DI GEMINI TRA LE VIRGOLETTE
CHIAVE_API = AQ.Ab8RN6IS86oxENRyNV96rfhQJCY-U7RSn4b0EulM_pc2hzuyUg

# Inizializza il cervello di Ryze con le tue regole di rispetto
genai.configure(api_key=CHIAVE_API)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
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
            risposta_reale = "🤖 [Errore di Connessione]: Capo, verifica di aver inserito correttamente la chiave API nel codice."
        
        st.markdown(risposta_reale)
        st.session_state.messages.append({"role": "assistant", "content": risposta_reale})
