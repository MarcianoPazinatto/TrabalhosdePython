from flask import Flask
from flask_restful import Api

from Aula42.pessoa_controller.PessoaController import PessoaController

app = Flask(__name__)
api = Api(app)

api.add_resource(PessoaController, '/api/pessoa', endpoint='pessoas')
api.add_resource(PessoaController, '/api/pessoa/<int:id>', endpoint='pessoa')

app.run(debug=True)