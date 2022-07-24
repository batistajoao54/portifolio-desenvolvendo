import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff

from dash import Dash, html, dcc

#importando os dados que iremos usar, importante deixar os dados os mais limpo possivel
df = pd.read_csv('dados.csv')

#criando o grafico de tabela
fig = ff.create_table(df, height_constant=20, annotation_offset=0.4)


#criando uma funçao que ira montar a tabela html
def gerador_tabela(df,max_range=10):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in df.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df),max_range))
        ])
    ])



#iniciando o app
app = Dash(__name__)
#server = app.server


#cores que podemos usar na construçao do nosso desenvolvimento
cores = {
    'grey11': '#1C1C1C',
    'SteelBlue': '#4682B4',
    'Aquamarine': '#7FFFD4',
    'SpringGreen': '#00FF7F',
    'Chocolate': '#D2691E',
    'PowderBlue': '#B0E0E6',
}


#iniciando a colocar as componetes no desenvolvimento web

app.layout= html.Div(style={'backgroundColor':cores['grey11']}, children=[
    #criando um titulo
    html.H1(
        children="REVISÃO DE ALGUMAS COMPONETES ESTUDADAS",
        style={
            'textAlign':'center',
            'color': cores['SpringGreen'],
        }
    ),

    #fazendo referencia a criação de uma tabela
    html.Div(style= {'backgroundColor': cores['PowderBlue']}, children=[
        html.H3(
            children="Criando uma tabela com html,",
            style={
                'textAlign': 'center',
                'color': cores['grey11'],
            }
        ),
        #gerando a tabela no desenvolvimento web
        gerador_tabela(df)

    ]),

    #criando a mesma tabela mais usando o plotly
    html.H2(
        style={'backgroundColor': cores['Chocolate'], 'textAlign': 'center'},
        children= "Criando a mesma tabela, porem usando plotly"
    ),

    #plotando o grafico no desenvolvimento web
    dcc.Graph(
        id='grafico-tabela',
        figure=fig
    )


])




#fazendo o app inicializar
if __name__ == '__main__':
    app.run_server(debug = True)


