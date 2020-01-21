import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

def listar(self):
    comando = f'SELECT * FROM MARCIANO_SQUAD'
    self.cursor.execute(comando)
    resultado = self.cursor.fetchall()
    return resultado    

    