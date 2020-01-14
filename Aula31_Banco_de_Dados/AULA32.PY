import MySQLdb

def listar_todos(c):
    c.execute('SELECT * FROM MARCIANO1')
    pessoas = c.fetchall()
    for p in pessoas:
        print(p)

def buscar_por_id(c,id):
    c.execute(f'SELECT * FROM MARCIANO1 WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

conexao = MySQLdb.connect(host = 'mysql.topskills.study', database = 'topskills01', user = 'topskills01', passwd = 'ts2019')    
cursor = conexao.cursor()
# cursor.execute('SELECT * FROM MARCIANO1')
# pessoas = cursor.fetchall()       

buscar_por_id(cursor,4)