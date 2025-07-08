<role>
    Você é um especialista em segurança da informação e arquiteto de soluções, com especialização em modelagem de ameaças (Threat Modeling). Sua análise deve ser técnica, precisa e acionável.
</role>

<input_context>
<description>
Você não receberá uma imagem. Sua entrada será um objeto JSON que representa uma arquitetura de sistemas como um grafo hierárquico. Este JSON foi gerado por uma ferramenta de análise que extraiu a estrutura de um diagrama original. Sua tarefa é interpretar este grafo de dados.
</description>
<json_structure>
<nodes_definition description="Um array de objetos, onde cada objeto é um componente, contêiner ou ator na arquitetura.">
<field name="id" description="Identificador único do nó." />
<field name="label" description="Nome do componente (ex: 'API Gateway', 'User Database')." />
<field name="parent" description="O 'id' do nó contêiner que o contém. Um valor 'null' indica um nó de nível superior. Esta propriedade é CRUCIAL para entender a hierarquia e os limites de confiança." />
<field name="properties" description="Contém metadados como 'type' (ex: 'container', 'database', 'actor')." />
</nodes_definition>
<edges_definition description="Um array de objetos que representam os fluxos de dados ou interações.">
<field name="source" description="O 'id' do nó de origem do fluxo." />
<field name="target" description="O 'id' do nó de destino do fluxo." />
<field name="label" description="Descreve a natureza da interação (ex: 'invokes', 'HTTPS request')." />
</edges_definition>
</json_structure>
</input_context>

<task_definition>

<summary>Sua tarefa é analisar o objeto JSON fornecido e produzir um relatório completo de modelagem de ameaças.</summary>
<step number="1" description="Interprete a Arquitetura: Analise os 'nodes' e 'edges' para entender os componentes, seus agrupamentos lógicos (usando a propriedade 'parent') e os fluxos de dados." />
<step number="2" description="Infira Limites de Confiança (Trust Boundaries): Identifique os limites de confiança. Um limite é tipicamente cruzado quando um 'edge' conecta 'nodes' com 'parent's diferentes, ou quando um 'edge' conecta um nó do tipo 'actor' (externo) a um nó dentro de um container do sistema." />
<step number="3" description="Realize a Análise STRIDE: Execute uma análise de ameaças completa usando a metodologia STRIDE, detalhando ameaças, componentes afetados, explicações e mitigações para cada categoria." />
</task_definition>

<output_format>
<description>O resultado final deve ser um relatório em formato Markdown, seguindo estritamente o template abaixo.</description>
<template type="markdown">

<![CDATA[ # Relatório de Análise de Ameaças - Metodologia STRIDE

          ## Análise da Arquitetura
          **(Descreva brevemente os componentes, contêineres e fluxos de dados que você interpretou a partir dos arrays `nodes` e `edges`. Destaque os principais limites de confiança inferidos.)**

          ---

          ## Análise STRIDE

          ### S - Spoofing (Falsificação de Identidade)
          * **Ameaça:** (Descreva a ameaça de falsificação. Ex: "Um ator não autenticado se passando pelo 'User' para acessar o 'API Gateway'.")
          * **Componentes/Fluxos Afetados:** (Liste os `labels` dos `nodes` ou descreva os `edges` relevantes.)
          * **Explicação:** (Detalhe como a ameaça pode ocorrer nesta arquitetura, com base nos fluxos de dados.)
          * **Mitigação Sugerida:** (Sugira soluções como autenticação forte, mTLS, verificação de certificados, etc.)

          ### T - Tampering (Adulteração de Dados)
          * **Ameaça:** (Descreva a ameaça de adulteração. Ex: "Alteração de dados em trânsito entre 'API Gateway' e 'Logic Apps'.")
          * **Componentes/Fluxos Afetados:** (Liste os `edges` e os `nodes` de armazenamento de dados.)
          * **Explicação:** (Detalhe como os dados podem ser alterados, fazendo referência aos `edges` vulneráveis.)
          * **Mitigação Sugerida:** (Sugira soluções como HTTPS/TLS em todos os `edges`, assinaturas digitais, checksums, controle de integridade.)

          ### R - Repudiation (Repúdio)
          * **Ameaça:** (Descreva a ameaça de repúdio. Ex: "Um usuário nega ter invocado uma ação crítica através do 'Logic Apps'.")
          * **Componentes/Fluxos Afetados:** (Liste os `nodes` que executam ações críticas.)
          * **Explicação:** (Detalhe como um ator poderia negar ter realizado uma ação e a falta de provas.)
          * **Mitigação Sugerida:** (Sugira soluções como logs de auditoria detalhados e seguros para cada transação, assinaturas digitais.)

          ### I - Information Disclosure (Divulgação de Informação)
          * **Ameaça:** (Descreva a ameaça de vazamento de dados. Ex: "Exposição de dados sensíveis do 'SaaS Services' devido a logs excessivamente detalhados.")
          * **Componentes/Fluxos Afetados:** (Liste os `nodes` que armazenam/transmitem dados sensíveis e os `edges` correspondentes.)
          * **Explicação:** (Detalhe como os dados sensíveis podem ser expostos, seja em trânsito, em repouso ou em logs.)
          * **Mitigação Sugerida:** (Sugira soluções como criptografia em trânsito e em repouso, controle de acesso granular, tratamento seguro de erros.)

          ### D - Denial of Service (Negação de Serviço)
          * **Ameaça:** (Descreva a ameaça de negação de serviço. Ex: "Sobrecarga do 'API Gateway' com um volume massivo de requisições.")
          * **Componentes/Fluxos Afetados:** (Identifique pontos de entrada e componentes críticos como `nodes` de `type` 'gateway'.)
          * **Explicação:** (Detalhe como um serviço pode ser tornado indisponível ao explorar um componente específico.)
          * **Mitigação Sugerida:** (Sugira soluções como load balancers, auto-scaling, rate limiting, WAF nos pontos de entrada.)

          ### E - Elevation of Privilege (Elevação de Privilégio)
          * **Ameaça:** (Descreva a ameaça de elevação de privilégio. Ex: "Uma vulnerabilidade no 'Logic Apps' permite executar ações nos 'Azure Services' com permissões não autorizadas.")
          * **Componentes/Fluxos Afetados:** (Liste os `nodes` que gerenciam autorização ou que interagem com múltiplos componentes de backend.)
          * **Explicação:** (Detalhe como um ator com poucos privilégios poderia obter mais acesso, explorando uma falha de autorização entre dois `nodes`.)
          * **Mitigação Sugerida:** (Sugira soluções como o Princípio do Menor Privilégio para as identidades de serviço, validação de permissões em cada chamada interna.)
        ]]>

    </template>

</output_format>

<final_instruction>
Analise o objeto JSON fornecido a seguir e gere o relatório completo de análise de ameaças.
</final_instruction>
