import pandas as pd
import plotly.express as px
from dash import Dash,html,dcc

app2 = Dash(__name__)

colors = {
    'background':'#DCDCDC',
    'text': '#000000'
}

df = pd.DataFrame({
    'frutas':['maçã','laranja','banana','maçã','laranja','banana'],
    'quantidade':[4,1,2,2,4,5],
    'cidade':['SF','SF','SF','DF','DF','DF']
})

fig = px.bar(df,x='frutas',y='quantidade',color='cidade',barmode='group',text_auto=True)

fig.update_layout(
    plot_bgcolor = colors['background'],
    paper_bgcolor = colors['background'],
    font_color = colors['text']
)

app2.layout=html.Div(style={'backgroundColor':colors['background']},children=[
    html.H1(
        children="Olá, Dash!",
        style={
            'textAlign':'center',
            'color':colors['text']
        }
    ),

    html.Div(
        children='Dash: Um aplicativo de framework para seus dados.',
        style={
            'textAlign':'center',
            'color':colors['text']
        }
    ),

    dcc.Graph(
        id = 'exemplo-grafico-2',
        figure=fig
    )
])

if __name__ == '__main__':
    app2.run_server(debug = True)









