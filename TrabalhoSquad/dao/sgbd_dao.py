import MySQLdb
from model.sgbd import Sgbd

class SgbdDao:    

    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = f"SELECT * FROM MARCIANO_SGBD"
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando = f"SELECT * FROM MARCIANO_SGBD WHERE ID= {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, sgbd:Sgbd):
        comando = f""" INSERT INTO MARCIANO_SGBD
        (   
            SISTEMA_BANCO
            
        )
        VALUES
        (   
            '{sgbd.sistema_banco}'
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido
    
    def alterar(self, sgbd:Sgbd):
        comando = f""" UPDATE MARCIANO_SGBD
        SET
            
            SISTEMA_BANCO = '{sgbd.sistema_banco}'
           
        WHERE ID = {sgbd.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()
    
    def deletar(self, id):
        comando = f"DELETE FROM MARCIANO_SGBD WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()