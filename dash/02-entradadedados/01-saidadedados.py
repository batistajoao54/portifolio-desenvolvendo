import pandas as pd
from dash import Dash, dcc, html, Input, Output


app = Dash(__name__)
server = app.server

app.layout = html.Div([
    html.H1("DIGITE O NÚMERO DA FACA"),
    html.Div([
        "Faca: ",
        dcc.Input(id='my-input', value='', type='text')
    ]),
    html.Br(),
    html.Div(id='my-output',),

])


@app.callback(
    Output(component_id='my-output', component_property='children'),
    Input(component_id='my-input', component_property='value')
)
def update_output_div(input_value):

    cima_c1 = ('2','180','121','120','109','104','107','13','183','105',
            '176','7','194','132','9','163','101','126','119','118',
            '117','125','218')

    cima_c2 = ('154','193','202','201','187','123','185','5','205','164','139','211','141',
        '50','51','138','168','165','151','124','216','149','54','156','216','137',
        '212','140','148','144','146','136','162','217')

    parede = ('57','166','145','197','55','158','172','159','173','142','147','174','60','61',
        '170','169','198','62','157','209','153','160','175','64','171','127b','167')

    baixo_c1 = (
        '106', 'luciano', '14', '130', '131', '186', '108', '112', '190', '200', '116', '129',
        '3', '8', '210', '127a', '133', '219', '182'
    )

    baixo_c2 = (
        '10', '134', '135', '58', '59', '16', '111', '110', '192', '196', '189', '102',
        '181', '115', '17', '114', '203', '214', '195', '188', '199'
    )

    estante_baixo = (
        '207', '103', '6', '113', '208', '204', '128', '122', '52', '152', '155', '200',
        '4', '191', '150', '215', '213', '143', '199b', '206', '161',
    )

    parede_interna = (
        '228', '223b', '225', '222', '226', '227', '223', '224', '229',
        '230', '231', '232', '233', '234', '235', '236', '237', '238', '239',
        '240', '241', '242',
    )

    if input_value in cima_c1:
        return 'Local: está em CIMA_C1'
    if input_value in cima_c2:
        return 'Local: está em CIMA_C2'
    if input_value in parede:
        return 'Local: está na PAREDE'
    if input_value in baixo_c1:
        return 'Local: está em BAIXO_C1'
    if input_value in baixo_c2:
        return 'Local: está em BAIXO_C2'
    if input_value in estante_baixo:
        return 'Local: está EMBAIXO NA ESTANTE'
    if input_value in parede_interna:
        return 'Local: está NA PAREDE INTERNA'
    elif input_value == "":
        return ''
    else:
        return 'Local: não encontrada'


if __name__ == '__main__':
    app.run_server(debug=True)
