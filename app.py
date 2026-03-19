import streamlit as st
import os
import openai

st.set_page_config(page_title="Med IA", page_icon="🏥")

st.title("🏥 Med IA")
st.write("💬 Descreva seus sintomas:")

# API KEY segura
openai.api_key = os.getenv("OPENAI_API_KEY")

if "chat" not in st.session_state:
    st.session_state.chat = []

entrada = st.text_input("Você:")

if entrada:
    resposta = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "Você é um assistente médico. Analise sintomas, sugira possíveis problemas, nível de risco, especialistas e emergência se necessário."},
            {"role": "user", "content": entrada}
        ]
    )

    texto = resposta.choices[0].message.content

    st.session_state.chat.append((entrada, texto))

for u, r in st.session_state.chat:
    st.write("👤:", u)
    st.write("🤖:", r)

if st.button("🔄 Nova consulta"):
    st.session_state.chat = []
    st.rerun()
