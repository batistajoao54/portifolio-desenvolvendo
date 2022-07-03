#importando as bibliotecas q iremos usar
import plotly.express as px
import pandas as pd
from dash import Dash, html, dcc

#iniciando um app
app = Dash(__name__)

#criando os dados que iremos usar como teste
df = pd.DataFrame({
    "Fruit":["Apples","Oragens","Bananas","Apples","Oragens","Bananas",],
    "Amount":[4,1,2,2,4,5],
    "City":["SF","SF","SF","Montreal","Montreal","Montreal"]
})

#criando o grafico que iremos usar os dados

fig = px.bar(df,x="Fruit",y="Amount",color="City",barmode="group",text_auto=True)


#adicionando os dados no app
app.layout = html.Div(children=[
    html.H1(children="Olá Dash"),

    html.Div(children='''Dash: A web de aplicações de dados para você, fiz uma alteração'''),

    dcc.Graph(
        id="Exemplo de grafico",
        figure=fig
    )
])

#finalizando o app

if __name__ == "__main__":
    app.run(debug=True)











