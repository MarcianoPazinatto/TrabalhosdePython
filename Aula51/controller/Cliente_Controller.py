from flask_restful import Resource
from flask import request

from Aula51.dao.ClienteDao import ClienteDao
from Aula51.model.ClienteModel import ClienteModel

class ClienteController(Resource):
    def __init__(self):
        self.dao = ClienteDao

    def get(self, id=None):
        if id:
            return self.dao.pegar_pelo_id(id)
        return self.dao.listartodos()

    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = request.json['idade']
        sexo = request.json['sexo']
        cliente = ClienteModel(nome,sobrenome,idade,sexo)
        mensagem = self.dao.inserir(cliente)
        return mensagem

    def put(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = request.json['idade']
        sexo = request.json['sexo']
        cliente = ClienteModel(nome,sobrenome,idade,sexo)
        mensagem = self.dao.update(cliente)
        return mensagem

    def delete(self):
        return self.dao.remove(id)
