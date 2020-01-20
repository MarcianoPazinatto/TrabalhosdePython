import MySQLdb

conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019')
cursor = conexao.cursor()
c_sql_select = "SELECT * FROM MARCIANO2"
cursor.execute(c_sql_select)
resultado = cursor.fetchall()
lista_enderecos = []
for e in resultado:
    dicionario_endereco = {'Id' : 0,'Rua' : '','Bairro' : '','Cidade':''}
    dicionario_endereco['Id'] = e[0]
    dicionario_endereco['Rua'] = e[1]
    dicionario_endereco['Bairro'] = e[2]
    dicionario_endereco['Cidade'] = e[3]
    lista_enderecos.append(dicionario_endereco)

with open('aula34/enderecos','a') as arquivo:
    for e in lista_enderecos:
        arquivo.write(f"{e['Id']};{e['Rua']};{e['Bairro']};{e['Cidade']}\n")    