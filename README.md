# 🧠 Dashboard Interativo - Doença Cardíaca

## Sobre o Projeto

Esse projeto foi criado pra facilitar a visualização de dados sobre doenças cardíacas usando um dashboard interativo. A ideia é ajudar qualquer pessoa — com ou sem experiência em ciência de dados — a explorar o tema de forma simples e visual.

Escolhi um dataset clássico do UCI chamado **Heart Disease**, que traz informações de pacientes como idade, colesterol, pressão arterial e outros fatores de risco.

---

## Como foi feito

- **Linguagem:** Python  
- **Ferramentas:** [Streamlit](https://streamlit.io/), [Plotly](https://plotly.com/), [Pandas](https://pandas.pydata.org/)

O dashboard foi desenvolvido com foco na interatividade. Dá pra filtrar por sexo e idade, e os gráficos mudam em tempo real. Os dados foram limpos e preparados com Pandas.

---

## O que o dashboard mostra

- 📊 **Histograma de Idades** – mostra a faixa etária mais comum entre os pacientes.
- 🧬 **Dispersão entre Idade e Pressão Arterial** – ajuda a ver se há alguma relação entre esses dois fatores.
- 🔥 **Mapa de Calor das Correlações** – mostra como as variáveis se relacionam entre si.

---

## Conclusão

Com esse painel interativo, ficou bem mais fácil entender como alguns fatores influenciam o risco de doenças cardíacas. É uma forma rápida de visualizar dados que, em tabelas, poderiam passar despercebidos.

---

## Como rodar

Instale os pacotes necessários e execute o app com:

```bash
pip install streamlit plotly pandas
streamlit run dashboard.py
