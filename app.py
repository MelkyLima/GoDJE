import streamlit as st
import requests
from datetime import datetime, timedelta

# CSS para cards modernos e layout
card_style = """
<style>
body {
    margin: 0;
    padding: 0;
    background: #0f172a;
    color: #f8fafc;
}
.card {
    border: none;
    border-radius: 20px;
    padding: 28px;
    margin: 16px 0;
    box-shadow: 0 16px 40px rgba(15, 23, 42, 0.35);
}
.card-title {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    text-align: center;
    font-size: 2rem;
    font-weight: 800;
}
.card-blue {
    background: linear-gradient(135deg, #1d4ed8 0%, #3b82f6 100%);
    color: white;
}
.card-green {
    background: linear-gradient(135deg, #047857 0%, #10b981 100%);
    color: white;
}
.card * {
    color: inherit;
}
.link-button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    background: #f97316;
    color: white;
    padding: 0.75rem 1.4rem;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 700;
    margin-top: 1rem;
}
.link-button:hover {
    opacity: 0.95;
}
</style>
"""
st.markdown(card_style, unsafe_allow_html=True)

# Card 1: Título
st.markdown('<div class="card card-title">📄 Visualizar DJE do TJRR</div>', unsafe_allow_html=True)

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

# Card 2: DJE Disponível Automaticamente
st.markdown('<div class="card card-blue">', unsafe_allow_html=True)
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
    date_display = selected_date.strftime('%d/%m/%Y') if selected_date else ''
    st.markdown(
        f'<a class="link-button" href="{url}" target="_blank">VISUALIZAR DJE {date_display}</a>',
        unsafe_allow_html=True,
    )

st.markdown('</div>', unsafe_allow_html=True)

# Card 3: Buscar Data Específica
st.markdown('<div class="card card-green">', unsafe_allow_html=True)
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
    date_display_specific = selected_specific.strftime('%d/%m/%Y')
    st.success(f"✅ DJE disponível para {date_display_specific}.")
    st.markdown(
        f'<a class="link-button" href="{url_specific}" target="_blank">VISUALIZAR DJE {date_display_specific}</a>',
        unsafe_allow_html=True,
    )
else:
    st.error(f"❌ DJE não disponível para {selected_specific.strftime('%d/%m/%Y')}.")

st.markdown('</div>', unsafe_allow_html=True)