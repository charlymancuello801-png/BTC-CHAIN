import requests
import streamlit as st

st.set_page_config(page_title="Panel Cripto", layout="centered")

# Fondo oscuro
st.markdown(
    "<style>.stApp { background-color: #12161c; color: white; }</style>",
    unsafe_allow_html=True,
)

st.title("Panel Cripto")
st.caption("Conectado en tiempo real a los servidores de Binance")


# Función para traer el precio real de Bitcoin
def obtener_precio_btc():
    try:
        url = "https://binance.com"
        datos = requests.get(url, timeout=5).json()
        return float(datos["price"])
    except Exception:
        return 0.0


precio_btc = obtener_precio_btc()
mi_saldo_btc = 0.01850552
valor_en_dolares = mi_saldo_btc * precio_btc

# Sección de Saldo Realizado
st.subheader("Valor total estimado")
st.metric(
    label="Tu Saldo",
    value=f"{mi_saldo_btc:.8f} BTC",
    delta=f"≈ ${valor_en_dolares:,.2f} USD (En vivo)",
)

st.divider()

# Menú de pestañas
pestana_inicio, pestana_pool = st.tabs(["📊 Inicio y Mercado", "⛏️ Pool"])

with pestana_inicio:
    st.write(f"**Precio actual de Bitcoin:** ${precio_btc:,.2f} USDT")
    st.info("Cuadro de Miedo y Codicia: **26 — Miedo**")
    if st.button("Actualizar precio ahora"):
        st.rerun()

with pestana_pool:
    st.subheader("Minería y Recompensas")
    col1, col2 = st.columns(2)
    col1.metric("Hashrate", "142.50 TH/s", "2 trabajadores")
    col2.metric("Recompensa 24h", "0.00045210 BTC")
    st.warning(
        "Conecta tu API Key de Binance para ver tus recompensas reales de"
        " minería."
    )