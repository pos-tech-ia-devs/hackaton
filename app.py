# app.py
import streamlit as st
import os
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# --- Configuração do Gemini e Prompt (mesmo de antes) ---

# O prompt que instrui o modelo
PROMPT_TEMPLATE = """
Você é um especialista em segurança da informação e arquiteto de soluções, especializado em modelagem de ameaças (Threat Modeling).

Sua tarefa é analisar a imagem de uma arquitetura de sistemas que fornecerei. Você deve identificar os componentes, os fluxos de dados, os limites de confiança (trust boundaries) e, em seguida, realizar uma análise de ameaças completa usando a metodologia STRIDE.

Para cada categoria do STRIDE, identifique ameaças potenciais, explique por que são uma ameaça nesta arquitetura específica e sugira uma ou mais mitigações.

Apresente o resultado em formato Markdown, seguindo estritamente esta estrutura:

# Relatório de Análise de Ameaças - Metodologia STRIDE

## Análise da Arquitetura
(Descreva brevemente os componentes e fluxos que você identificou na imagem.)

---

## Análise STRIDE

### S - Spoofing (Falsificação de Identidade)
*   **Ameaça:** (Descreva a ameaça de falsificação)
*   **Componentes Afetados:** (Liste os componentes)
*   **Explicação:** (Detalhe como a ameaça pode ocorrer)
*   **Mitigação Sugerida:** (Sugira soluções como autenticação forte, mTLS, verificação de certificados, etc.)
*   **Referencias:** (Inclua links para documentação ou melhores práticas, se possível)

### T - Tampering (Adulteração de Dados)
*   **Ameaça:** (Descreva a ameaça de adulteração)
*   **Componentes Afetados:** (Liste os fluxos de dados, bancos de dados, etc.)
*   **Explicação:** (Detalhe como os dados podem ser alterados em trânsito ou em repouso)
*   **Mitigação Sugerida:** (Sugira soluções como HTTPS/TLS, assinaturas digitais, checksums, controle de integridade de arquivos, etc.)
*   **Referencias:** (Inclua links para documentação ou melhores práticas, se possível)

### R - Repudiation (Repúdio)
*   **Ameaça:** (Descreva a ameaça de repúdio)
*   **Componentes Afetados:** (Liste os componentes responsáveis por ações críticas)
*   **Explicação:** (Detalhe como um ator poderia negar ter realizado uma ação)
*   **Mitigação Sugerida:** (Sugira soluções como logs de auditoria detalhados e seguros, assinaturas digitais, etc.)
*   **Referencias:** (Inclua links para documentação ou melhores práticas, se possível)

### I - Information Disclosure (Divulgação de Informação)
*   **Ameaça:** (Descreva a ameaça de vazamento de dados)
*   **Componentes Afetados:** (Liste componentes que armazenam ou transmitem dados sensíveis)
*   **Explicação:** (Detalhe como dados sensíveis podem ser expostos)
*   **Mitigação Sugerida:** (Sugira soluções como criptografia em trânsito e em repouso, controle de acesso granular, tratamento de erros seguro, etc.)
*   **Referencias:** (Inclua links para documentação ou melhores práticas, se possível)

### D - Denial of Service (Negação de Serviço)
*   **Ameaça:** (Descreva a ameaça de negação de serviço)
*   **Componentes Afetados:** (Identifique pontos únicos de falha ou componentes expostos)
*   **Explicação:** (Detalhe como um serviço pode ser tornado indisponível)
*   **Mitigação Sugerida:** (Sugira soluções como load balancers, auto-scaling, rate limiting, WAF, etc.)
*   **Referencias:** (Inclua links para documentação ou melhores práticas, se possível)

### E - Elevation of Privilege (Elevação de Privilégio)
*   **Ameaça:** (Descreva a ameaça de elevação de privilégio)
*   **Componentes Afetados:** (Liste os componentes que gerenciam autorização)
*   **Explicação:** (Detalhe como um usuário com poucos privilégios poderia obter mais acesso)
*   **Mitigação Sugerida:** (Sugira soluções como o Princípio do Menor Privilégio, validação rigorosa de autorização em cada endpoint, etc.)
*   **Referencias:** (Inclua links para documentação ou melhores práticas, se possível)

Analise a imagem fornecida e gere o relatório.
"""

def analyze_architecture(image_data):
    """
    Analisa uma imagem de arquitetura de sistemas usando o Gemini
    e retorna um relatório de ameaças STRIDE.

    Argumentos:
        image_data: Um objeto de imagem aberto (como o retornado pelo st.file_uploader).
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        # Mostra um erro na própria interface do Streamlit
        st.error("Chave da API do Gemini não encontrada. Por favor, configure seu arquivo .env ou as secrets do Streamlit.")
        return None

    genai.configure(api_key=api_key)
    
    # Prepara a imagem e o modelo
    img = Image.open(image_data)
    model = genai.GenerativeModel('gemini-2.5-flash')

    try:
        # Gera o conteúdo
        response = model.generate_content([PROMPT_TEMPLATE, img])
        return response.text
    except Exception as e:
        st.error(f"Ocorreu um erro ao chamar a API do Gemini: {e}")
        return None

# --- Interface do Streamlit ---

# Configuração da página (título na aba do navegador e layout)
st.set_page_config(page_title="Arch-Sec-Analyst", layout="wide")

# Título principal da aplicação
st.title("🤖 Arch-Sec-Analyst com Gemini")

# Descrição
st.write("Faça o upload de um diagrama de arquitetura de sistemas para receber uma análise de ameaças automatizada usando a metodologia STRIDE.")

# Componente para upload de arquivo
uploaded_file = st.file_uploader(
    "Escolha a imagem da arquitetura...",
    type=["png", "jpg", "jpeg"]
)

# Verifica se um arquivo foi enviado
if uploaded_file is not None:
    # Mostra a imagem enviada
    st.image(uploaded_file, caption="Arquitetura Enviada", width=500)

    # Adiciona um botão para iniciar a análise
    if st.button("Analisar Arquitetura"):
        # Mostra uma mensagem de "carregando" enquanto a análise ocorre
        with st.spinner("O Gemini está analisando a imagem... Por favor, aguarde. Isso pode levar alguns segundos."):
            report = analyze_architecture(uploaded_file)
            
            if report:
                st.divider() # Adiciona uma linha divisória
                st.subheader("Relatório de Análise de Ameaças - STRIDE")
                # st.markdown() renderiza o texto em formato Markdown, que é o formato da nossa saída
                st.markdown(report)
