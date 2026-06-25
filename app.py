import streamlit as st
import google.generativeai as genai
from PIL import Image

st.set_page_config(page_title="La mia AI Personale", page_icon="🤖", layout="centered")
st.title("🤖 RyzeOS(2.0)")
st.subheader("Sempre attiva sul Cloud 24/7")

# Recupera la chiave segreta in modo sicuro dalle impostazioni di Streamlit
if "GEMINI_API_KEY" in st.secrets:
    genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
else:
    st.error("Manca la chiave API! Inseriscila nei Secrets di Streamlit.")
    st.stop()

if "messages" not in st.session_state:
    st.session_state.messages = []

# Mostra la cronologia della chat
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Caricamento delle immagini
uploaded_file = st.file_uploader("Carica una foto da far vedere all'IA", type=["png", "jpg", "jpeg"])

if prompt := st.chat_input("Scrivi qualcosa a Ryze..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    
    st.session_state.messages.append({"role": "user", "content": prompt})

    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        
        # Scegliamo il modello corretto (Gemini Flash è velocissimo)
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        if uploaded_file:
            image = Image.open(uploaded_file)
            st.image(image, caption="Immagine inviata", use_container_width=True)
            # Se c'è un'immagine, inviamo sia il testo che la foto
            response = model.generate_content([prompt, image])
        else:
            # Altrimenti inviamo solo il testo della chat
            response = model.generate_content(prompt)
            
        message_placeholder.markdown(response.text)
        
    st.session_state.messages.append({"role": "assistant", "content": response.text})
