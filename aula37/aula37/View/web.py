from flask import Flask, render_template, request, redirect
import sys
sys.path.append('/marciano/TrabalhosdePython/aula37/aula37')
from Controller.squad_controller import SquadController
from Controller.squad_controller import SquadController
from Model.squad import Squad

app = Flask(__name__)
squad_controller = SquadController()
end_controller = SquadController()
nome = 'Cadastros de Squad'

@app.route('/')
def inicio():
    return render_template('index.html', titulo_app = nome )

@app.route('/listar')
def listar():
    squad = squad_controller.listar()
    return render_template('listar.html', titulo_app = nome, lista = squad)

@app.route('/cadastrar')
def cadastrar():
    squad = Squad()    
    if 'id' in request.args:
        id = request.args['id']
        squad = squad_controller.buscar_por_id(id)
    return render_template('cadastrar.html', titulo_app = nome, squad = squad )


@app.route('/excluir')
def excluir():

    id = int(request.args['id'])
    squad_controller.deletar(id)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad_controller = SquadController()
    squad = Squad()
    squad.id = request.args['id']
    squad.nome = request.args['nome']
    squad.descricao = request.args['descricao']
    squad.numeropessoas = request.args['numeropessoas']
    squad.linguagembackend = request.args['linguagembackend']
    squad.frameworkfrontend = request.args['frameworkfrontend']

    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)    

    # pessoa.endereco = end

    # if squad.id == 0:
    #     squad_controller.salvar(squad)
    # else:
    #     squad_controller.alterar(squad)
    return redirect('/listar')

app.run(debug=True)

