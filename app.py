import streamlit as st
import pandas as pd
import gspread

# Conecta ao Google Sheets sem autenticação privada
gc = gspread.public()

# Abre a planilha pelo ID
SHEET_ID = "1M6QdiL5_yxzaFyg37cPcq71oH8p1i2dponkqtbyoCgg"
sh = gc.open_by_key(SHEET_ID)

# Nome da aba
worksheet = sh.worksheet("Página1")

# Pega os dados como lista de listas
data = worksheet.get_all_values()

# Converte para DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

st.title("🔍 Consulta de Operadores")

numero = st.text_input("Digite o número pessoal:")

if numero:
    resultado = df[df["Número Pessoal"].astype(str) == numero]
    if not resultado.empty:
        st.success("Operador encontrado:")
        st.dataframe(resultado)
    else:
        st.warning("Nenhum operador encontrado com esse número.")
