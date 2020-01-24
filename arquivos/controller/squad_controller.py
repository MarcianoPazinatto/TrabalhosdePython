from dao.squad_dao import SquadDao
from model.squad import Squad
from model.framework import Framework
from model.linguagem import Linguagem
from model.sgbd import Sgbd
from controller.framework_controller import FrameworkController
from controller.linguagem_controller import LinguagemController
from controller.sgbd_controller import SgbdController

class SquadController:

    dao = SquadDao()

    def listar_todos(self):
        lista_squads = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            p1 = Squad()
            p1.id = p[0]
            p1.nome = p[1]
            p1.descricao= p[2]
            p1.numeropessoas = p[3]
            p1.linguagembackend = p[4]
            p1.frameworkfrontend = p[5]
            p1.framework = Framework()
            p1.framework.id = p[6]
            p1.framework.frame = p[7]
            p1.linguagem = Linguagem()
            p1.linguagem.id = p[8]
            p1.linguagem.ling = p[9]
            p1.sgbd = Sgbd() 
            p1.sgbd.id = p[10]
            p1.sgbd.sistema_banco = p[11]
            lista_squads.append(p1)
        return lista_squads

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        p1 = Squad()
        p1.id = p[0]
        p1.nome = p[1]
        p1.descricao= p[2]
        p1.numeropessoas = p[3]
        p1.linguagembackend = p[4]
        p1.frameworkfrontend = p[5]
        p1.framework = Framework()
        p1.framework.id = p[6]
        p1.framework.frame = p[7]
        p1.linguagem = Framework()
        p1.linguagem.id = p[8]
        p1.linguagem.ling = p[9]
        p1.sgbd = Sgbd()
        p1.sgbd.id = p[10]
        p1.sgbd.sistema_banco = p[11]
        return p1

    def salvar(self, squad:Squad):
        squad.framework.id = self.framework_controller.salvar(squad.framework)
        squad.linguagem.id = self.linguagem_controller.salvar(squad.linguagem)
        squad.sgbd.id = self.sgbd_controller.salvar(squad.sgbd)
        return self.dao.salvar(squad)

    def alterar(self, squad:Squad):
        squad.framework.id = self.framework_controller.salvar(squad.framework)
        squad.linguagem.id = self.linguagem_controller.salvar(squad.linguagem)
        squad.sgbd.id = self.sgbd_controller.salvar(squad.sgbd)
        self.dao.alterar(squad)    


    # def salvar(self, squad:Squad):
    #     return self.dao.salvar(squad)

    # def alterar(self, squad:Squad):
    #     self.dao.alterar(squad)

    def deletar(self, id):
        self.dao.deletar(id)