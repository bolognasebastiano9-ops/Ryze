import streamlit as st

st.set_page_config(page_title="Ryze OS", page_icon="🤖", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    stTextInput input { background-color: #262730; color: white; }
    </style>
    """, unsafe_allow_html=True)

st.title("🤖 Ryze Personal AI v1.0")
st.write("Sistemi online. Benvenuto, Sebastiano. 🚀")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "🤖 Sistemi inizializzati alla perfezione. Sono Ryze, il tuo assistente robot privato. Come posso aiutarti oggi, Sebastiano?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Invia un comando a Ryze..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        risposta_ryze = f"🤖 [Ryze OS]: Comando ricevuto: '{prompt}'. Interfaccia grafica creata con successo! I sistemi rispondono all'istante."
        st.markdown(risposta_ryze)
        st.session_state.messages.append({"role": "assistant", "content": risposta_ryze})