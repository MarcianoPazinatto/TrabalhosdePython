import MySQLdb
from model.framework import Framework

class FrameworkDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM MARCIANO_FRAMEWORK"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM MARCIANO_FRAMEWORK WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, framework:Framework):
        comando = f""" INSERT INTO MARCIANO_FRAMEWORK
        (
            FRAME
          
        )
        VALUES
        (
            '{framework.frame}'
           
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, framework:Framework):
        comando = f""" UPDATE MARCIANO_FRAMEWORK
        SET
            FRAME = '{framework.frame}',
            
        WHERE ID = {framework.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM MARCIANO_FRAMEWORK WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()