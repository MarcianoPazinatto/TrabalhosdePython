import MySQLdb
from model.linguagem import Linguagem

class LinguagemDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar_todos(self):
        comando = f"SELECT * FROM MARCIANO_LINGUAGEM"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchall()
        return resultado
    
    def buscar_por_id(self, id):
        comando = f"SELECT * FROM MARCIANO_LINGUAGEM WHERE ID = {id}"
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado

    def salvar(self, linguagem:Linguagem):
        comando = f""" INSERT INTO MARCIANO_LINGUAGEM
        (
            LING,
            
        )
        VALUES
        (
            '{linguagem.ling}',
            
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido

    def alterar(self, linguagem:Linguagem):
        comando = f""" UPDATE MARCIANO_LINGUAGEM
        SET
            LING = '{linguagem.ling}'
            
        WHERE ID = {linguagem.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM MARCIANO_LINGUAGEM WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()