# 🤖 FYS Scout AI 📍
> **Todo sabor. Menos pressão.** — Sistema Inteligente de Prospecção e Análise de Mercado para o Portfólio FYS (Grupo HEINEKEN).

Este projeto consiste em uma plataforma web inteligente focada em otimizar e automatizar a prospecção comercial de refrigerantes da marca **FYS** em estabelecimentos de panificação (padarias) na região de São Paulo. O sistema transforma dados brutos de mercado em tomadas de decisão rápidas, dividindo-se entre interações automatizadas de IA e painéis analíticos gerenciais.

---

## 🏗️ Arquitetura das Abas do Sistema

O ecossistema da aplicação foi desenhado de forma modular para cobrir desde a ponta da operação (vendas de rua) até o nível de tomada de decisão executiva (diretoria comercial).

### 🤖 1. Agente Ativo (Interface de Prospecção)
Interface conversacional simulada que atua no primeiro contato com o ponto de venda (PDV).
* **Objetivo:** Automatizar a abordagem de vendas e diminuir o atrito de entrada do produto.
* **Dinâmica:** A IA analisa instantaneamente as variáveis locais da padaria selecionada no arquivo `padarias_sp.csv` e simula uma negociação focada no portfólio que o cliente já consome.
* **Ações Rápidas:** Permite o disparo de abordagens personalizadas via canais como WhatsApp ou E-mail.

### 📊 2. Dashboard Comercial (Painel Macroeconômico)
Painel estatístico focado em dar clareza visual e métricas de desempenho sobre a base mapeada.
* **Objetivo:** Sumarizar KPIs de mercado essenciais em tempo real.
* **Componentes Visuais:** Cartões de métricas rápidas (KPI Cards) indicando o volume total de alvos, médias de Score e gráficos de barras feitos em CSS mapeando a dominância de sabores.

### 🎯 3. Radar de Oportunidades (Triagem e Priorização)
Módulo inteligente que atua como o funil de vendas (*pipeline*) prioritário da equipe comercial.
* **Objetivo:** Ordenar e guiar a força de vendas de rua para focar nas padarias de maior retorno.
* **Dinâmica:** Apresenta os leads qualificados em formato de *Cards Inteligentes* ordenados de forma decrescente pelo **Score FYS**. Os estabelecimentos de topo (Score > 90) ganham destaque visual imediato.

### 📄 4. Relatório Executivo (Auditoria de Cobertura)
Módulo denso de dados e sumário analítico voltado para auditoria e apresentações de diretoria.
* **Objetivo:** Fornecer transparência analítica total sobre a base de dados.
* **Funcionalidades:** Sumário analítico descritivo, volumetria geográfica por zonas de SP e tabela de dados integral com formatação otimizada para impressão em PDF.

---

## 📈 Inteligência de Dados Baseada no Arquivo `padarias_sp.csv`

O motor de recomendações do sistema utiliza parâmetros reais obtidos a partir do cruzamento de dados do mercado de panificação:

1. **Predominância do Sabor Guaraná:** O modelo de IA identificou que **66.6%** (10 de 15) das padarias mapeadas possuem o fit perfeito para receber o *Guaraná da Amazônia FYS*.
2. **Corelação de Fluxo x Score:** Estabelecimentos centrais com fluxos massivos receberam as maiores notas de priorização (Scores acima de 90), qualificando-se como alvos prioritários de expansão.

---

## 🛠️ Tecnologias e Padrões Aplicados

* **HTML5 & CSS3:** Estrutura semântica moderna com sistema de grelhas flexíveis (*CSS Grid* e *Flexbox*) em paleta Dark.
* **JavaScript Nativo (Vanilla JS):** Lógica limpa para alternância de abas de forma instantânea em formato *Single Page Application* (SPA).
* **Design Responsivo:** Componentes adaptáveis para diferentes resoluções com transições visuais fluidas.
