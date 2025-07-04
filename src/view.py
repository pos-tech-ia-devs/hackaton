from agents.architecture_diagram import run_agent
import streamlit as st
import os
import uuid
import shutil

st.set_page_config(page_title="Arch-Sec-Analyst", layout="wide")

st.title("🤖 Arch-Sec-Analyst")

st.write(
    "Faça o upload de um diagrama de arquitetura de sistemas para receber uma análise de ameaças automatizada usando a metodologia STRIDE."
)

with st.sidebar:
    st.header("Configurações")

    gemini_key_value = st.text_input(
        "Insira sua api key do Gemini",
        key="gemini_key_value",
        type="password",
        help="Insira sua chave de API do Gemini para autenticação. Você pode obter uma chave de API no console do Google Cloud.",
        value=os.getenv("GEMINI_API_KEY"),
    )

uploaded_file = st.file_uploader(
    "Escolha a imagem da arquitetura...", type=["png", "jpg", "jpeg"]
)

temp_directory = "./temp"

if uploaded_file is not None:
    st.image(uploaded_file, caption="Arquitetura Enviada", width=500)

    def save_uploaded_file(uploaded_file):
        try:
            file_id = str(uuid.uuid4())
            file_extension = os.path.splitext(uploaded_file.name)[1]
            file_name = f"{file_id}{file_extension}"
            os.makedirs(temp_directory, exist_ok=True)
            file_path = os.path.join(temp_directory, file_name)

            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
            return file_path
        except Exception as e:
            st.error(f"Error saving file: {e}")
            return None

    if st.button("Analisar Arquitetura"):
        with st.spinner(
            "Analisando a imagem e procurando vulnerabilidades... Por favor, aguarde. Isso pode levar alguns minutos."
        ):
            file_path = save_uploaded_file(uploaded_file)
            report = run_agent(file_path, api_key=gemini_key_value)

            if report:
                st.divider()
                st.subheader("Relatório de Análise de Ameaças - STRIDE")
                st.markdown(report)

                new_diagram_path = f"{temp_directory}/new_diagram.png"
                if os.path.exists(new_diagram_path):
                    st.image(
                        new_diagram_path,
                        caption="Novo Diagrama de Arquitetura",
                        width=1000,
                    )
            shutil.rmtree(temp_directory, ignore_errors=True)
