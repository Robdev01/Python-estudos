from flask import Flask, jsonify
from tabulate import tabulate

app = Flask(__name__)


class Pessoa:
    def __init__(self, numero, nome, cidade, pais):
        self.numero = numero
        self.nome = nome
        self.cidade = cidade
        self.pais = pais


@app.route('/')
def entrada():
    numeros = [1, 2, 3, 4, 5, 6]
    nomes = ["Bruna", "Gabriel", "Maria", "Gabriela", "Robson", "Jubila"]
    cidades = ["sbc", "sbc", "sbc", "bh", "sbc", "sp"]
    paises = ["BR", "BR", "BR", "BR", "BR", "USA"]

    pessoas = [Pessoa(numero, nome, cidade, pais) for numero, nome, cidade, pais in
               zip(numeros, nomes, cidades, paises)]

    table = []
    for pessoa in pessoas:
        table.append([pessoa.numero, pessoa.nome, pessoa.cidade, pessoa.pais])

    return tabulate(table, headers=["Número", "Nome", "Cidade", "País"], tablefmt="html")


if __name__ == '__main__':
    app.run(debug=True)
