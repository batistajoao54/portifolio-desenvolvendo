import pandas as pd
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
        df_marca = df[df['MARCA'] == marca_seletor]
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
        st.write("QUANTIDADE DE DADOS REGISTRADOS")
        with c12:
            quantidade_dados = st.selectbox('',[3,5,4,2,1,10,15,20,30])
        st.table(df_visualizacao.tail(int(quantidade_dados)))
        


