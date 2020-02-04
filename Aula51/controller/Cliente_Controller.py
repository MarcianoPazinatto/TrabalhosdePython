from flask_restful import Resource
from flask import request

from Aula51.dao.Cliente_Dao import ClienteDao
from Aula51.model.Cliente_Model import ClienteModel

class ClienteController(Resource):
    def __init__(self):
        self.dao = ClienteDao()

    def get(self, id=None):
        if id:
            return self.dao.pgid(id)
        return self.dao.listartodos()

    def post(self):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = request.json['idade']
        sexo = request.json['sexo']
        cliente = ClienteModel(nome, sobrenome, idade, sexo)
        mensagem = self.dao.inserir(cliente)
        return mensagem

    def put(self,id):
        nome = request.json['nome']
        sobrenome = request.json['sobrenome']
        idade = request.json['idade']
        sexo = request.json['sexo']
        cliente = ClienteModel(nome, sobrenome, idade, sexo, id)
        mensagem = self.dao.update(cliente)
        return mensagem

    def delete(self,id):
        return self.dao.remover(id)
