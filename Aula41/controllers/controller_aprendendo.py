from flask_restful import Resource

from Aula41.daos import Pessoadao

class PessoaController(Resource):

    def __init__(self):
        self.dao = Pessoadao()

    def get(self):
        msg = self.dao.listar
        return msg

    def post(self):
        msg = self.dao.
        return 'Acessando pelo HTTP POST'

    def put(self):
        return 'Acessando pelo HTTP PUT'

    def delete(self):
        return 'Acessando pelo HTTP DELETE'
