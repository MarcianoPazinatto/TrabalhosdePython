from Dao.linguagem_dao import LinguagemDao
from Model.linguagem import Linguagem

class LinguagemController:
    dao = LinguagemDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, linguagem:Linguagem):
        return self.dao.salvar(linguagem)

    def alterar(self, linguagem:Linguagem):
        self.dao.alterar(linguagem)

    def deletar(self, id):
        self.dao.deletar(id)