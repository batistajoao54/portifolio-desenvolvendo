import plotly.express as px
import pandas as pd
from dash import Dash, dcc, html

app = Dash(__name__)
#server = app.server

df = pd.read_csv('dados.csv')
#print(df.info())

#importante o df deve estar limpo e suas colunas devidamente preenchida
#com seus tipos int ou str, etc..

fig = px.scatter(df, x='pessoa', y='marca', size='quantidade', color='status',
                 hover_name='os', size_max=60)

#esse grafico nao deu muito certo com os dados que usei
#size deve ser int

figura = px.bar(df, x='pessoa', y= 'quantidade', color='status', barmode='group', text='quantidade')

app.layout= html.Div([
    dcc.Graph(
        id = 'Quantidade-de-sacolas',
        figure= fig
    ),

    html.Div(children="GRAFICO DE BARRA",style={'textAlign':'center'}),

    dcc.Graph(
        id= "grafico-barra",
        figure= figura
    )

])




if __name__ == '__main__':
    app.run_server(debug=True)

