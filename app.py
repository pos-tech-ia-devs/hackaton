import os
import sys
import google.generativeai as genai
from PIL import Image
from dotenv import load_dotenv

# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()

# O prompt que definimos anteriormente
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

### T - Tampering (Adulteração de Dados)
*   **Ameaça:** (Descreva a ameaça de adulteração)
*   **Componentes Afetados:** (Liste os fluxos de dados, bancos de dados, etc.)
*   **Explicação:** (Detalhe como os dados podem ser alterados em trânsito ou em repouso)
*   **Mitigação Sugerida:** (Sugira soluções como HTTPS/TLS, assinaturas digitais, checksums, controle de integridade de arquivos, etc.)

### R - Repudiation (Repúdio)
*   **Ameaça:** (Descreva a ameaça de repúdio)
*   **Componentes Afetados:** (Liste os componentes responsáveis por ações críticas)
*   **Explicação:** (Detalhe como um ator poderia negar ter realizado uma ação)
*   **Mitigação Sugerida:** (Sugira soluções como logs de auditoria detalhados e seguros, assinaturas digitais, etc.)

### I - Information Disclosure (Divulgação de Informação)
*   **Ameaça:** (Descreva a ameaça de vazamento de dados)
*   **Componentes Afetados:** (Liste componentes que armazenam ou transmitem dados sensíveis)
*   **Explicação:** (Detalhe como dados sensíveis podem ser expostos)
*   **Mitigação Sugerida:** (Sugira soluções como criptografia em trânsito e em repouso, controle de acesso granular, tratamento de erros seguro, etc.)

### D - Denial of Service (Negação de Serviço)
*   **Ameaça:** (Descreva a ameaça de negação de serviço)
*   **Componentes Afetados:** (Identifique pontos únicos de falha ou componentes expostos)
*   **Explicação:** (Detalhe como um serviço pode ser tornado indisponível)
*   **Mitigação Sugerida:** (Sugira soluções como load balancers, auto-scaling, rate limiting, WAF, etc.)

### E - Elevation of Privilege (Elevação de Privilégio)
*   **Ameaça:** (Descreva a ameaça de elevação de privilégio)
*   **Componentes Afetados:** (Liste os componentes que gerenciam autorização)
*   **Explicação:** (Detalhe como um usuário com poucos privilégios poderia obter mais acesso)
*   **Mitigação Sugerida:** (Sugira soluções como o Princípio do Menor Privilégio, validação rigorosa de autorização em cada endpoint, etc.)

Analise a imagem fornecida e gere o relatório.
"""

def analyze_architecture(image_path: str):
    """
    Analisa uma imagem de arquitetura de sistemas usando o Gemini
    e retorna um relatório de ameaças STRIDE.
    """
    api_key = os.get("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Chave da API do Gemini não encontrada. Defina a variável de ambiente GEMINI_API_KEY.")

    genai.configure(api_key=api_key)

    try:
        img = Image.open(image_path)
    except FileNotFoundError:
        print(f"Erro: O arquivo de imagem '{image_path}' não foi encontrado.")
        return

    # Inicializa o modelo multimodal
    model = genai.GenerativeModel('gemini-1.5-flash')

    print("Analisando a arquitetura... Isso pode levar alguns segundos.")

    # Envia o prompt e a imagem para a API
    response = model.generate_content([PROMPT_TEMPLATE, img], stream=True)
    response.resolve()

    # Salva o relatório em um arquivo Markdown
    report_filename = f"report_{os.path.basename(image_path)}.md"
    with open(report_filename, "w", encoding="utf-8") as f:
        f.write(response.text)

    print("\n--- Relatório Gerado ---")
    print(response.text)
    print(f"\nRelatório completo salvo em: {report_filename}")

if __name__ == "__main__":
    analyze_architecture("azure.png")