import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout = 'wide')

dados = st.sidebar.file_uploader("")

pagina = st.sidebar.checkbox('dados carregados')

if pagina == True:
    df = pd.read_csv(dados)
    lista_Os = df.OS.unique()

    #SELECIONADO A OS
    cx_os = st.sidebar.selectbox("Selecione uma OS", lista_Os)
    df_os = df[df["OS"] == cx_os]

    df_total = df_os[df_os['STATUS'] == "TOTAL OS"]

    #SELECIONANDO O TOTAL DE SACOLAS ENVIADAS e recebidas POR OS
    df_base = df[df['OS'] == cx_os]
    df_recebido = df_base[df_base["STATUS"] == 'RECEBIDO']
    df_enviado = df_base[df_base['STATUS'] == 'ENVIADO']

    soma_enviado = df_enviado.copy()

    soma_recebido = df_recebido.copy()

    juncao = soma_enviado.groupby(["OS", "TAMANHO", "STATUS"]).sum().reset_index()
    juncao2 = soma_recebido.groupby(["OS", "TAMANHO", "STATUS"]).sum().reset_index()

    df_total_final = pd.concat([df_total,juncao,juncao2])

    c1,c2 = st.columns([1,1])

    with c1:
        fig_inicial = px.bar(df_total_final, x="OS", y="QUANTIDADE", color='STATUS',
                             barmode='group', height=400, width=400,
                             text_auto=True,
                             title=f"SACOLAS {df_total.iloc[0,4]} {df_total.iloc[0,5]} {df_total.iloc[0,6]}")

        st.plotly_chart(fig_inicial)


    with c2:
        df_dropidez = df_os[df_os['STATUS'] != "TOTAL OS"].copy()
        coladores = df_dropidez.groupby(["COLADOR", "MARCA", "TAMANHO", "COR", "OS", "STATUS"]).sum().reset_index()
        coladores_enviado = coladores[coladores["STATUS"] == "ENVIADO"]
        coladores_recebido = coladores[coladores["STATUS"] == "RECEBIDO"]

        novo_coladores = pd.concat([coladores_enviado, coladores_recebido])

        fig_final = px.bar(novo_coladores, x="COLADOR", y="QUANTIDADE",
                           color="STATUS", text_auto=True,
                           barmode="group", height=400, width=400,
                           title="COLADORES")
        st.plotly_chart(fig_final)

    st.header("Dados gerais de todas as OS ativas")
