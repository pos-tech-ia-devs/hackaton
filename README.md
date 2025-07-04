# 🤖 Arch-Sec-Analyst: Analisador de Ameaças com IA

## Visão Geral

O Arch-Sec-Analyst é uma ferramenta poderosa que utiliza a inteligência artificial do Google Gemini para realizar análises de ameaças em diagramas de arquitetura de sistemas. A análise é baseada na metodologia STRIDE (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege), um modelo de ameaças amplamente reconhecido para identificar e mitigar riscos de segurança.

## ✨ Funcionalidades Principais

- **Análise de Ameaças Automatizada**: Envie um diagrama de arquitetura e receba um relatório de ameaças completo.
- **Suporte para Múltiplos Formatos de Imagem**: Compatível com os formatos de imagem mais comuns (PNG, JPG, JPEG).
- **Relatórios Detalhados**: Gera relatórios em formato Markdown, fáceis de ler e integrar em documentações.
- **Duas Interfaces de Uso**:
  - **Interface Web**: Uma aplicação interativa construída com Streamlit para uma experiência de usuário amigável.
  - **Linha de Comando (CLI)**: Para automação e integração com outros scripts e fluxos de trabalho.

## 🏗️ Arquitetura do Projeto

- **`app.py`**: Contém o código da interface web construída com Streamlit. É o ponto de entrada para a execução da aplicação no modo interativo.
- **`main.py`**: Ponto de entrada para a execução via linha de comando. Permite analisar uma imagem local e exibir o relatório no console.
- **`core.py`**: O coração do projeto. Este módulo contém a lógica de análise, a formatação do prompt e a integração com a API do Google Gemini.
- **`requirements.txt`**: Lista todas as bibliotecas Python necessárias para o funcionamento do projeto.
- **`.env`**: Arquivo de configuração para armazenar variáveis de ambiente, como a chave da API do Gemini.

## ⚙️ Configuração do Ambiente

### Pré-requisitos

- Python 3.8 ou superior
- Uma chave de API do Google Gemini

### Passos para Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/pos-tech-ia-devs/hackaton.git
    cd hackaton
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a chave da API:**
    - Crie um arquivo chamado `.env` na raiz do projeto.
    - Adicione sua chave da API do Google Gemini a este arquivo:
      ```
      GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
      ```

## 🚀 Como Executar

### 1. Executando a Interface Web

Para uma experiência interativa, use a aplicação Streamlit.

1.  **Inicie a aplicação:**
    ```bash
    streamlit run app.py
    ```
2.  Abra o navegador no endereço fornecido (geralmente `http://localhost:8501`).
3.  Clique no botão "Escolha a imagem da arquitetura..." para fazer o upload do seu diagrama.
4.  Clique em "Analisar Arquitetura" e aguarde o relatório ser gerado.

### 2. Executando via Linha de Comando

Para automação ou uso em scripts, você pode executar a análise diretamente pelo terminal.

1.  Certifique-se de que o caminho da imagem no arquivo `main.py` está correto. Por padrão, ele aponta para `resources/aws.png`.
2.  **Execute o script:**
    ```bash
    python main.py
    ```
3.  O relatório de análise será impresso diretamente no console.

## 📄 Exemplo de Uso (Interface Web)

1.  Após iniciar a aplicação com `streamlit run app.py`, você verá a tela inicial.
2.  Faça o upload de um diagrama de arquitetura (como o exemplo em `resources/aws.png`).
3.  A imagem será exibida na tela.
4.  Clique no botão "Analisar Arquitetura".
5.  Aguarde alguns segundos enquanto o Gemini processa a imagem.
6.  O relatório completo da análise STRIDE será exibido abaixo da imagem.
