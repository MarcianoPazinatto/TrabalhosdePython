#ORM
# ---- SqlAlchemy
#---- Instalação do framework
#--- pip3 install sqlalchemy

#---- Conector do Mysql
#---- Instalação do conector do Mysql
#---- pip3 install mysql-connector-python

from Aula53_corrigido.dao.produto_dao import ProdutoDao


dao = ProdutoDao()
produtos = dao.list_all()
print(produtos)
for p in produtos:
    print(p)