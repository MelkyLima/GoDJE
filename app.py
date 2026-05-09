import streamlit as st
import requests
import base64
from datetime import datetime

st.title("Visualizar DJE do TJRR - Dia Atual")

# Obter a data atual
date = datetime.now()
date_str = date.strftime("%Y%m%d")
date_display = date.strftime("%d/%m/%Y")

st.write(f"Buscando DJE para a data: {date_display}")

# URL do PDF baseado no padrão observado
url = f"https://diario.tjrr.jus.br/dpj/dpj-{date_str}.pdf"

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 200:
        st.success("DJE encontrado!")
        
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
        
    else:
        st.error(f"DJE não disponível para a data {date_display}. Status: {response.status_code}")
        
except requests.exceptions.RequestException as e:
    st.error(f"Erro ao acessar o site: {e}")
except Exception as e:
    st.error(f"Erro inesperado: {e}")