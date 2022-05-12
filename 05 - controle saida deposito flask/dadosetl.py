import pandas as pd
import dados

tabela = dados.dados_get()
tabela_home = tabela.copy()
tabela_home['texto'] = tabela_home['marca'] + ' ' + tabela_home['produto'] + ' ' + tabela_home['quantidade']


lista = list(tabela_home.data)
lista2 = list(tabela_home.texto)

def tabela():
    j = 0
    tabela_inicio = {}
    for i in range(len(lista)):
        tabela_inicio[f'{j} {lista[i]} '] = f'{j} {lista2[i]}'
        j = j + 1
    return tabela_inicio


def marca(marca):
    df_marca = tabela_home[tabela_home['marca'] == marca]
    lista_marca = list(df_marca.data)
    lista_marca2 = list(df_marca.texto)
    tabela_marca = {}
    j = 0
    for i in range(len(lista_marca)):
        tabela_marca[f'{j} {lista_marca[i]}'] = f'{j} {lista_marca2[i]}'
        j = j + 1
    return tabela_marca




#print(marca('exito'))