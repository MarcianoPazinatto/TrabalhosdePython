import MySQLdb
from Model.squad import Squad

class SquadDao:
    conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
    cursor = conexao.cursor()

    def listar(self):
        comando = f'SELECT * FROM MARCIANO_SQUAD'
        self.cursor.execute(comando)        
        resultado = self.cursor.fetchall()
        return  resultado
        # list_s = self.converter(resultado)
        # return list_s     
    
    def salvar(self, squad:Squad):
        comando = f""" INSERT INTO MARCIANO_SQUAD
        (
            NOME,
            DESCRICAO,
            NUMEROPESSOAS,
            LINGUAGEMBACKEND,
            FRAMEWORKFRONTEND
        )
        VALUES
        (
            '{squad.nome}',
            '{squad.descricao}',
            '{squad.numeropessoas}',
            '{squad.linguagembackend}',
            '{squad.frameworkfrontend}'

        )"""
        self.cursor.execute(comando)
        self.conexao.commit()
        id_inserido = self.cursor.lastrowid
        return id_inserido
        
    def alterar(self, squad:Squad):
        comando = f""" UPDATE MARCIANO_SQUAD
        SET
            NOME = '{squad.nome}',
            SOBRENOME = '{squad.descricao}',
            NUMEROPESSOAS = '{squad.numeropessoas}',
            LINGUAGEMBACKEND = '{squad.linguagembackend}',
            FRAMEWORKFRONTEND = '{squad.frameworkfrontend}'
        WHERE ID = {squad.id}
        """
        self.cursor.execute(comando)
        self.conexao.commit()

    def deletar(self, id):
        comando = f"DELETE FROM MARCIANO_SQUAD WHERE ID = {id}"
        self.cursor.execute(comando)
        self.conexao.commit()    



    #  def converter(self, list_s):
    #     lista_squad = []
    #     for s in list_s:
    #         s1 = Squad()
    #         s1.id = s[0]
    #         s1.nome = s[1]
    #         s1.descricao = s[2]
    #         s1.linguagembackend = s[3]
    #         s1.frameworkfrontend = s[4]  
    #         lista_squad.append(s1)   
    #     return lista_squad    

    