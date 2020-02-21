from flask_restful import Api
from flask import Flask
from trabalho_notificacao.controller.notificacao_controller import BaseController


app = Flask(__name__)
api = Api(app)


api.add_resource(BaseController, '/api/trabalho_notificacao', endpoint='trabalho_notificacao')


app.run(debug=True)