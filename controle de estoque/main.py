import streamlit as st
import pandas as pd
import dados

df = dados.dados_get()


st.set_page_config(layout='wide')

c1,c2,c3 = st.columns((1,2,1))

with c2:
    st.title("CONTROLE DE MERCADORIAS")

#selecionando as marcas
marcas = list(df['marca'].unique())
clientes = st.selectbox("MARCAS", marcas)
df_marcas = df[df['marca'] == clientes]
#st.dataframe(df_marcas)

#selecionando os produtos
produtos = list(df_marcas['produto'].unique())
produtos_ = st.selectbox("PRODUTO", produtos)
df_produto = df_marcas[df_marcas['produto']== produtos_]

#selecionando especificacao
especificacao_ = list(df_produto['expecificacao'].unique())
especificacao = st.selectbox("TIPO", especificacao_)
df_especificacao = df_produto[df_produto['expecificacao']== especificacao]
#st.dataframe(df_especificacao)

#tratando a informação para ser exibida
deposito = df_especificacao[df_especificacao['deposito_enviado'] == 'deposito']
deposito['quantidade'] = pd.to_numeric(deposito['quantidade'])
soma = deposito['quantidade'].sum()
#st.dataframe(deposito)

st.markdown(f'## {produtos_} {especificacao}')
st.metric("QUANTIDADE",value=soma)

#informação dos enviados
st.markdown('## ENVIADOS')
enviado = df_especificacao[df_especificacao['deposito_enviado'] == 'enviado']
enviado['data'] = pd.to_datetime(enviado['data']).dt.strftime('%d-%m-%y')
#organizando o index final
enviados = enviado.reset_index()
enviados.drop(['index'], axis=1, inplace=True)

st.table(enviados.sort_values(by=['data'],ascending=False).head(10))


