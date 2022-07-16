
import pandas as pd
import streamlit as st 

cima_c1 = ['2','180','121','120','109','104','107','13','183','105',
            '176','7','194','132','9','163','101','126','119','118',
            '117','125','218']

cima_c2 = [
    '154','193','202','201','187','123','185','5','205','164','139','211','141',
    '50','51','138','168','165','151','124','216','149','54','156','216','137',
    '212','140','148','144','146','136','162','217'
]

parede = [
    '57','166','145','197','55','158','172','159','173','142','147','174','60','61',
    '170','169','198','62','157','209','153','160','175','64','171','127b','167'
]

baixo_c1 = [
    '106','luciano','14','130','131','186','108','112','190','200','116','129',
    '3','8','210','127a','133','219','182'
]

baixo_c2 = [
    '10','134','135','58','59','16','111','110','192','196','189','102',
    '181','115','17','114','203','214','195','188','199'
]

estante_baixo = [
    '207','103','6','113','208','204','128','122','52','152','155','200',
    '4','191','150','215','213','143','199b','206','161',
]

parede_interna = [
    '228','223b','225','222','226','227','223','224','229',
    '230','231','232','233','234','235','236','237','238','239',
    '240','241','242',
]



df = pd.read_excel('dados.xlsx')
df['numero'] = df['numero'].astype(str)


st.set_page_config(layout='wide')

c1,c2,c3 = st.columns([3,4,3])

with c2:
    st.title("CONSULTA DE FACAS")

faca = st.text_input("DIGITE O NÚMERO DA FACA.")

c1,c2,c3 = st.columns([3,1,3])

with c2:
    botao = st.button("BUSCAR")

df_faca = df[df['numero'] == faca]

 
if botao == True:
    df_faca.drop("numero", axis=1, inplace=True)
    st.table(df_faca)
    
    c1,c2,c3 = st.columns([3,4,3])
    with c2:

        if faca in cima_c1:
            st.markdown("## ESTÁ EM CIMA NA COLUNA 1")
        elif faca in cima_c2:
            st.markdown("## ESTÁ EM CIMA NA COLUNA 2")
        elif faca in parede:
            st.markdown("## ESTÁ EM PAREDE")
        elif faca in baixo_c1:
            st.markdown("## ESTÁ EMBAIXO NA COLUNA 1")
        elif faca in baixo_c2:
            st.markdown("## ESTÁ EMBAIXO NA COLUNA 2")
        elif faca in estante_baixo:
            st.markdown("## ESTÁ NA ESTANTE EMBAIXO")
        elif faca in parede_interna:
            st.markdown("## ESTÁ NA PAREDE INTERNA")
        elif faca == "":
            st.markdown("## DIGITE A NUMERAÇÃO DE UMA FACA")
        else:
           st.markdown("## NÃO ENCONTRADO")

st.markdown("## OUTRAS CONSULTAS")

c1,c5,c3,c4 = st.columns([1,1,1,1])

df_ordem = df.sort_values(by="tipo ")
tipos = list(df_ordem['tipo '].unique())

with c1:
    tipo = st.selectbox("TIPO", tipos)

with c5:
    st.text('')
    st.text('')
    st.text('')
    buscar = st.button("PROCURAR")

df_tipo = df[df['tipo '] == tipo]
df_tipo.drop("numero", axis=1, inplace=True)
st.table(df_tipo)

caixa = st.checkbox("MOSTRAR TABELA COMPLETA")

if caixa == True:
    df.drop("numero", axis=1, inplace=True)
    st.dataframe(df)
