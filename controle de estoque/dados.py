import pandas as pd
import requests as r


# pegando os dados do repositorio e transformando ele em um dadaframe
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

#criando uma funcao para separar as marcas

def marca():
    dados = dados_get()

    marca = list(dados['marca'].unique())
   
    marca_ : dict = {}
    
    j = 1
    
    for i in range(len(marca)):
    
        marca_[f'<<{j}']= f'{marca[i]} >>  '
        j = j + 1

    return marca_
#print(marca())

dados = dados_get()

dados['data2'] = pd.to_datetime(dados.data)
#aparentimente a data esta no formado mes dia ano
dados['mes'] = dados.data2.dt.strftime('%d') #prestar atençao nesse detalhe aqui


#criando uma funcao pra separar as marcas por mes
def mes_geral(mes):
    dados_mes = dados[dados['mes'] == mes].copy()
    marca = list(dados_mes['marca'].unique())
   
    marca_ : dict = {}
    
    j = 1
    
    for i in range(len(marca)):
    
        marca_[f'<<{j}']= f'{marca[i]} >>  '
        j = j + 1

    return marca_
   
#print(mes_geral('05'))
dados['texto'] = dados['data'] + ' ' + dados['marca'] + ' ' + dados['produto'] + ' ' + dados['quantidade']

def produtos(empresa):
    dados_produtos = dados[dados['marca'] == empresa].copy()
    marca = list(dados_produtos['texto'].unique())
    marca_ : dict = {}
    j = 1
    for i in range(len(marca)):
        marca_[f'<<{j}']= f'{marca[i]} >>  '
        j = j + 1
    return marca_


print(produtos('exito'))
