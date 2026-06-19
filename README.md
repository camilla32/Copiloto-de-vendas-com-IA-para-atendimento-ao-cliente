# 🤖 FYS Scout AI 📍
> **Todo sabor. Menos pressão.** — Sistema Inteligente de Prospecção e Análise de Mercado para o Portfólio FYS (Grupo HEINEKEN).

O **FYS Scout AI** é uma plataforma web inteligente desenvolvida para otimizar, qualificar e automatizar a prospecção comercial dos refrigerantes da marca **FYS** no segmento de panificação (padarias) na região de São Paulo. 

O sistema consome dados brutos de mercado, aplica inteligência de negócios para calcular o fit comercial de cada estabelecimento (*Score FYS*) e direciona as ações tanto da equipe de vendas de rua quanto da diretoria executiva.

---

## 🏗️ Arquitetura e Abas do Sistema

O ecossistema da aplicação foi desenhado de forma modular em formato *Single Page Application* (SPA). A navegação é dividida em 4 abas estratégicas:

<table>
  <tr>
    <td width="50%" valign="top">
      <strong>🤖 1. Agente Ativo</strong><br>
      Interface conversacional simulada que atua na ponta da prospecção. A IA analisa instantaneamente as variáveis da padaria selecionada (como o histórico de marcas parceiras) e gera uma abordagem de vendas personalizada. Possui gatilhos rápidos para envio de mensagens via WhatsApp, E-mail e opção de transbordo para um consultor humano.
    </td>
    <td width="50%" valign="top">
      <strong>📊 2. Dashboard Comercial</strong><br>
      Painel analítico focado em inteligência de mercado macro. Consolida indicadores-chave de performance (KPIs) em tempo real, como o volume total de leads mapeados, média geral de aderência e gráficos fluidos (construídos em CSS puro) que demonstram a dominância de sabores sugeridos na base.
    </td>
  </tr>
  <tr>
    <td width="50%" valign="top">
      <strong>🎯 3. Radar de Oportunidades</strong><br>
      O coração do funil de vendas (*pipeline*) para a equipe de rua. Apresenta os clientes em formato de <em>Cards Inteligentes</em> organizados de forma decrescente pelo Score FYS. Os estabelecimentos com maior potencial (Score > 90) recebem destaque visual imediato para priorização de visitas.
    </td>
    <td width="50%" valign="top">
      <strong>📄 4. Relatório Executivo</strong><br>
      Módulo focado em auditoria, conformidade e apresentações gerenciais. Apresenta um sumário descritivo cruzando fluxo de clientes com potencial de conversão, volumetria demográfica dividida pelas Zonas de São Paulo e uma tabela de dados integral com os registros tratados, otimizada nativamente para impressão em PDF.
    </td>
  </tr>
</table>

---

## 📈 Inteligência de Dados (`padarias_sp.csv`)

O motor de recomendações e regras de negócio do sistema foi baseado na análise detalhada do arquivo de dados das padarias:

* **Predominância do Sabor Guaraná:** O algoritmo identificou que **66.6%** (10 de 15) das padarias mapeadas possuem o fit ideal para a introdução do *Guaraná da Amazônia FYS*, impulsionado pelo forte fluxo de consumo no período da tarde.
* **Correlação de Fluxo x Score:** Estabelecimentos com fluxo de clientes massivo (como a *Padaria Ponto Certo* com 950 clientes/dia e a *Padaria Imperial* com 880 clientes/dia) foram classificados com os maiores níveis de oportunidade (Scores 93 e 91, respectivamente).

---

## 🛠️ Tecnologias e Padrões Aplicados

* **HTML5 & CSS3:** Arquitetura semântica com layout responsivo baseado em *CSS Grid* e *Flexbox*. Visual construído em *Dark Mode* premium, utilizando a paleta de cores da marca FYS (tons de verde profundo, dourado/bronze e branco).
* **JavaScript Nativo (Vanilla JS):** Desenvolvimento focado em alta performance e zero dependências externas. A alternância entre as abas e a renderização dos dados ocorrem de forma instantânea no navegador.
* **Componentização Visual:** Uso de efeitos de transição dinâmica (*Hover Effects*) e cartões interativos para melhorar a experiência do usuário (UI/UX).
* CHATGPT.
*  GEMINI.

---


# 👩‍💻 Autora

**Camila Silva dos Santos**

Graduada em Ciências Econômicas, com interesse nas áreas de Dados, Business Intelligence, Processos, Tecnologia, Inteligência Artificial e Melhoria Contínua.




