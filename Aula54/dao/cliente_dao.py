from Aula54.dao.base_dao import BaseDao
# importa as classes necessárias do basedao e do model
from Aula54.model.cliente_model import ClienteModel

class ClienteDao(BaseDao) # importa da classe mãe e atribui para a classe filha os seus atributos
    def list_all(self):
        return self.sessao.query(ClienteModel).all()
    