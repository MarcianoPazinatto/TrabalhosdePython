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
    id_end = request.args['id_end']
    squad_controller.deletar(id)
    if id_end != 'None':
        end_controller.deletar(id_end)
    return redirect('/listar')

@app.route('/salvar')
def salvar():
    squad = Squad()
    squad.id = request.args['id']
    squad.nome = request.args['nome']
    squad.descricao = request.args['descrição']
    squad.numeropessoas = request.args['numero de pessoas']
    squad.linguagembackend = request.args['linguagem back end']
    squad.frameworkfrontend = request.args['framework front end']

  
    # pessoa.endereco = end

    if squad.id == 0:
        squad_controller.salvar(squad)
    else:
        squad_controller.alterar(squad)
    return redirect('/listar')

app.run(debug=True)

