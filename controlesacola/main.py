from asyncore import write
import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout = 'wide')

st.sidebar.header("Menu")
pagina =  st.sidebar.radio('',['','Atualizar','Analisar'])

#pagina em que o usuario envia dados para o servidor
if pagina == 'Atualizar':
    st.markdown("# EM MANUNTENÇÃO")
    st.markdown('''
                Em breve essa parte será acessivel.
                ''')

#pagina inicial
if pagina == '':
    st.markdown('''
                ## Selecione na barra ao lado o que deseja.
                ''')

#pagina de analise de dados

if pagina == 'Analisar':
    df = pd.read_csv('dados.csv')
    
    c1,c3,c2 = st.columns([1,0.1,1])
    with c1:
        lista_Os=df.OS.unique()
        cx_os = st.selectbox("Selecione uma OS",lista_Os)    
        df_os = df[df["OS"] == cx_os]
   
        df_total = df_os[df_os['Status'] == "total"]
    
        marca_titlo = df_total.Marca.unique()
        cx_marca = st.selectbox('Selecione uma marca', marca_titlo)
        df_total_marca = df_total[df['Marca'] == cx_marca]
    
        tamanho_lista = df_total_marca.Tamanho.unique()
        cx_tamanho = st.selectbox("Selecione um tamanho", tamanho_lista)
        df_total_marca_tamanho = df_total_marca[df_total_marca['Tamanho'] == cx_tamanho]
    
        cor_lista = df_total_marca_tamanho.Cor.unique()
        cx_cor = st.selectbox("Selecione uma cor", cor_lista)
        df_total_marca_tamanho_cor = df_total_marca_tamanho[df_total_marca_tamanho["Cor"] == cx_cor]
    
    #analisando pra saber quandas sacolas foram devolvidas
    df_base = df[df['OS'] == cx_os]
    df_base_marca = df_base[df_base["Marca"] == cx_marca]
    df_base_marca_tamanho = df_base_marca[df_base_marca['Tamanho'] == cx_tamanho]
    df_base_marca_tamanho_cor = df_base_marca_tamanho[df_base_marca_tamanho["Cor"] == cx_cor]
    df_pegou = df_base_marca_tamanho_cor[df_base_marca_tamanho_cor["Status"] == 'entregou']
    
    soma = df_pegou.copy()
    soma['Colador'] = "Idez"
    total_entregue = soma.Quantidade.sum()
    juncao = soma.groupby(["OS","Tamanho","Status"]).sum().reset_index()   
    
    novo = pd.concat([df_total_marca_tamanho_cor, juncao])
    
    with c2:
        fig_inicial = px.bar(novo, x = "Tamanho",y = "Quantidade",color='Status',
                        barmode='group', height=400, width=400, 
                        text_auto=True, 
                        title=f"Sacolas {cx_marca.upper()} {cx_tamanho} {cx_cor.upper()}")
  
        st.plotly_chart(fig_inicial)

    cx_colador = st.checkbox("Monstrar coladores")
    
    if cx_colador == True:
        dropidez = df_base_marca_tamanho_cor[df_base_marca_tamanho_cor["Status"] != "total"]
        coladores = dropidez.groupby(["Colador","Marca","Tamanho","Cor","OS","Status"]).sum().reset_index()
        coladores_pegou = coladores[coladores["Status"] == "pegou"]
        coladores_entregou = coladores[coladores["Status"] == "entregou"]
        
        novo_coladores = pd.concat([coladores_pegou, coladores_entregou])
        
        fig_final = px.bar(novo_coladores, x = "Colador", y="Quantidade",
                           color="Status", text_auto=True,
                           barmode="group", height=400, width=800)
        st.plotly_chart(fig_final)

    cx_coladores_geral = st.checkbox("Status geral Sacolas")
    if cx_coladores_geral == False:
        st.write("Esses status são referente ao quadro geral de quem pegou ou entregou sacola.")
        st.write("O TOTAL somando todos os modelos!")
    
    if cx_coladores_geral == True:
        lista_os2 = df.OS.unique()
        
        cx=st.selectbox("Selecione uma ORDEM de SERVIÇO",lista_os2)
        
        df_geral = df[df["OS"] == cx]
        
        novo_df = df_geral[df_geral["Status"] != "total"]
        
        grafico = novo_df.groupby(["Colador","Status"]).sum().reset_index()
        grafico_pegou = grafico[grafico["Status"] == "pegou"]
        grafico_entregou = grafico[grafico["Status"] == "entregou"]
        grafico_atual = pd.concat([grafico_pegou,grafico_entregou])
        
        
        figura_geral = px.bar(grafico_atual, x="Colador",height=400,width=800,
                              y="Quantidade", color="Status",barmode='group',
                              text_auto=True,)
        st.plotly_chart(figura_geral)
        
        