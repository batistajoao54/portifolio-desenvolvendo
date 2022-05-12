import pandas as pd
import requests as r

def dados_get():
    url = 'https://raw.githubusercontent.com/batistajoao54/portifolio-desenvolvendo/main/deposito.csv'

    res = r.get(url)
    tabela = res.text

    separados = tabela.split()
    #nome = separados.split(',')

    dados = []

    for i in range(len(separados)):
        palavra = separados[i]
        linha = palavra.split(',')
        dados.append(linha)
    

    data = []

    for i in dados[1:]:
        datas= i[0]
        data.append(datas)

   
    marca = []

    for i in dados[1:]:
        marcas= i[1]
        marca.append(marcas)


    produto = []

    for i in dados[1:]:
        produtos= i[2]
        produto.append(produtos)


    cabecalho = dados[0]
    cabecalho

    

    quantidade = []

    for i in dados[1:]:
        quantidades= i[3]
        quantidade.append(quantidades)



    dicionario = {f'{cabecalho[0]}':data,
                f'{cabecalho[1]}':marca,
                f'{cabecalho[2]}':produto,
                f'{cabecalho[3]}':quantidade,
    }

    df = pd.DataFrame(dicionario)

    return df

#print(dados_get())




