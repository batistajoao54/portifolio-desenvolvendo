import streamlit as st
import pandas as pd


df = pd.read_csv('dados.csv')

lista_nomes = list(df['pessoa'].unique())
lista_nomes.insert(0, '')

lista_marcas = list(df['marca'].unique())
lista_marcas.insert(0,'')


st.set_page_config(layout = 'wide')

st.title("CONTROLE DE SACOLAS")

nome = st.selectbox("PESQUISA POR NOME", lista_nomes)


#codigo para detalhar os dados atravez do nome do sacoleiro
if nome != '':
    
    #ficar atendo quando a os vir a ser usada como parametro
    
    df_nome = df[df['pessoa'] == nome].copy()
    
    c1,c2,c3,c4,c5 = st.columns((2,2,1,2,2))
    
    with c1:
        st.image('user.png')
    
    with c2:
        lista_marca_pessoa = list(df_nome['marca'].unique())
        lista_marca_pessoa.insert(0,'')
        
        lista_cor_pessoa = list(df_nome['cor'].unique())
        lista_cor_pessoa.insert(0,'')
        
                
        selecionar_marca = st.selectbox("MARCA", lista_marca_pessoa)
        df_marca = df_nome[df_nome['marca'] == selecionar_marca].copy()
        
        if selecionar_marca != '':
            selecionar_cor = st.selectbox("COR", lista_cor_pessoa)

            #essa parte foi para pegar o valor pego das sacolas apos selecionar a cor
            df_pegou = df_marca[df_marca['cor']== selecionar_cor].copy()
            df_pegou_final = df_pegou[df_pegou['status'] == "pegou"].copy()
            quantidade_pega = df_pegou_final['quantidade'].sum()
            
            #agora essa parte para as sacolas entregues
            df_entregou_final = df_pegou[df_pegou['status'] == "entregou"].copy()
            quantidade_entregue = df_entregou_final['quantidade'].sum()
            if len(df_entregou_final) == 0:
                quantidade_entregue = "NÃO ENTREGOU"
            
            
            with c4:
                
                if selecionar_cor != '':
                    st.write('')
                    st.write('')
                    st.write('')
                    st.metric(label= "PEGOU", value = f"{quantidade_pega}")
    
            with c5:
                if selecionar_cor != '':
                    st.write('')
                    st.write('')
                    st.write('')
                    st.metric(label= "ENTREGOU", value = f"{quantidade_entregue}")
    
        
    st.table(df_marca)







marca = st.selectbox("PESQUISA POR MARCA", lista_marcas)




