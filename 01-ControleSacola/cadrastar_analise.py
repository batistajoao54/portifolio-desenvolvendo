import pandas as pd
import streamlit as st
import plotly.express as px



def analise():

    #Criar uma analise aqui pra ver se melhora o codigo
    #tentando diminuir o codigo e corrigindo alguns bugs
    df_os_filtrada = pd.read_csv('ativas.csv')
    df_coladores = pd.read_excel("03-entrada e saida.xlsx") #dados dos coladores sem o filtro
    lista_os2 = df_os_filtrada['OS'].unique() #filtrando as OS.

    #fazendo um loop para filtrar os coladores de acordo com as OS já filtradas
    for i in lista_os2:
        df_ativos = pd.read_excel('06-dados_ativos.xlsx') # esse arquivo tem que existir e ja preenchido as colunas
        df5 = df_coladores[df_coladores['OS'] == i] #filtrando os coladores pela OS linha a linha usando a lista das OS já filtrada
        df_ativos = pd.concat([df_ativos,df5]) #salvando essa linha se for verdadeira(se existir) 
        df_ativos = df_ativos.drop_duplicates() #eliminando as possiveis linhas duplas
        df_ativos.to_excel('06-dados_ativos.xlsx', index=False) #salvando essa nova seleção
    
    #juntando em um só arquivo os dados OS e os dados Coladores
    df_final23 = pd.concat([df_os_filtrada,df_ativos])
    df_final23.to_excel('04-dados-Os-Coladores-ativos.xlsx',index=False)
    
    #fim da analise
    
    caixa_escolha = st.checkbox("Ordem de Serviço com dados incompletos.")
    df_os = pd.read_excel('02-dados_os.xlsx')
    df_colador = pd.read_excel('03-entrada e saida.xlsx')
    df = pd.concat([df_os,df_colador])
    if caixa_escolha == True:
        df = df_final23 #caso queira apenas os dados ativos
    st.write(len(df),"LINHAS")

    lista_marca = list(df['MARCA'].unique()) #selecioando todas as marcas
    col1,col2,col3,col4,col5 = st.columns([2,7,0.1,0.1,0.1]) #criando colunas para começa a dividir a tela

    with col1: #escolha da marca
        opcao = st.selectbox("MARCA",lista_marca) 

    df_marca = df[df['MARCA'] == opcao].copy() #fitrando o df para apenas com as marcas
    df_marca['text'] = df_marca['MARCA'] + " " + df_marca['TAMANHO'] + " " + df_marca['COR'] + " || " + df_marca['OS'] #add um texto que sera usando nos graficos
    lista_os = list(df_marca['OS'].unique()) #separando as OS desse filtro

    
    with col2:
        opcao2 = st.multiselect('ADICIONE AS OS',lista_os,lista_os[-1])
    
    for i in opcao2:
        dados = df_marca[df_marca['OS'] == i]
        df_junto = dados.groupby(['COLADOR','OS','MARCA','TAMANHO','COR','STATUS','PAGO']).sum().reset_index()
        cabecalho = df_junto[df_junto['COLADOR'] == 'IDEZ'].copy() #separando todos as OS
        enviados = df_junto[df_junto['STATUS'] == 'ENVIADO'].copy() #separando todos os enviados
        recebidos = df_junto[df_junto['STATUS'] == 'RECEBIDO'].copy() #separando todos os recebidos
        df_temporario = pd.concat([enviados,recebidos]) #juntado os enviados e recebidos
        idez_enviados = enviados.copy()
        idez_recebidos = recebidos.copy()
        
        #talvez essa parte no futuro de um problema, mais no momento atual eu ainda nao sei fazer de outra forma
        #separar os enviados e somar todos com o nome de idez
        #juntar em um novo df e no final juntar com os dados a serem usado nos graficos
        idez_enviados['COLADOR'] = "IDEZ"
        idez_enviados = idez_enviados.groupby(['COLADOR','OS','MARCA','TAMANHO','COR','STATUS',]).sum().reset_index()
        idez_recebidos['COLADOR'] = "IDEZ"
        idez_recebidos = idez_recebidos.groupby(['COLADOR','OS','MARCA','TAMANHO','COR','STATUS',]).sum().reset_index()
        idez_juncao = pd.concat([idez_enviados, idez_recebidos])

       

        
        df_final = pd.concat([cabecalho,idez_juncao,df_temporario]) #para que o IDEZ seja o primeiro
        df_final=df_final.drop_duplicates() #eliminando as duplicatas se ouver
        texto = df_marca[df_marca['OS'] == i] #precisei para poder colocar os titulos dos graficos

        #criando o grafico ainda dentro do loop
        fig = px.bar(df_final, x="COLADOR", y="QUANTIDADE", color='STATUS',
                barmode='group', height=400, width=700,
                text_auto=True, title=f'SACOLAS {texto.iloc[0,11]}')
    
        st.plotly_chart(fig, use_container_width=True)

        sacola_colador = st.checkbox(f"{i} ver tabela") #ver os dados na tabela
        lista_colador_dados = list(df_final['COLADOR'].unique())

        #criando uma tabela com os coladores
        if sacola_colador == True:
            cx_dados = st.selectbox("Colador", lista_colador_dados)
            df_tabela = df_final[['DIA','MES','ANO',"COLADOR",'QUANTIDADE','STATUS','PAGO']]
            df_colador_dados = df_tabela[df_tabela['COLADOR'] == cx_dados]
            st.table(df_colador_dados)
    
        


if "__main__" == __name__:
    analise()
