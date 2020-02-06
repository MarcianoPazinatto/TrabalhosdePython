from Aula54.dao.base_dao import BaseDao
# importa as classes necessárias do basedao(mãe e do model)
from Aula54.model.cliente_model import ClienteModel

class ClienteDao(BaseDao):

    def list_all(self):
        return self.sessao.query(ClienteModel).all()
    # cria uma conexão com o banco de dados, e usa os dados da tabela model. e pega todos os dados da tabela
