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
st.title("🔍 Autorização - ON THE JOB")

numero = st.text_input("Digite o número pessoal (N.P.):")

if numero:
    st.cache_data.clear()  # 🔄 Limpa o cache ao buscar
    df = carregar_dados()  # 🔁 Recarrega os dados atualizados

    try:
        numero_int = int(numero)
        resultado = df[df["N.P."] == numero_int]
        if not resultado.empty:
            st.success("Operador encontrado:")
            for _, row in resultado.iterrows():
                nome_completo = str(row['Nome']).strip()
                partes = nome_completo.split()
                primeiro_nome = partes[0]
                sobrenomes_censurados = ' '.join(['*******'] * (len(partes) - 1))
                nome_censurado = f"{primeiro_nome} {sobrenomes_censurados}" if sobrenomes_censurados else primeiro_nome

                st.markdown(f"""
                **🆔 N.P.:** {row['N.P.']}  
                **👤 Nome:** {nome_censurado}  
                **📅 Data de admissão:** {row['Data de admissão']}  
                **🛠️ Máquinas autorizadas:** {row['Máquinas autorizadas']}  
                **👥 Subgrupo de empregados:** {row['Subgrupo de empregados']}
                """)
        else:
            st.warning("Nenhum operador encontrado com esse número.")
    except ValueError:
        st.error("Por favor, digite apenas números válidos.")
