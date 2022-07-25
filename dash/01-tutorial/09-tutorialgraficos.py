#importando as blibliotecas que usaremos
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
#import tutorialdados
from dash import Dash, html, dcc

#criando funções que podemos estar usando
#importando os dados para dentro do codigo
df_dados = pd.read_csv('dados.csv')
#df_clima = pd.read_csv('clima.csv')

#modificando os dados para reduzir um pouco os dados
df_grupo = df_dados[['pessoa','status','marca','quantidade']].groupby(['status','pessoa','marca']).sum().reset_index()
#df_clima_grupo = df_clima[['EstacaoCodigo','Data','NumDiasDeChuva']].groupby(['EstacaoCodigo','Data']).sum().reset_index()

#criando os graficos dentro de funcoes

def sacolas_quantidades():
    fig = px.bar(df_grupo, x='pessoa', y='quantidade', color='status', barmode='group', text_auto=True)
    return fig

def sacolas_tabela():
    fig = ff.create_table(df_dados, height_constant=30)
    return fig

#def clima_dados():
#    fig = px.bar(df_clima_grupo, x='Data', y='NumDiasDeChuva', color='EstacaoCodigo', text_auto=True)
#    return fig
#------------------------------------------------------------------------------


#iniciando o app
app = Dash(__name__)
server = app.server

app.layout = html.Div(children=[
    html.H2(
        children="Adicionando Graficos",
        style={
            'textAlign': 'center',
            'color': '#D2691E'
        }
    ),

    dcc.Graph(
        id='grafico-sacolas',
        figure=sacolas_quantidades()
    ),

    dcc.Graph(
        id='grafico-tabela-sacola',
        figure=sacolas_tabela()
    ),

    #dcc.Graph(
    #    id='grafico-clima',
    #    figure=clima_dados()
    #)

])





#iniciando o app para rodar na web
if __name__ == '__main__':
    app.run_server(debug=True)

