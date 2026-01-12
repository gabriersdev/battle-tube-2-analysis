# Análise de Clips - Battle Tube 2

Este projeto realiza uma análise de dados sobre clips extraídos das plataformas Twitch e Kick, referentes ao ano de 2025. O foco é entender o comportamento da audiência durante o período.

## Tecnologias Usadas

- Python: Linguagem de programação utilizada.
- Pandas: Biblioteca para leitura, limpeza e manipulação dos dados.
- Matplotlib e Seaborn: Bibliotecas utilizadas para a criação de gráficos e visualização de dados.
- Pendulum: Biblioteca para tratamento e conversão de datas e horários.
- Jupyter Notebook: Ambiente interativo onde a análise foi desenvolvida.

## Como Funciona

O projeto utiliza arquivos JSON armazenados na pasta de dados, que contêm as informações brutas dos clips (como título, criador, número de visualizações e data de criação).

O notebook principal (`Main.ipynb`) executa o seguinte fluxo:
1. Carregamento de Dados: Lê os arquivos da Twitch (obtidos via scraping) e da Kick (obtidos manualmente) e os combina em uma única tabela.
2. Tratamento: Converte as datas para o fuso horário de Brasília e trata valores ausentes.
3. Análise: Calcula métricas como os dias com mais clips, os criadores mais ativos (clippers), os horários de pico e os clips mais assistidos.
4. Visualização: Gera gráficos que mostram a evolução das visualizações, a distribuição de clips por dia da semana e horário, e comparações entre períodos de eventos (como a Subathon) e períodos normais.

## Objetivo

O objetivo é fornecer uma visão geral sobre o engajamento da comunidade e identificar padrões de criação e consumo de conteúdo curto (clips) relacionados ao projeto.