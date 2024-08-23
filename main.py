from flask import Flask, jsonify, make_response, request
from bd import Dados

app = Flask('dados')

@app.route('/dados', methods=['GET'])
def GetDados():
    return Dados

@app.route('/dados/<int:id>', methods=['GET'])
def GetDado(id):
    for dado in Dados:
        if dado['id'] == id:
            return jsonify(dado)
    return make_response(jsonify(mensagem= "Dado não encontrado!"))

@app.route('/dados', methods=['POST'])
def PostDado():
    dadoNovo = request.get_json()
    for dado in Dados:
        if dado['id'] == dadoNovo['id']:
            return make_response(jsonify(mensagem = f"Dado com id {dadoNovo['id']} já existe!"))
    Dados.append(dadoNovo)
    return make_response(jsonify(mensagem = "Dado cadastrado com sucesso!", dado = dadoNovo))

@app.route('/dados', methods=['PUT'])
def PutDado():
    data = request.get_json()
    for dado in Dados:
        if 'id' in data:
            if dado['id'] == data['id']:
                if 'co2' in data:
                    if data['co2'] != dado['co2']:
                        dado['co2'] = data['co2']
                if 'temperatura' in data:
                    if data['temperatura'] != dado['temperatura']:
                        dado['temperatura'] = data['temperatura']
                if 'pressao' in data:
                    if data['pressao'] != dado['pressao']:
                        dado['pressao'] = data['pressao']
                if 'umidade' in data:
                    if data['umidade'] != dado['umidade']:
                        dado['umidade'] = data['umidade']
                if 'altitude' in data:
                    if data['altitude'] != dado['altitude']:
                        dado['altitude'] = data['altitude']
                return make_response(jsonify(mensagem = "Dado Atualizado com sucesso!", dado = dado))
    return make_response(jsonify(mensagem = "Informe um id!"))

@app.route('/dados/<int:id>', methods=['DELETE'])
def DeleteDado(id):
    for dado in Dados:
        if dado['id'] == id:
            Dados.remove(dado)
            return make_response(jsonify(mensagem = "Dado deletado com sucesso!", dado = dado))
    return make_response(jsonify(mensagem = "Dado não encontrado!"))


if __name__ == '__main__':
    app.run(port=5000, host='localhost')