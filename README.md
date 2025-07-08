# 🤖 Arch-Sec-Analyst: Análise de Ameaças Automatizada com IA

**Analisador de Ameaças de Arquitetura de Sistemas utilizando Google Gemini e a metodologia STRIDE.**

---

## 📜 Índice

- [1. Introdução](#1-introdução)
- [2. O Problema: A Complexidade da Modelagem de Ameaças](#2-o-problema-a-complexidade-da-modelagem-de-ameaças)
- [3. A Solução: Arch-Sec-Analyst](#3-a-solução-arch-sec-analyst)
- [4. Funcionalidades Principais](#4-funcionalidades-principais)
- [5. Arquitetura e Fluxo de Execução](#5-arquitetura-e-fluxo-de-execução)
- [6. Tecnologias Utilizadas](#6-tecnologias-utilizadas)
- [7. Como Instalar e Executar](#7-como-instalar-e-executar)
  - [Pré-requisitos](#pré-requisitos)
  - [Passos para Instalação](#passos-para-instalação)
  - [Como Executar](#como-executar)
- [8. Como Contribuir](#8-como-contribuir)

---

## 1. Introdução

O **Arch-Sec-Analyst** é um projeto desenvolvido como parte do curso de Pós-Graduação em IA para Devs. A ferramenta visa revolucionar o processo de modelagem de ameaças (Threat Modeling), utilizando o poder dos Grandes Modelos de Linguagem (LLMs), especificamente o **Google Gemini**, para automatizar a análise de segurança de arquiteturas de sistemas.

A segurança da informação é um pilar fundamental no desenvolvimento de software. Identificar vulnerabilidades em fases iniciais do projeto economiza tempo, recursos e previne incidentes de segurança. O Arch-Sec-Analyst surge como uma solução inteligente para tornar essa análise mais acessível, rápida e eficiente.

## 2. O Problema: A Complexidade da Modelagem de Ameaças

A modelagem de ameaças é um processo crítico, mas frequentemente complexo e demorado. Tradicionalmente, ele exige:

- **Conhecimento Especializado:** Profissionais de segurança com vasta experiência para identificar uma ampla gama de vetores de ataque.
- **Tempo e Esforço Manuais:** Análise detalhada de diagramas e documentação, um processo que pode levar horas ou dias.
- **Inconsistência:** A qualidade da análise pode variar significativamente dependendo do profissional envolvido.
- **Escalabilidade:** Em ambientes de desenvolvimento ágil (Agile) e DevOps, a análise manual se torna um gargalo, dificultando a integração da segurança no ciclo de vida de desenvolvimento de software (SDLC).

## 3. A Solução: Arch-Sec-Analyst

O Arch-Sec-Analyst aborda esses desafios de frente, automatizando a análise de ameaças com o uso de IA. A ferramenta recebe um diagrama de arquitetura (em formato de imagem) e, em questão de segundos, gera um relatório completo baseado na metodologia **STRIDE**.

**STRIDE** é um mnemônico para as seis principais categorias de ameaças de segurança:

- **S**poofing (Falsificação de Identidade)
- **T**ampering (Adulteração de Dados)
- **R**epudiation (Repúdio)
- **I**nformation Disclosure (Divulgação de Informações)
- **D**enial of Service (Negação de Serviço)
- **E**levation of Privilege (Elevação de Privilégio)

Ao automatizar essa análise, o projeto democratiza o acesso a práticas de segurança robustas, permitindo que equipes de desenvolvimento identifiquem e mitiguem riscos de forma proativa.

## 4. Funcionalidades Principais

- **Análise Visual Inteligente:** Utiliza a capacidade multimodal do Google Gemini para interpretar componentes, fluxos de dados e limites de confiança diretamente de uma imagem de arquitetura.
- **Relatórios STRIDE Completos:** Gera um relatório detalhado em Markdown, identificando ameaças potenciais para cada categoria do STRIDE, com explicações e sugestões de mitigação.
- **Geração de Diagramas Corrigidos:** Após a análise, a ferramenta gera um novo diagrama de arquitetura em código Mermaid, incorporando as mitigações sugeridas, permitindo uma visualização clara da arquitetura aprimorada.
- **Interface Web Interativa:** Uma aplicação amigável construída com Streamlit que permite o upload de imagens e a visualização dos relatórios de forma intuitiva.
- **Suporte a Linha de Comando (CLI):** Oferece uma interface de linha de comando para facilitar a automação e a integração com pipelines de CI/CD e outros scripts.

## 5. Arquitetura e Fluxo de Execução

O projeto é construído sobre uma arquitetura de agentes inteligentes orquestrada pela biblioteca **LangChain**. Isso permite uma clara separação de responsabilidades e um fluxo de trabalho modular.

### Componentes Principais:

- **Agente Orquestrador (`architecture_diagram.py`):** É o cérebro do sistema. Ele recebe a requisição inicial e coordena a execução das ferramentas na sequência correta para cumprir o objetivo.
- **Ferramentas (`toolkit.py`):** São funções especializadas que o agente pode invocar. Cada ferramenta tem uma responsabilidade única:
  - `analyze_image`: Analisa a imagem da arquitetura.
  - `stride`: Gera o relatório de ameaças STRIDE.
  - `generate_fixed_report`: Cria um relatório de remediação.
  - `generate_mermaid_diagram`: Gera o novo diagrama corrigido.
- **Prompts (`prompts/`):** Contêm as instruções detalhadas que guiam o comportamento do LLM para cada tarefa específica, garantindo resultados consistentes e de alta qualidade.

### Fluxo de Execução:

1.  **Entrada do Usuário:** O usuário fornece um diagrama de arquitetura através da interface web ou CLI.
2.  **Início do Agente:** O Agente Orquestrador é ativado com um objetivo claro: analisar a imagem, gerar relatórios e criar um novo diagrama.
3.  **Análise da Imagem:** O agente invoca a ferramenta `analyze_image` para interpretar o diagrama.
4.  **Análise STRIDE:** Com o entendimento da arquitetura, a ferramenta `stride` é chamada para gerar o relatório de ameaças.
5.  **Relatório de Correção:** A ferramenta `generate_fixed_report` é usada para detalhar as mitigações.
6.  **Geração do Novo Diagrama:** Por fim, a ferramenta `generate_mermaid_diagram` cria o código Mermaid para o diagrama de arquitetura seguro.
7.  **Saída:** O resultado final (relatórios e o novo diagrama) é apresentado ao usuário.

## 6. Tecnologias Utilizadas

- **Linguagem de Programação:** Python 3.11
- **Inteligência Artificial:**
  - **Google Gemini 2.5 Flash e Pro:** Modelo de linguagem multimodal para análise de imagem e geração de texto.
  - **LangChain:** Framework para orquestração de agentes e desenvolvimento de aplicações com LLMs.
- **Interface de Usuário:** Streamlit

## 7. Como Instalar e Executar

### Pré-requisitos

- Python 3.8 ou superior
- Git
- Uma chave de API do **Google Gemini**.

### Passos para Instalação

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/pos-tech-ia-devs/hackaton.git
    cd hackaton
    ```

2.  **Crie e ative um ambiente virtual:**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure sua chave de API:**
    - Crie um arquivo `.env` na raiz do projeto.
    - Adicione sua chave de API do Gemini ao arquivo:
      ```
      GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
      ```

### Como Executar

#### Interface Web (Recomendado)

1.  **Inicie a aplicação Streamlit:**
    ```bash
    make streamlit # OU python3 -m streamlit run src/view.py
    ```
2.  Abra seu navegador no endereço `http://localhost:8501`.
3.  Faça o upload do seu diagrama e clique em "Analisar Arquitetura".

#### Linha de Comando (CLI)

1.  **Execute o script principal:**
    ```bash
    make run # OU python main.py
    ```
2.  O script analisará a imagem padrão (`resources/aws.png`) e imprimirá o relatório no console.
