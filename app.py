import streamlit as st
import pandas as pd
import requests
from io import StringIO

# 🔗 ID da planilha e nome da aba
SHEET_ID = "1M6QdiL5_yxzaFyg37cPcq71oH8p1i2dponkqtbyoCgg"
SHEET_NAME = "Página1"
url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/export?format=csv&sheet={SHEET_NAME}"

# 📥 Função para carregar os dados da planilha
def carregar_dados():
    response = requests.get(url)
    response.encoding = 'utf-8'
    csv_data = StringIO(response.text)
    df = pd.read_csv(csv_data)
    df.columns = df.columns.str.strip()
    df.columns = df.columns.str.replace('\ufeff', '')  # Remove BOM invisível
    return df

# 🧭 Interface do app
st.set_page_config(page_title="Consulta de Operadores", layout="centered")
st.markdown("<h2 style='text-align: center;'>🔍 Consulta de Operadores</h2>", unsafe_allow_html=True)

numero = st.text_input("Digite o número pessoal (N.P.):")

if numero:
    st.cache_data.clear()  # 🔄 Limpa o cache ao buscar
    df = carregar_dados()  # 🔁 Recarrega os dados atualizados

    try:
        numero_int = int(numero)
        resultado = df[df["N.P."] == numero_int]
        if not resultado.empty:
            for _, row in resultado.iterrows():
                st.markdown(f"""
                <div style="background-color:#f9f9f9; padding:20px; border-radius:10px; box-shadow:0 2px 6px rgba(0,0,0,0.1); margin-bottom:20px;">
                    <p><strong>🆔 N.P.:</strong> {row['N.P.']}</p>
                    <p><strong>👤 Nome:</strong> {row['Nome']}</p>
                    <p><strong>📅 Data de admissão:</strong> {row['Data de admissão']}</p>
                    <p><strong>🛠️ Máquinas autorizadas:</strong> {row['Máquinas autorizadas']}</p>
                    <p><strong>👥 Subgrupo de empregados:</strong> {row['Subgrupo de empregados']}</p>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("Nenhum operador encontrado com esse número.")
    except ValueError:
        st.error("Por favor, digite apenas números válidos.")
