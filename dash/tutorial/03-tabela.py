#importante colocar os from abaixo dos imports
import pandas as pd
from dash import Dash,html

df = pd.read_csv('dados.csv')

#criando uma funcao que exibe a tabela do tadaframe do pandas
def generate_table(dataframe,max_rows =30):
    return html.Table([
        html.Thead(
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns
            ]) for i in range(min(len(dataframe),max_rows))
        ])
    ])

app = Dash(__name__)
server= app.server

app.layout = html.Div([
    html.H3(children="Controle de sacolas",style={'textAlign':'center'}),
    generate_table(df)
])

if __name__ == "__main__":
    app.run_server(debug = True)


#não saiou como imaginei mais da pra ter uma nocao dos dados abordados





