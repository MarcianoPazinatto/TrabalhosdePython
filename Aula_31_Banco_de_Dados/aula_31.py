#Banco de Dados
#SGBD Sistema Gerenciador de Banco de Dados
#Mysql, SqlServer..........

#Mysql ~=MariaDb

#CRUD
#C = CREATE - INSERIR/SALVAR - INSERT
#R = READ - LER/LISTAR - SELECT
#U = UPDATE - ALTERAR - 
#D = DELETE - APAGAR

#pip3 install flask_mysql

import MySQLdb

conexao = MySQLdb.connect(host = 'mysql.topskills.study', database = 'topskills01', user = 'topskills01', passwd = 'ts2019')

cursor = conexao.cursor()
cursor.execute('SELECT * FROM MARCIANO1')
pessoas = cursor.fetchall()

for p in pessoas:
    print(p)

