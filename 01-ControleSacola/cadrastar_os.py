import pandas as pd
import streamlit as st
import csv

#st.set_page_config(layout='wide') #configura a pagina para q ela aconpanhe a expansao ou reduçao da mesma

def cadrastro_os():
    st.write("# *ESCREVER TUDO MAIUSCULO E SEM ACENTO*")
    df_os = pd.read_excel('02-dados_os.xlsx') #carregando os dados para a variavel
    
    
    c1,c2,c3,c4,c5,c6,c7 = st.columns([1.2,1.2,1.4,2.2,2.2,1.5,2.5]) #criando colunas para add os inputs
    
    #add cada coluna um input
    with c1:
        data_dia = st.number_input('DIA', min_value=1, max_value=31)
    with c2:
        data_mes = st.number_input('MES', min_value=1,max_value=12)
    with c3:
        data_ano = st.number_input('ANO',min_value=2022)
    with c4:
        data_os = st.text_input('OS')
    with c5:
        data_marca = st.text_input('MARCA')
    with c6:
        data_tamanho = st.selectbox('TAMANHO', ['P','PP','P2','M','M2','G','< >'])
    with c7:
        data_cor = st.text_input('DESCRIÇÃO')
            
    c8,c9,c10 = st.columns([1,1,1])
    with c8:
        data_colador = st.selectbox('COLADOR',['IDEZ'])
    with c9:
        data_quantidade = st.number_input('QUANTIDADE', min_value=1)
    with c10:
        data_status = st.selectbox('STATUS',['TOTAL OS'])
    
        
    botao_atualizar = st.button('SALVAR') #criando um botao
    if botao_atualizar == True: #ativando o botao
        lista_cadrastro = [data_dia,data_mes,data_ano,data_os.strip(),data_marca.strip(),data_tamanho,data_cor.strip(),data_colador.strip(),data_quantidade,data_status,'N'] #uma lista com todos os inputs coletados  
        cabecalho = ['DIA','MES','ANO','OS','MARCA','TAMANHO','COR','COLADOR','QUANTIDADE','STATUS','PAGO'] #usado para auxiliar na junção dos dados
        #st.write(lista_cadrastro) #verificando se os dados sao coletados

        with open("06-memoria.csv","w", newline="") as file: #escrevendo um aquivo memoria com os dados coletados
            writer = csv.writer(file, delimiter=",") #delimentando com virgula
            writer.writerow(cabecalho) #escrevendo o cabeçalho
            writer.writerow(lista_cadrastro) #escrevendo os dados coletados

        df_memoria = pd.read_csv('06-memoria.csv') #lendo os aquivos recem craiado
        df_final = pd.concat([df_os,df_memoria]) #juntando os aquivos antigos junto com os recem criado
        df_final= df_final.drop_duplicates() #eliminando duplicatas
        df_final.to_excel('02-dados_os.xlsx',index=False) #salvando os dados
        

    c11,c12,c13 = st.columns([1,2,2])
    df_visualizacao = pd.read_excel('02-dados_os.xlsx') #relendo os arquivos agora atualizado com os dados novos
    st.write("ULTIMOS DADOS REGISTRADOS")
    with c11:
        quantidade_dados = st.selectbox('',[3,5,4,2,1,10,15,20,30,40,50,100,200])
    st.table(df_visualizacao.tail(int(quantidade_dados))) #vizualizando os dados novos
    
    #essa parte é tentativa de reduzir os arquivos .py e tentar deixar o codigo mais rapido

    df = pd.read_excel('02-dados_os.xlsx')
    df2 = pd.read_excel('03-entrada e saida.xlsx')
    df_recebidos = df2[df2['STATUS'] == "RECEBIDO"] #selecioando apenas os dados recebidos
    df_filtro_soma = df_recebidos[['OS','MARCA','TAMANHO','COR','QUANTIDADE','STATUS']].copy() #fazendo uma pequena selecao para facilitar o tratamento
    df_soma_os = df_filtro_soma.groupby(['OS','MARCA','TAMANHO','COR','STATUS']).sum().reset_index() #somando as quantidades de acordo com cada OS
    lista_os_of = df['OS'].unique() #criando uma lista so com as OS dos dados de OS

    #tentando comparar os dados cuidado pra nao rodar 2 vezes
    for i in lista_os_of:
        df_concat = pd.read_csv('pesquisa.csv') #carregando um arquivo vazio
        df_fake = df[df['OS']== i].copy() #pesquisando cada os
        df_fake2 = df_soma_os[df_soma_os['OS'] == i].copy() #pesquisando cada os nos recebidos

        df_concat = pd.concat([df_fake,df_fake2,df_concat]) #juntando as informações
        df_concat= df_concat.drop_duplicates() #tentando remover as duplicatas
        df_concat.to_csv('pesquisa.csv',index=False) #salvando no mesmo diretorio csv


    #criando uma df so com as OS ativas
    for i in lista_os_of:
        df_ativa = pd.read_csv('ativas.csv')
        df4 = pd.read_csv('pesquisa.csv')
        df3 = df4[df4['OS'] == i] #pegando cada os
        try: #criando uma condição para os que derem errado no calculo
            a = df3.iloc[1,8] >= df3.iloc[0,8]*0.9 #fazendo uma pequena comparação
        except: #e atribuindo o valor a False
            a = False
    
        if a == False:
            df_ativa = pd.concat([df_ativa,df3]) #juntando os dados
            df_ativa = df_ativa.drop_duplicates() #tentando remover as duplicatas
            df_ativa[df_ativa['STATUS'] == "TOTAL OS"] .to_csv('ativas.csv', index=False) #salvando os dados






if "__main__" == __name__:  #condição para que  se o comando for rodado funcione
    cadrastro_os()
