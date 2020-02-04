import MySQLdb

from Aula51.model.Cliente_Model import ClienteModel

class ClienteDao:
    def __init__(self):
        self.connection = MySQLdb.connect(host='mysql.topskills.dev', database='topskills01', user='topskills01', passwd='ts2019')
        self.cursor = self.connection.cursor()

    def listartodos(self):
        self.cursor.execute("SELECT * FROM TABELA_CLIENTES")
        clientes = self.cursor.fetchall()
        lista_clientes = []
        for c in clientes:
            cliente = ClienteModel(c[1], c[2], c[3], c[4], c[0])
            lista_clientes.append(cliente.__dict__)
        return lista_clientes

    def pgid(self, id):
        self.cursor.execute("SELECT * FROM TABELA_CLIENTES WHERE ID = {}".format(id))
        cliente = self.cursor.fetchone()
        c = ClienteModel(cliente[1], cliente[2], cliente[3], cliente[4], cliente[0])
        return c.__dict__

    def inserir(self, cliente : ClienteModel):
        self.cursor.execute("INSERT INTO TABELA_CLIENTES(NOME, SOBRENOME, IDADE, SEXO) VALUES ('{}','{}',{},'{}')".format(cliente.nome, cliente.sobrenome, cliente.idade, cliente.sexo))
        self.connection.commit()
        id = self.cursor.lastrowid
        cliente.id = id
        return cliente.__dict__

    def update(self, cliente: ClienteModel):
        self.cursor.execute("UPDATE TABELA_CLIENTES SET NOME = '{}', SOBRENOME = '{}', IDADE = {}, SEXO = '{}' WHERE ID = {}".format(cliente.nome,cliente.sobrenome, cliente.idade, cliente.sexo, cliente.id))
        self. connection. commit()
        return cliente.__dict__

    def remover(self, id):
        self.cursor.execute("DELETE FROM TABELA_CLIENTES WHERE ID = {}".format(id))
        self.connection.commit()
        return 'removido a pessoa de id: {}'.format(id)
