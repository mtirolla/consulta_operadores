import streamlit as st
import pandas as pd

# ID da sua planilha
SHEET_ID = "1M6QdiL5_yxzaFyg37cPcq71oH8p1i2dponkqtbyoCgg"
SHEET_NAME = "Página1"  # Altere se o nome da aba for diferente

# URL para exportar os dados como CSV
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}"

@st.cache_data
def carregar_dados():
    return pd.read_csv(url)

df = carregar_dados()

st.title("🔍 Consulta de Operadores")

numero = st.text_input("Digite o número pessoal:")

if numero:
    resultado = df[df["Número Pessoal"].astype(str) == numero]
    if not resultado.empty:
        st.success("Operador encontrado:")
        st.dataframe(resultado)
    else:
        st.warning("Nenhum operador encontrado com esse número.")
