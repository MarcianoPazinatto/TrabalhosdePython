#########cLASSES
#IMPORTAR BIBLIOTECA Mysql
import MySQLdb

#CONFIGURAR CONEXÃO
conexao = MySQLdb.connect(host='mysql.topskills.study',database='topskills01', user= 'topskills01',passwd='ts2019')

#SALVA CURSOS DA CONEXÃO EM UMA VARIÁVEL
cursor = conexao.cursor()


#criação do comando sql e passando para o cursor
comando_sql_select = "SELECT * FROM MARCIANO1"

cursor.execute(comando_sql_select)
#cria uma lista para armazenar os dicionarios
lista_pessoas = []

resultado = cursor.fetchall()
for p in resultado:
    #criação do dicionarios que representa uma pessoa
    dicionario_pessoas = { 'Id':0, 'Nome':'', 'Sobrenome':'', 'Idade':0, 'endereco_id':0}
    
    #pega uma posição da tupla e atribui a uma chave do dicionario
    dicionario_pessoas['Id'] = p[0]
    dicionario_pessoas['Nome'] = p[1]
    dicionario_pessoas['Sobrenome'] = p[2]
    dicionario_pessoas['Idade'] = p[3]
    dicionario_pessoas['endereco_id'] = p[4]
    lista_pessoas.append(dicionario_pessoas)


with open('pessoas.txt','a') as arquivo:
    for p in lista_pessoas:
        arquivo.write(f"{p['Id']};{p['Nome']};{p['Sobrenome']};{p['Idade']};{p['endereco_id']}\n")    