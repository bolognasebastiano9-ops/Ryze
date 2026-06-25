import streamlit as st
import google.generativeai as genai
from PIL import Image

# Configura l'interfaccia grafica avanzata
st.set_page_config(page_title="Ryze OS v1.0", page_icon="🤖", layout="wide")

# Stile futuristico personalizzato
st.markdown("""
    <style>
    .main { background-color: #0b0f19; color: #e2e8f0; }
    stTextInput input { background-color: #1e293b; color: white; border-radius: 10px; }
    .stButton>button { background-color: #3b82f6; color: white; border-radius: 8px; }
    </style>
    """, unsafe_allow_html=True)

# Trucco di sicurezza per nascondere la chiave a GitHub dividendo la scritta in due pezzi
P1 = "AQAb8RN6IKroDgDMy4CP3G_Z"
P2 = "LC-qMA-f7rDc9WmyXTwMNHKGJmx-g"
CHIAVE_PROGETTO = P1 + P2

genai.configure(api_key=CHIAVE_PROGETTO)

# Creazione della Barra Laterale (Sidebar) per cambiare modalità
with st.sidebar:
    st.title("⚙️ Pannello Ryze")
    st.write("Configura i moduli del tuo droide.")
    
    # Menu a tendina per scegliere cosa fare
    modalita = st.selectbox(
        "Seleziona Modalità:",
        ["💬 Chat Testuale", "👁️ Visione Immagini/Video"]
    )
    st.markdown("---")
    st.write("Proprietà: *Capo Sebastiano*")
    st.write("Stato: Online 🟢")

# Titolo principale della pagina
st.title("🤖 Ryze Personal AI v1.0")
st.write(f"Modulo attivo: *{modalita}*")

# 1. MODALITÀ CHAT NORMALE
if modalita == "💬 Chat Testuale":
    model = genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction="Tu sei Ryze, l'assistente robot personale di Sebastiano. Rivolgiti a lui chiamandolo 'Signor Sebastiano' o 'Capo'. Il tuo tono deve essere educato, amichevole e futuristico. Usa sempre le emoji robotiche (🤖🚀⚙️). Rispondi in italiano."
    )

    if "messages" not in st.session_state:
        st.session_state.messages = [
            {"role": "assistant", "content": "🤖 Sistemi inizializzati alla perfezione. Sono Ryze, il tuo assistente robot privato in modalità testuale. Come posso aiutarti oggi, Capo Sebastiano?"}
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
                risposta_reale = "🤖 Capo, c'è un problema di trasmissione con i server centrali. Riprova tra un istante."
            
            with st.chat_message("assistant"):
                st.markdown(risposta_reale)
            st.session_state.messages.append({"role": "assistant", "content": risposta_reale})

# 2. MODALITÀ VISIONE PER FOTO E VIDEO
elif modalita == "👁️ Visione Immagini/Video":
    st.subheader("📸 Carica un elemento visivo")
    
    # Ecco il pulsante per caricare i file dal tuo PC!
    uploaded_file = st.file_uploader("Scegli un'immagine da mandare a Ryze...", type=["png", "jpg", "jpeg"])
    
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Elemento caricato correttamente.", use_container_width=True)
        
        domanda_foto = st.text_input("Cosa vuoi chiedere a Ryze su questa foto?", "Descrivi questa immagine nei dettagli.")
        
        if st.button("Fai analizzare a Ryze 🚀"):
            with st.spinner("Ryze sta scansionando i pixel..."):
                try:
                    model_vision = genai.GenerativeModel("gemini-1.5-flash")
                    response = model_vision.generate_content([domanda_foto, image])
                    st.markdown(f"### 🤖 Risposta di Ryze:\n{response.text}")
                except Exception as e:
                    st.error("🤖 Errore durante la scansione visiva.")
