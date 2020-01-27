#----- Importar biblioteca do Mysql
import MySQLdb
from model.squad import Squad

class SquadDao:

    def __init__(self):
        #----- Configurar a conexão
        self.conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
        #----- Salva o cursor da conexão em uma variável
        self.cursor = self.conexao.cursor()

    def listar_todos(self):
        #----- Criação do comando SQL e passado para o cursor
        comando_sql_select = f""" SELECT S.ID, S.NOME,S.DESCRICAO,S.NUMEROPESSOAS,B.LING,A.FRAME,C.SISTEMA_BANCO FROM MARCIANO_SQUAD AS S
        INNER JOIN MARCIANO_FRAMEWORK AS A ON S.FRAMEWORKFRONTEND= A.ID
        INNER JOIN MARCIANO_LINGUAGEM AS B ON S.LINGUAGEMBACKEND = B.ID
        INNER JOIN MARCIANO_SGBD AS C ON S.SGBD = C.ID
        
        
        """
        self.cursor.execute(comando_sql_select)
        #---- Pega todos os resultados da execução do comando SQL e armazena em uma variável
        resultado = self.cursor.fetchall()
        return resultado

    def buscar_por_id(self, id):
        #----- Criação do comando SQL e passado para o cursor
        comando = f""" SELECT S.ID, 
        S.NOME,S.DESCRICAO,
        S.NUMEROPESSOAS,
        B.ID,
        B.LING
        ,A.ID, 
        A.FRAME,
        C.ID,
        C.SISTEMA_BANCO 
        FROM MARCIANO_SQUAD AS S
        INNER JOIN MARCIANO_FRAMEWORK AS A ON S.FRAMEWORKFRONTEND= A.ID
        INNER JOIN MARCIANO_LINGUAGEM AS B ON S.LINGUAGEMBACKEND = B.ID
        INNER JOIN MARCIANO_SGBD AS C ON S.SGBD = C.ID WHERE S.ID = {id}
        
        
        """
        self.cursor.execute(comando)
        resultado = self.cursor.fetchone()
        return resultado
    
    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO MARCIANO_SQUAD
        (
            NOME,
            DESCRICAO,
            NUMEROPESSOAS,
            LINGUAGEMBACKEND,
            FRAMEWORKFRONTEND,
            SGBD
        )
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            {squad.numeropessoas},
            {squad.linguagem.id},
            {squad.framework.id},
            {squad.sgbd.id}
        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido
    
    def alterar(self, squad:Squad):
        comando = f""" UPDATE MARCIANO_SQUAD
        SET
            NOME = '{squad.nome}',
            DESCRICAO ='{squad.descricao}',
            NUMEROPESSOAS = {squad.numeropessoas},
            LINGUAGEMBACKEND = {squad.linguagem.id},
            FRAMEWORKFRONTEND = {squad.framework.id},
            SGBD = {squad.sgbd.id}
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()


    def deletar(self, id):
        comando = f"DELETE FROM MARCIANO_SQUAD WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()