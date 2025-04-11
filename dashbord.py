import streamlit as st
import pandas as pd
import plotly.express as px

# Carregar dados
st.title("Dashboard Interativo: Doença Cardíaca")
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/kb22/Heart-Disease-Prediction/master/dataset.csv"
    df = pd.read_csv(url)
    return df

df = load_data()

#Filtros
st.sidebar.header("Filtros")
sex_filter = st.sidebar.selectbox("Sexo", options=["Todos", "Masculino", "Feminino"])
age_range = st.sidebar.slider("Faixa etária", int(df.age.min()), int(df.age.max()), (40, 60))

# Aplicar
filtered_df = df[(df.age >= age_range[0]) & (df.age <= age_range[1])]
if sex_filter != "Todos":
    filtered_df = filtered_df[filtered_df.sex == (1 if sex_filter == "Masculino" else 0)]

#idade
st.subheader("Distribuição de Idade")
fig_age = px.histogram(filtered_df, x="age", nbins=20, title="Histograma de Idade")
st.plotly_chart(fig_age)

#Relação idade pressão
st.subheader("Idade vs Pressão Arterial")
fig_bp = px.scatter(filtered_df, x="age", y="trestbps", color="target",
                    labels={"target": "Tem doença cardíaca"}, title="Idade x Pressão Sistólica")
st.plotly_chart(fig_bp)

# Mapa das correlações
st.subheader("Mapa de Calor de Correlações")
corr = filtered_df.corr(numeric_only=True)
fig_heatmap = px.imshow(corr, text_auto=True, title="Correlação entre Variáveis")
st.plotly_chart(fig_heatmap)

# Footer
st.markdown("Desenvolvido por [Seu Nome] | Dados: UCI Repository")
