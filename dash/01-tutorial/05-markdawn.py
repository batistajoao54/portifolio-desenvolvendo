import pandas as pd
from dash import Dash, html, dcc

app = Dash(__name__)
server = app.server

markdawn_text = '''
### Dash and Markdwon

Dash apps can be writter in markdown.
Dash uses the [CommonMark](http://commonmark.org/)
specification of markdown.
Check out their [60 Segund markdwon tutorial](http://commonmark.org/help/)
if this is your first introduction to markdwon!
'''

app.layout = html.Div([
    dcc.Markdown(style={'backgroundColor':'#DCDCDC'}, children=markdawn_text)
])

if __name__ == "__main__":
    app.run_server(debug = True)
