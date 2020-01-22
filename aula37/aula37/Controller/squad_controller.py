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
        self.s_db.alterar(squad)

    def deletar(self, id):
        self.s_db.deletar(id)  

    def buscar_por_id(self, id):
        p = self.s_db.buscar_por_id(id)
        squad = Squad()
        squad.id =  p[0]
        squad.nome = p[1]
        squad.descricao = p[2]
        squad.linguagembackend = p[3]
        equad.frameworkfrontend = p[4]        
        return squad     