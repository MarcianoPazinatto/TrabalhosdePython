import sqlalchemy as bd
# nomeia o alchemy para bd

from sqlalchemy.ext.declarative import declarative_base
# pega dentro do sqlalchemy e importa declarative_base

BaseAlchemy = declarative_base()
# declara o BaseAlchemy como o objeto declarative_base()

class ClienteModel(BaseAlchemy): #cria a classe e aponta a declaração
    __tablename__= "TABELA_CLIENTES" # declara o nome da tabela
    id = bd.Column(bd.Integer, primary_key=True)
    nome = bd.Column(bd.String(length=45))
    sobrenome = bd.Column(bd.String(length=45))
    idade = bd.Column(bd.Integer)
    sexo = bd.Column(bd.String(length=45))

    # declara as colunas do banco de dados e deixa explicito quais suas propriedades dentro do banco de dados

    def __str__(self):
        return " {}, {}, {}, {}, {}".format(self.id, self.nome, self.sobrenome, self.idade, self.sexo)