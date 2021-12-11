import streamlit as st
from db_conn import *
import pandas as pd

def app():
    paginas = st.sidebar.selectbox("Página",
                                   ("Entradas",
                                    "Lugares Livres",
                                    "Registos",
                                    "Saídas"))


    if paginas == "Entradas":
        entradas()

    if paginas == "Lugares Livres":
        lugareslivres()

    if paginas == "Registos":
        registos()

    if paginas == "Saídas":
        saidas()


def entradas():
    st.title("Parque Estacionamento - Entradas")

    result = query('tb_entradas', [])
    columns = ['id', 'matricula', 'hr_entradas']
    df = pd.DataFrame(result, columns=columns)
    pd.set_option("max_rows", None)

    st.table(df)


def lugareslivres():
    st.title("Parque Estacionamento - Lugares Livres")

    result = query('tb_lugareslivres', [])
    columns = ['lugar', 'livre', 'matricula']
    df = pd.DataFrame(result, columns=columns)
    pd.set_option("max_rows", None)

    st.table(df)


def registos():
    st.title("Parque Estacionamento - Registos")

    result = query('tb_registos', [])
    columns = ['id', 'matricula', 'tempo_total', 'custo']
    df = pd.DataFrame(result, columns=columns)
    pd.set_option("max_rows", None)
    styler = df.style.format({
        "custo": lambda x: float(x)
    })

    st.table(styler)


def saidas():
    st.title("Parque Estacionamento - Saídas")

    result = query('tb_saidas', [])
    columns = ['id', 'hr_saida', 'matricula']
    df = pd.DataFrame(result, columns=columns)
    pd.set_option("max_rows", None)

    st.table(df)


app()
