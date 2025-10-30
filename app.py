import streamlit as st
import pandas as pd
import requests
from io import StringIO

# ID da planilha e nome da aba
SHEET_ID = "1M6QdiL5_yxzaFyg37cPcq71oH8p1i2dponkqtbyoCgg"
SHEET_NAME = "Página1"

# URL de exportação como CSV
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&sheet={SHEET_NAME}"

@st.cache_data
def carregar_dados():
    response = requests.get(url)
    response.encoding = 'utf-8'
    csv_data = StringIO(response.text)
    return pd.read_csv(csv_data)

df = carregar_dados()

st.title("🔍 Consulta de Operadores")

numero = st.text_input("Digite o número pessoal (N.P.):")

if numero:
    try:
        numero_int = int(numero)
        resultado = df[df["N.P."] == numero_int]
        if not resultado.empty:
            st.success("Operador encontrado:")
            st.dataframe(resultado)
        else:
            st.warning("Nenhum operador encontrado com esse número.")
    except ValueError:
        st.error("Por favor, digite apenas números válidos.")
