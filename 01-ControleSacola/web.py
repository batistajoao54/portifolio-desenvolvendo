import streamlit as st
import plotly.exceptions as px

import cadrastar_os
import cadrastar_colador
import cadrastar_analise


#tem q resolver a problematica da comunicação entre os arquivos
#ou transformar tudo em um só aquivo

st.set_page_config(layout='wide') #configura a pagina

escolha = st.selectbox("OPÇÕES",['Visualizar os dados','Cadrastar os','Cadrastar colador'])

if escolha == "Cadrastar os":
    paginaos = cadrastar_os.cadrastro_os()

if escolha == "Cadrastar colador":
    paginacolador = cadrastar_colador.cadrastar_colador()

if escolha == "Visualizar os dados":
    analise = cadrastar_analise.analise()

