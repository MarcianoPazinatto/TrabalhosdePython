from flask import Flask
from flask_restful import Api
# import controllers
from controllers.controller_aprendendo import Pessoa

app = Flask(__name__)
api = Api(app)

api.add_resource(Pessoa,'/api/teste1')

@app.route('/')
def inicio():
    return 'Dentro da API'

app.run(debug=True, port=80)