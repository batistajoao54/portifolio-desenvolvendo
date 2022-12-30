import pandas as pd
import streamlit as st
import csv


def cadrastar_colador():
    coluna1,coluna2 = st.columns([1,1])
    df_os = pd.read_excel('02-dados_os.xlsx')
    with coluna1:
        lista_colador = df_os['MARCA'].unique() #fazendo seleçao unica de marcas
        marca_seletor = st.selectbox("MARCA", lista_colador)
    df_marca = df_os[df_os['MARCA'] == marca_seletor] #selecionando uma marca
    lista_os = df_marca['OS'].unique() #filtando as os dessa marca

    with coluna2:
        os_seletor = st.selectbox("OS",lista_os) #selecionando a os
    
    df_os_final = df_os[df_os['OS'] == os_seletor] #criando uma tabela so com a seleção
    cor = df_os_final.iloc[0,6] #coletando dados de descriçoes
    tamanho_final = df_os_final.iloc[0,5] #coletando dados de tamanho
    st.write('')
    st.write('# *ESCREVER TUDO MAIUSCULO E SEM ACENTO*')

    c1,c2,c3,c4,c5,c6,c7 = st.columns([1.2,1.2,1.4,2.2,2.2,1.5,2.2])
    with c1:
        data_dia = st.number_input('DIA',min_value=1,max_value=31)
    with c2:
        data_mes = st.number_input('MES',min_value=1,max_value=12)
    with c3:
        data_ano = st.number_input('ANO',min_value=2022)
    with c4:
        data_os = st.selectbox('OS',[os_seletor, 'OS'])
    with c5:
        data_marca = st.selectbox('MARCA',[marca_seletor,"MARCA"])
    with c6:
        data_tamanho = st.selectbox('TAMANHO', [tamanho_final,'P','PP','P2','M','M2','G','< >'])
    with c7:
        data_cor = st.selectbox('COR',[cor,"cor"])

    c8,c9,c10,c11 = st.columns([1,1,1,1])
    with c9:
        data_colador = st.text_input('COLADOR')
    with c8: 
        df = pd.read_excel('03-entrada e saida.xlsx')
        botao_nome = st.checkbox("NOMES USADOS")
        nomes = list(df['COLADOR'].unique())
        if botao_nome == True:
            st.write(nomes)
    
    with c10:
           data_quantidade = st.number_input('QUANTIDADE',min_value=1)
    with c11:
        data_status = st.selectbox('STATUS',['ENVIADO','RECEBIDO',])

    botao_atualizar = st.button('SALVAR')
    
    if botao_atualizar == True:
        lista_cadrastro = [data_dia,data_mes,data_ano,data_os.strip(),data_marca.strip(),data_tamanho,data_cor.strip(),data_colador.strip(),data_quantidade,data_status,'N']
        cabecalho = ['DIA','MES','ANO','OS','MARCA','TAMANHO','COR','COLADOR','QUANTIDADE','STATUS','PAGO']
        
        with open("memoria.csv","w", newline="") as file:
            writer = csv.writer(file, delimiter=",")
            writer.writerow(cabecalho)
            writer.writerow(lista_cadrastro)
        
        df_memoria = pd.read_csv('memoria.csv')
        df_final = pd.concat([df,df_memoria])
        df_final= df_final.drop_duplicates() #eliminando duplicatas
        df_final.to_excel('03-entrada e saida.xlsx',index=False)

    c12,c13,c14 = st.columns([1,2,2])
    df_visualizacao = pd.read_excel('03-entrada e saida.xlsx')
    st.write("ULTIMOS REGISTRADOS")
    with c12:
        quantidade_dados = st.selectbox('',[3,5,4,2,1,10,15,20,30,40,50,100,200])
    st.table(df_visualizacao.tail(int(quantidade_dados)))


if "__main__" == __name__:
    cadrastar_colador()
