import streamlit as st
import pandas as pd

SHEET_ID = "1M6QdiL5_yxzaFyg37cPcq71oH8p1i2dponkqtbyoCgg"
SHEET_NAME = "Página1"

url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&sheet={SHEET_NAME}"

@st.cache_data
def carregar_dados():
    return pd.read_csv(url, encoding="utf-8")

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

