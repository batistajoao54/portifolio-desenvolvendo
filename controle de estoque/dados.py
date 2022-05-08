import pandas as pd
import requests as r

def dados_get():
    url = 'https://raw.githubusercontent.com/batistajoao54/portifolio-desenvolvendo/main/dados.csv'

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
    
   
    nome = []

    for i in dados[1:]:
        nomes= i[1]
        nome.append(nomes)
    

    marca = []

    for i in dados[1:]:
        marcas= i[2]
        marca.append(marcas)
    

    tipo = []

    for i in dados[1:]:
        tipos= i[3]
        tipo.append(tipos)
    

    modelo = []

    for i in dados[1:]:
        modelos = i[4]
        modelo.append(modelos)

    quantidade = []

    for i in dados[1:]:
        quantidades= i[5]
        quantidade.append(quantidades)

    dicionario = {f'{dados[0][0]}':data,
                    f'{dados[0][1]}':nome,
                    f'{dados[0][2]}':marca,
                    f'{dados[0][3]}':tipo,
                    f'{dados[0][4]}':modelo,
                    f'{dados[0][5]}':quantidade,}

    df = pd.DataFrame(dicionario)
    return df

print(dados_get())


