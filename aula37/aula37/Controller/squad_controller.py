from Model.squad import Squad
from Dao.squad_dao import SquadDao

class SquadController:
    # s = Squad()
    s_db = SquadDao()

    def listar(self):
        return self.s_db.listar()

    
    def salvar(self, squad:Squad):
        return self.s_db.salvar(squad)

    def alterar(self, squad:Squad):
        return self.s_db.alterar(squad)

    def deletar(self, id):
        return self.s_db.deletar(id)    