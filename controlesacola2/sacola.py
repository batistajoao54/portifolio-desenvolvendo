import pandas as pd
import plotly.express as px
import streamlit as st
import csv

st.set_page_config(layout='wide')

df =pd.read_csv('entrada e saida.csv')
#df['QUANTIDADE'] = pd.to_numeric(df['QUANTIDADE'])
df_os = pd.read_csv('dados_os.csv')
#df_os['QUANTIDADE'] = pd.to_numeric(df_os['QUANTIDADE'])

pagina = st.sidebar.radio('',['ATUALIZAR', 'ANALISAR'])

if pagina == "ATUALIZAR":
    
    os_cadrasto = st.checkbox("CADRASTAR OS") #criando um widg para definio o q fazer
    
    if os_cadrasto == True: # iniciando os afazeres
        c1,c2,c3,c4,c5,c6,c7 = st.columns([1,1,1.2,2.5,2.5,1.5,2.5]) #criando colunas para separar a tela
        with c1:
            data_dia = st.text_input('DIA')
        with c2:
            data_mes = st.text_input('MES')
        with c3:
            data_ano = st.text_input('ANO')
        with c4:
            data_os = st.text_input('OS')
        with c5:
            data_marca = st.text_input('MARCA')
        with c6:
            data_tamanho = st.selectbox('TAMANHO', ['P','P2','M','M2','G','< >'])
        with c7:
            data_cor = st.text_input('COR')
                
        c8,c9,c10 = st.columns([1,1,1])
        with c8:
            data_colador = st.selectbox('COLADOR',['IDEZ'])
        with c9:
            data_quantidade = st.text_input('QUANTIDADE')
        with c10:
            data_status = st.selectbox('STATUS',['TOTAL OS'])
        
        lista_cadrastro = [data_dia,data_mes,data_ano,data_os,data_marca,data_tamanho,data_cor,data_colador,data_quantidade,data_status] #uma lista com todos os inputs coletados
        
        botao_atualizar = st.button('SALVAR') #criando um botao 
        if botao_atualizar == True: #ativando o botao
            cabecalho = ['DIA','MES','ANO','OS','MARCA','TAMANHO','COR','COLADOR','QUANTIDADE','STATUS']
            #print(lista)
            with open("memoria.csv","w", newline="") as file: #escrevendo um aquivo memoria com os dados coletados
                writer = csv.writer(file, delimiter=",")
                writer.writerow(cabecalho)
                writer.writerow(lista_cadrastro)
            
            df_memoria = pd.read_csv('memoria.csv') #lendo os aquivos recem craiado
            df_final = pd.concat([df_os,df_memoria]) #juntando os aquivos antigos junto com os recem criado
            df_final.to_csv('dados_os.csv',index=False) #salvando os dados
        
        c11,c12,c13 = st.columns([1,2,2])
        df_visualizacao = pd.read_csv('dados_os.csv') #relendo os arquivos agora atualizado com os dados novos
        st.write("ULTIMOS DADOS REGISTRADOS")
        with c11:
            quantidade_dados = st.selectbox('',[3,5,4,2,1,10,15,20,30])
        st.table(df_visualizacao.tail(int(quantidade_dados))) #bizualizando os dados novos
    
    ###########################################################################    
    cadrastrar_colador = st.checkbox("ATUALIZAR COLADOR") #criando outro botao para outras coisas
    if cadrastrar_colador == True: #ativando ele
        coluna1,coluna2 = st.columns([1,1])
        #fazendo uma pequena seleçao 
        with coluna1:
            lista_colador = df_os['MARCA'].unique()
            marca_seletor = st.selectbox("MARCA", lista_colador)
        df_marca = df_os[df_os['MARCA'] == marca_seletor]
        lista_os = df_marca['OS'].unique()
        with coluna2:
            os_seletor = st.selectbox("OS",lista_os)
        
        df_os_final = df_os[df_os['OS'] == os_seletor]
        cor = df_os_final.iloc[0,6]
        tamanho_final = df_os_final.iloc[0,5]
        st.write('')
        st.write('')
         
        #mesma funçao dos dados acima        
        c1,c2,c3,c4,c5,c6,c7 = st.columns([1,1,1.2,2.5,2.5,1.5,2.5])
        with c1:
            data_dia = st.text_input('DIA')
        with c2:
            data_mes = st.text_input('MES')
        with c3:
            data_ano = st.text_input('ANO')
        with c4:
            data_os = st.selectbox('OS',[os_seletor, 'OS'])
        with c5:
            data_marca = st.selectbox('MARCA',[marca_seletor,"MARCA"])
        with c6:
            data_tamanho = st.selectbox('TAMANHO', [tamanho_final,'P','P2','M','M2','G','< >'])
        with c7:
            data_cor = st.selectbox('COR',[cor,"cor"])
                
        c8,c9,c10,c11 = st.columns([1,1,1,1])
        with c9:
            data_colador = st.text_input('COLADOR')
        with c8:
            botao_nome = st.checkbox("NOMES USADOS")
            nomes = list(df['COLADOR'].unique())
            if botao_nome == True:
                st.write(nomes)
            
        with c10:
            data_quantidade = st.text_input('QUANTIDADE')
        with c11:
            data_status = st.selectbox('STATUS',['ENVIADO','RECEBIDO'])
        
        lista_cadrastro = [data_dia,data_mes,data_ano,data_os,data_marca,data_tamanho,data_cor,data_colador,data_quantidade,data_status]
        
        botao_atualizar = st.button('SALVAR')
        if botao_atualizar == True:
            cabecalho = ['DIA','MES','ANO','OS','MARCA','TAMANHO','COR','COLADOR','QUANTIDADE','STATUS']
            #print(lista)
            with open("memoria.csv","w", newline="") as file:
                writer = csv.writer(file, delimiter=",")
                writer.writerow(cabecalho)
                writer.writerow(lista_cadrastro)
            
            df_memoria = pd.read_csv('memoria.csv')
            df_final = pd.concat([df,df_memoria])
            df_final.to_csv('entrada e saida.csv',index=False)
        
        c12,c13,c14 = st.columns([1,2,2])
        df_visualizacao = pd.read_csv('entrada e saida.csv')
        st.write("ULTIMOS REGISTRADOS")
        with c12:
            quantidade_dados = st.selectbox('',[3,5,4,2,1,10,15,20,30])
        st.table(df_visualizacao.tail(int(quantidade_dados)))

