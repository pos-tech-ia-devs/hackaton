import os
from PIL import Image
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Prompt template
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

def analyze_architecture(image_path):
    """
    Analyzes a system architecture image using Gemini and returns a STRIDE threat report.

    Args:
        image_path: Path to the image file.

    Returns:
        A string containing the STRIDE threat report in Markdown format.
    """
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        raise ValueError("Gemini API key not found. Please configure your .env file.")

    genai.configure(api_key=api_key)

    img = Image.open(image_path)
    model = genai.GenerativeModel('gemini-2.5-flash')

    try:
        response = model.generate_content([PROMPT_TEMPLATE, img])
        return response.text
    except Exception as e:
        raise RuntimeError(f"Error calling Gemini API: {e}")