import streamlit as st
import requests
from datetime import datetime, timedelta

st.title("📄 Visualizar DJE do TJRR")

# Função para verificar se DJE existe (usando HEAD para eficiência)
def check_dje_available(date):
    date_str = date.strftime("%Y%m%d")
    url = f"https://diario.tjrr.jus.br/dpj/dpj-{date_str}.pdf"
    try:
        response = requests.head(url, timeout=5)
        return response.status_code == 200, url
    except requests.exceptions.RequestException:
        return False, url

# Função para encontrar o DJE mais recente disponível
def find_latest_dje(start_date, max_days=30):
    current = start_date
    for _ in range(max_days):
        available, url = check_dje_available(current)
        if available:
            return current, url
        current -= timedelta(days=1)
    return None, None

# CSS para cards modernos
card_style = """
<style>
.card {
    background-color: #ffffff;
    border: 1px solid #e0e0e0;
    border-radius: 10px;
    padding: 20px;
    margin: 10px 0;
    box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# Card 1: DJE Disponível Automaticamente
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📅 DJE Disponível")

# Buscar automaticamente: dia atual ou mais recente
today = datetime.now()
available_today, url_today = check_dje_available(today)

if available_today:
    selected_date = today
    url = url_today
    status_msg = f"✅ DJE do dia atual ({today.strftime('%d/%m/%Y')}) está disponível."
else:
    selected_date, url = find_latest_dje(today)
    if selected_date:
        status_msg = f"ℹ️ DJE do dia atual não disponível. Mostrando o mais recente: {selected_date.strftime('%d/%m/%Y')}."
    else:
        status_msg = "❌ Nenhum DJE encontrado nos últimos 30 dias."

st.write(status_msg)

if url:
    st.link_button("VISUALIZAR DJE", url, type="primary")

st.markdown('</div>', unsafe_allow_html=True)

# Card 2: Buscar Data Específica
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🔍 Buscar Data Específica")

selected_specific = st.date_input(
    "Selecione uma data:",
    value=datetime.now(),
    max_value=datetime.now(),
    format="DD/MM/YYYY"
)
selected_specific_dt = datetime.combine(selected_specific, datetime.min.time())

available_specific, url_specific = check_dje_available(selected_specific_dt)

if available_specific:
    st.success(f"✅ DJE disponível para {selected_specific.strftime('%d/%m/%Y')}.")
    st.link_button("VISUALIZAR DJE", url_specific, type="primary")
else:
    st.error(f"❌ DJE não disponível para {selected_specific.strftime('%d/%m/%Y')}.")

st.markdown('</div>', unsafe_allow_html=True)