#INICAIANDO A SEGUNDA PARTE DO SISTEMA, ANALISE DOS DADOS
if pagina == 'ANALISAR':
    df2 = pd.read_csv('dados_os.csv')
    df3 = pd.read_csv('entrada e saida.csv')
    df_completo = pd.concat([df2,df3])
    df_completo.to_excel('dadosatuais.xlsx', index = False) #essa primeira parte serve pra juntar e salva os dados atuais
    
    #agora com os dados atualizados e salvo iremos chamalos
    
    df_atual = pd.read_excel('dadosatuais.xlsx')
    df_atual['QUANTIDADE'] = pd.to_numeric(df_atual["QUANTIDADE"])
    
    lista_marca = df_atual.MARCA.unique() #separando todas as marcas
    
    cx_marca = st.sidebar.selectbox("Escolha uma MARCA!",lista_marca) #criando uma seleçao para as marcas
    df_marca2 = df_atual[df_atual['MARCA'] == cx_marca] #criando um df so com as marcas selecionada
    lista_Os = df_marca2.OS.unique() #criando uma lista com todas as os
    cx_os = st.sidebar.selectbox("Selecione uma OS", lista_Os) #criando uma selecao para as os
    df_os2 = df_atual[df_atual["OS"] == cx_os] #selecionado apeanas os dados com as os
    df_total2 = df_os2[df_os2['STATUS'] == "TOTAL OS"] #criando os dados apenas com as os
    
    #fazendo a selecao do total de enviados e recebidos
    df_base = df[df['OS'] == cx_os]
    df_recebido = df_base[df_base["STATUS"] == 'RECEBIDO']
    df_enviado = df_base[df_base['STATUS'] == 'ENVIADO']
    soma_enviado = df_enviado.copy()
    soma_recebido = df_recebido.copy()
    
    juncao = soma_enviado.groupby(["OS", "TAMANHO", "STATUS",]).sum().reset_index()
    juncao2 = soma_recebido.groupby(["OS", "TAMANHO", "STATUS",]).sum().reset_index()

    df_total_final = pd.concat([df_total2,juncao,juncao2]) #juntando todas as informaçoes que precisamos
    
    c1,c,c2 = st.columns([1,0.2,1]) #criando outras colunas que iremos usar
    
    #criando o primeiro grafico
    with c1:
        fig_inicial = px.bar(df_total_final, x="OS", y="QUANTIDADE", color='STATUS',
                             barmode='group', height=400, width=400,
                             text_auto=True,
                             title=f"SACOLAS {df_total2.iloc[0,4]} {df_total2.iloc[0,5]} {df_total2.iloc[0,6]}")

        st.plotly_chart(fig_inicial)
    
    with c2:
        df_dropidez = df_os2[df_os2['STATUS'] != "TOTAL OS"].copy()
        coladores = df_dropidez.groupby(["COLADOR", "MARCA", "TAMANHO", "COR", "OS", "STATUS",]).sum().reset_index()
        coladores_enviado = coladores[coladores["STATUS"] == "ENVIADO"]
        coladores_recebido = coladores[coladores["STATUS"] == "RECEBIDO"]

        novo_coladores = pd.concat([coladores_enviado, coladores_recebido]) #juntando as informaç~es dos coladores

        fig2 = st.checkbox("VER COLADORES")
        
        if fig2 == True:
            
            fig_final = px.bar(novo_coladores, x="COLADOR", y="QUANTIDADE",
                               color="STATUS", text_auto=True,
                               barmode="group", height=400, width=500,
                               title="COLADORES")

            st.plotly_chart(fig_final)
        
        #transformando os número em data
            df_data = df_dropidez.copy()
            df_data["DATA"] = f"{df_data.iloc[0,0]:.0f}-{df_data.iloc[0,1]:.0f}-{df_data.iloc[0,2]:.0f}"
            df_data_atual = df_data[df_data['COLADOR'] != "IDEZ"]
            lista_data = list(df_data_atual['COLADOR'].unique())
        
            registros = st.checkbox("Verificar tabelas")
        
            if registros == True:
                pesquisa = st.selectbox("Colador", lista_data)

                df_tabela = df_data_atual[['DATA',"COLADOR",'QUANTIDADE','STATUS']]
            
                df_tabela_final = df_tabela[df_tabela['COLADOR'] == pesquisa]
                df_apresentacao = df_tabela_final[['DATA','QUANTIDADE','STATUS']]
                st.table(df_apresentacao)
