#from typing import Optional
from fastapi import FastAPI
#from pydantic import BaseModel
import facas
import dados

app = FastAPI()

@app.get('/')
def read_root():
    return {"AVISO":"VERSÃO TESTE"}


#parte das facas
#essa funcao me retorna a faca que eu estou procurando
@app.get('/{faca}')
def read_root(faca: str): 
    
    cima_c1 = facas.cima_c1()

    cima_c2 = facas.cima_c2()

    parede = facas.parede()

    baixo_c1 = facas.baixo_c1()

    baixo_c2 = facas.baixo_c2()

    estante_baixo = facas.estante_baixo()

    if faca in cima_c1:
        local = "ESTA EM CIMA EM C1"
    elif faca in cima_c2:
        local = "ESTA EM CIMA EM C2"
    elif faca in parede:
        local = "ESTA NA PAREDE"
    elif faca in baixo_c1:
        local = "ESTA EM BAIXO EM C1"
    elif faca in baixo_c2:
        local = "ESTA EM BAIXO EM C2"
    elif faca in estante_baixo:
        local = "ESTA EM BAIXO NA ESTANTE"
    else:
        local = "NÃO ENCONTRADO" 

    return {"FACA":faca, "OBS":local}


#criando a parte dos produtos que ja estão encaixotados
#essa funcao me retorna todas as marcas que tenho em dados
@app.get("/enviado/marca")
def deposito():
    marca = dados.marca()
    return marca

#criando a parte que separa os produtos por mes
#essa funcao me retorna todas as marcas por mes
@app.get("/enviado/marca/mes/{mes}")
def mes(mes: str):
    mes_ = dados.mes_geral(mes)
    if mes_ == {}:
        mes_ = {"ERRO": "DIGITE UM MES VALIDO [01,02,03,...]", "OBS":"PODE OCORRER DE NAO TERMOS DADOS"}

    return mes_


#criando a parte que separa os produtos por marca
#essa funcao me retorna os produtos por marca geral com todos os dados que tenho
@app.get("/enviado/marca/{marca}")
def produto(marca:str):
    produto = dados.produtos(marca)
    return produto

#ESSA PARTE AINDA NAO USO CORRETAMENTE
#@app.get("/items/{item_id}")
#def read_item(item_id: int, q: Optional[str]=None):
#    return {"item_id": item_id, "q":q}

#@app.put("/items/{item_id}")
#def update_item(item_id: int, item: Item):
#    return {"item_price": item.price, "item_id": item_id}

