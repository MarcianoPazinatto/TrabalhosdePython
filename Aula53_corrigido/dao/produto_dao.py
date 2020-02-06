# from Aula53_corrigido.dao.base_dao import BaseDao
from Aula53_corrigido.model.produto_model import ProdutoModel

class ProdutoDao(BaseDao):
    def list_all(self):
        return self.sessao.query(ProdutoModel).all()