from dao.sgbd_dao import SgbdDao
from model.sgbd import Sgbd

class SquadController:

    dao = SgbdDao()

    def listar_todos(self):
        lista_squad = []
        lista_tuplas = self.dao.listar_todos()
        for p in lista_tuplas:
            p1 = Squad()
            p1.id = p[0]
            p1.sistema_banco = p[1]
            lista_squads.append(p1)
        return lista_squads

    def buscar_por_id(self, id):
        p = self.dao.buscar_por_id(id)
        p1 = Sgbd()
        p1.id = p[0]
        p1.sistema_banco = p[1]
        return p1


    def salvar(self, sgbd:Sgbd):
        return self.dao.salvar(sgbd)

    def alterar(self, sgbd:Sgbd):
        self.dao.alterar(sgbd)

    def deletar(self, id):
        self.dao.deletar(id)