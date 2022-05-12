from flask import Flask
import dadosetl


app = Flask(__name__)


@app.route("/")
def homepage():
    tabela_inicio = dadosetl.tabela()
    return tabela_inicio


@app.route("/marca/<marca>")
def deposito(marca: str):

    tabela_marca = dadosetl.marca(marca)

    return tabela_marca


if __name__ == "__main__":
    app.run(debug=True)