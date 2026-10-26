
import streamlit as st
from datetime import datetime

st.set_page_config(
    page_title="Football Hub Pro",
    page_icon="⚽",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
.stApp {
    background-color: #0b1220;
    color: #f1f5f9;
}
[data-testid="stMetric"] {
    background-color: #172337;
    padding: 16px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

CAMPIONATI = {
    "Serie A": "ITA",
    "Premier League": "ENG",
    "La Liga": "ESP",
    "Bundesliga": "GER",
    "Ligue 1": "FRA",
    "Champions League": "UCL",
    "Europa League": "UEL",
    "Primeira Liga": "POR",
    "Eredivisie": "NED",
}

st.sidebar.title("⚽ FOOTBALL HUB PRO")
pagina = st.sidebar.radio(
    "Navigazione",
    [
        "Dashboard",
        "Calendario",
        "Gol e Over/Under",
        "Multigol",
        "1X2 e doppia chance",
        "Risultati esatti",
        "Corner",
        "Cartellini",
        "Tiri in porta",
        "Stato aggiornamenti",
    ],
)

st.sidebar.divider()
campionato = st.sidebar.selectbox(
    "Campionato",
    list(CAMPIONATI.keys())
)

st.sidebar.caption("Versione iniziale del progetto")

st.title("⚽ FOOTBALL HUB PRO")
st.caption("Piattaforma di analisi statistica del calcio")

if pagina == "Dashboard":
    st.subheader("Dashboard principale")

    c1, c2, c3 = st.columns(3)
    c1.metric("Campionati configurati", "9")
    c2.metric("Fonte dati", "Da collegare")
    c3.metric("Ultimo aggiornamento", "Non ancora eseguito")

    st.info(
        "La dashboard è stata creata. "
        "I dati reali verranno collegati nel passaggio successivo."
    )

    st.subheader("Campionati disponibili")
    st.dataframe(
        [
            {"Campionato": nome, "Codice": codice}
            for nome, codice in CAMPIONATI.items()
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Calendario":
    st.subheader(f"Calendario — {campionato}")
    st.warning(
        "Il calendario verrà visualizzato dopo il collegamento "
        "alla fonte dati."
    )

elif pagina == "Gol e Over/Under":
    st.subheader("Analisi Gol e Over/Under")
    st.write("Mercati previsti:")
    st.write(
        "Gol, No Gol, Over 1.5, Over 2.5, "
        "Over 3.5, Over 4.5 e relativi Under."
    )
    st.info("In attesa dei dati delle partite.")

elif pagina == "Multigol":
    st.subheader("Analisi Multigol")
    st.write("Fasce previste: 1-2, 1-3, 2-3, 2-4 e 3-5.")
    st.info("Le probabilità saranno calcolate dal motore statistico.")

elif pagina == "1X2 e doppia chance":
    st.subheader("1X2 e doppia chance")
    st.write("Mercati previsti: 1, X, 2, 1X, X2 e 12.")
    st.info("In attesa dei dati necessari per le stime.")

elif pagina == "Risultati esatti":
    st.subheader("Distribuzione dei risultati esatti")
    st.write("Il modello stimerà la probabilità dei diversi punteggi.")
    st.info("Modello statistico non ancora collegato.")

elif pagina == "Corner":
    st.subheader("Calci d'angolo")
    st.write("Linee previste: Over/Under 7.5, 8.5, 9.5, 10.5 e 11.5.")
    st.info("Disponibilità subordinata alla fonte statistica.")

elif pagina == "Cartellini":
    st.subheader("Analisi cartellini")
    st.write("Linee previste: Over/Under 2.5, 3.5, 4.5 e 5.5.")
    st.info("Disponibilità subordinata alla fonte statistica.")

elif pagina == "Tiri in porta":
    st.subheader("Tiri in porta")
    st.write("Analisi del totale partita e delle singole squadre.")
    st.info("I dati saranno mostrati quando disponibili.")

elif pagina == "Stato aggiornamenti":
    st.subheader("Stato del sistema")
    st.write("Stato attuale: configurazione iniziale.")
    st.write("Data e ora di apertura:", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    st.warning(
        "Gli aggiornamenti automatici non sono ancora attivi. "
        "Li configureremo dopo aver collegato le fonti."
    )

st.divider()
st.caption(
    "Football Hub Pro — Le probabilità future saranno stime statistiche, "
    "non garanzie di risultato."
)
