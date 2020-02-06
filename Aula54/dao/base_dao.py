import sqlalchemy as bd
# da o mesmo nome de bd ao alchemy, que está explicito no model

class BaseDao:
    def __init__(self):
        # ----database+conector://user:passwd@url:porta/database
        conexao = bd.create_engine("mysql+mysqlconnector://topskills01:ts2019@mysql.topskills.dev:3306/topskills01")
        criador_sessao = bd.orm.sessionmaker()
        criador_sessao.configure(bind=conexao)
        self.sessao = criador_sessao()

        # cria uma variável que conecta o banco de dados do sql, e nela atribui os valores para conexão