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

# La tua chiave API numero 3 corretta e funzionante con le sue virgolette
CHIAVE_API = "AQAb8RN6IKroDgDMy4CP3G_ZLC-qMA-f7rDc9WmyXTwMNHKGJmx-g"
genai.configure(api_key=CHIAVE_API)

# Creazione della Barra Laterale (Sidebar) per cambiare modalità
with st.sidebar:
    st.title("⚙️ Pannello Ryze")
    st.write("Configura i moduli del tuo droide.")
    
    # Menu a tendina per scegliere cosa fare
    modalita = st.selectbox(
        "Seleziona Modalità:",
        ["💬 Chat Testuale", "👁️ Visione Immagini/Video", "🌐 Analisi Link"]
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
                risposta_reale = "🤖 Capo, si è verificato un errore nel caricamento della risposta."
            st.markdown(risposta_reale)
            st.session_state.messages.append({"role": "assistant", "content": respuesta_reale})

# 2. MODALITÀ VISIONE PER FOTO E VIDEO
elif modalita == "👁️ Visione Immagini/Video":
    st.subheader("📸 Carica un elemento visivo")
    
    # Ecco il pulsante per caricare i file!
    uploaded_file = st.file_uploader("Scegli un'immagine o un video da mandare a Ryze...", type=["png", "jpg", "jpeg", "mp4"])
    
    if uploaded_file is not None:
        if uploaded_file.type.startswith('image'):
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
        else:
            st.video(uploaded_file)
            st.info("🤖 Ricezione video completata. Funzione di analisi video in attivazione.")

# 3. MODALITÀ ANALISI LINK
elif modalita == "🌐 Analisi Link":
    st.subheader("🔗 Analizzatore Web")
    url_input = st.text_input("Incolla qui un link internet da far leggere a Ryze:")
    domanda_link = st.text_input("Cosa vuoi sapere su questo sito?", "Fammi un riassunto di questa pagina.")
    
    if st.button("Analizza link 🚀"):
        st.warning("🤖 Funzione di navigazione web in corso di configurazione sul server.")
