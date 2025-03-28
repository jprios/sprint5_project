import streamlit as st
import pandas as pd
import plotly.express as px

# Cabeçalho do aplicativo
st.header('Análise de Dados de Vendas de Carros nos EUA')

# Leitura do conjunto de dados
car_data = pd.read_csv('C:\Users\joaop\projeto-dados\scripts\sprint5_project\vehicles_us.csv')

# Botão para histograma
hist_button = st.button('Criar histograma')

if hist_button:
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Botão para gráfico de dispersão
scatter_button = st.button('Criar gráfico de dispersão')

if scatter_button:
    st.write('Criando um gráfico de dispersão entre preço e odômetro')
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Relação entre Odômetro e Preço")
    st.plotly_chart(fig2, use_container_width=True)

# --- DESAFIO EXTRA: Versão com caixas de seleção ---
st.header('Versão com Caixas de Seleção')

# Caixa de seleção para histograma
build_histogram = st.checkbox('Mostrar histograma da coluna odometer')

if build_histogram:
    st.write('Criando um histograma para a coluna odometer')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# Caixa de seleção para gráfico de dispersão
build_scatter = st.checkbox('Mostrar gráfico de dispersão entre odometer e price')

if build_scatter:
    st.write('Criando gráfico de dispersão entre odometer e price')
    fig2 = px.scatter(car_data, x="odometer", y="price", title="Dispersão: Odômetro x Preço")
    st.plotly_chart(fig2, use_container_width=True)
