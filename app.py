import streamlit as st
import requests
import base64
from datetime import datetime, timedelta

st.title("Visualizar DJE do TJRR")

# Função para encontrar o DJE mais recente disponível
def find_latest_dje(start_date, max_days=30):
    current = start_date
    for _ in range(max_days):
        date_str = current.strftime("%Y%m%d")
        url = f"https://diario.tjrr.jus.br/dpj/dpj-{date_str}.pdf"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                return current, response
        except requests.exceptions.RequestException:
            pass
        current -= timedelta(days=1)
    return None, None

# Opções de busca
option = st.radio(
    "Escolha a opção de busca:",
    ("Dia atual", "Mais recente disponível", "Selecionar data específica")
)

selected_date = None
response = None

if option == "Dia atual":
    selected_date = datetime.now()
elif option == "Mais recente disponível":
    st.write("Buscando o DJE mais recente disponível...")
    selected_date, response = find_latest_dje(datetime.now())
    if selected_date is None:
        st.error("Nenhum DJE encontrado nos últimos 30 dias.")
elif option == "Selecionar data específica":
    selected_date = st.date_input("Selecione a data:", value=datetime.now(), max_value=datetime.now())
    selected_date = datetime.combine(selected_date, datetime.min.time())  # converter para datetime

if selected_date:
    date_str = selected_date.strftime("%Y%m%d")
    date_display = selected_date.strftime("%d/%m/%Y")
    
    if response is None:  # se não foi obtido na busca mais recente
        st.write(f"Buscando DJE para a data: {date_display}")
        url = f"https://diario.tjrr.jus.br/dpj/dpj-{date_str}.pdf"
        try:
            response = requests.get(url, timeout=10)
        except requests.exceptions.RequestException as e:
            st.error(f"Erro ao acessar o site: {e}")
            response = None
    
    if response and response.status_code == 200:
        st.success(f"DJE encontrado para {date_display}!")
        
        # Botão para download
        st.download_button(
            label="Baixar DJE",
            data=response.content,
            file_name=f"DJE_{date_str}.pdf",
            mime="application/pdf",
            key="download_pdf"
        )
        
        # Visualizar o PDF inline usando iframe
        pdf_base64 = base64.b64encode(response.content).decode('utf-8')
        pdf_display = f'<iframe src="data:application/pdf;base64,{pdf_base64}" width="100%" height="600" type="application/pdf"></iframe>'
        st.components.v1.html(pdf_display, height=600)
        
    elif response:
        st.error(f"DJE não disponível para a data {date_display}. Status: {response.status_code}")
    else:
        st.error("Não foi possível obter o DJE.")