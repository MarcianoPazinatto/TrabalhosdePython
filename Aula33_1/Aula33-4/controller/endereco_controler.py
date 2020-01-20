
from model.endereco import Endereco
from dao.endereco_db import EnderecoDb

class EnderecoController:
    e = Endereco()
    e_db = EnderecoDb()

    def listar_todos_enderecos(self):
        return self.e_db.listar_todos_enderecos()

    def exportar(self):
        lec = self.e_db.listar_todos_enderecos()
        self.e.exportar_txt(lec)
