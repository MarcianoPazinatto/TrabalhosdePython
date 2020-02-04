from flask import Flask
from flask_restful import Api

from Aula51.controller.Cliente_Controller import ClienteController

app = Flask(__name__)
api = Api(app)

api.add_resource(ClienteController, '/api/cliente', endpoint='clientes')
api.add_resource(ClienteController, '/api/cliente/<int:id>', endpoint='cliente')


app.run(debug=True)