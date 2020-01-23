from Dao.framework_dao import FrameworkDao
from Model.framework import Framework

class frameworkController:
    dao = FrameworkDao()

    def listar_todos(self):
        return self.dao.listar_todos()

    def buscar_por_id(self, id):
        return self.dao.buscar_por_id(id)

    def salvar(self, framework:Framework):
        return self.dao.salvar(framework)

    def alterar(self, framework:Framework):
        self.dao.alterar(framework)

    def deletar(self, id):
        self.dao.deletar(id)