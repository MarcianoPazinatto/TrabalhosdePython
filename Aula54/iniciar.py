#ORM
# ---- SqlAlchemy
#---- Instalação do framework
#--- pip3 install sqlalchemy

#---- Conector do Mysql
#---- Instalação do conector do Mysql
#---- pip3 install mysql-connector-python

from Aula54.dao.cliente_dao import ClienteDao


dao = ClienteDao()
clientes = dao.list_all()
print(clientes)
for c in clientes:
    print(c)