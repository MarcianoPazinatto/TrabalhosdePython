# pip3 install flask_mysqldb
# referencia ao Mysql
import time
import MySQLdb
#listar todas as pessoas 
def listar_todos(c):
    c.execute('SELECT * FROM MARCIANO1')
    pessoas = c.fetchall()
    for p in pessoas:
        print(p)

def visualizar_end(c):
    c.execute('SELECT * FROM MARCIANO2')
    pessoas = c.fetchall()
    for a in pessoas:
        print(a)        
        
#buscar uma pessoa pelo ID
def buscar_por_id(c, id):
    c.execute(f'SELECT * FROM MARCIANO1 WHERE ID = {id}')
    pessoa = c.fetchone()
    print(pessoa)

#buscar pessoas por sobrenome
def buscar_por_sobrenome(c, sobrenome):
    c.execute(f"SELECT * FROM MARCIANO1 WHERE SOBRENOME like '{sobrenome}%' ")
    for p  in  c.fetchall():
        print(p)

#salvar pessoa
def salvar(cn, cr, nome, sobrenome, idade,email, endereco_id='NULL'):
    cr.execute(f"INSERT INTO MARCIANO1 (NOME, SOBRENOME, IDADE,EMAIL, ENDEREÇO_ID )VALUES('{nome}', '{sobrenome}',{idade},'{email}',{endereco_id})")
    cn.commit()

# #salvar endereço
def salvar_end(cn, cr, rua, bairro, cidade):
    cr.execute(f"INSERT INTO MARCIANO2 (RUA, BAIRRO, CIDADE)VALUES('{rua}', '{bairro}','{cidade}')")
    cn.commit()

#alterar pessoa
def alterar(cn, cr, id, nome, sobrenome, idade, endereco_id='NULL'):
    cr.execute(f"UPDATE MARCIANO1 SET NOME='{nome}', SOBRENOME='{sobrenome}', IDADE={idade}, ENDERECO_ID={endereco_id} WHERE ID={id} ")
    cn.commit()

#alterar endereço
def alterar_end(cn, cr, id, rua, bairro, cidade):
    cr.execute(f"UPDATE MARCIANO2 SET RUA='{rua}', BAIRRO='{bairro}', CIDADE={cidade}")
    cn.commit()    

#deletar pessoa por ID
def deletar(cn, cr, id):
    cr.execute(f'DELETE FROM MARCIANO1 WHERE ID={id}')
    cn.commit()

#deletar pessoa por ID
def deletar_end(cn, cr, id):
    cr.execute(f'DELETE FROM MARCIANO2 WHERE ID={id}')
    cn.commit()

conexao = MySQLdb.connect(host='mysql.topskills.study', database='topskills01', user='topskills01', passwd='ts2019' )
cursor = conexao.cursor()

# visualizar_end(cursor)
# listar_todos(cursor)
# buscar_por_id(cursor, 3)
# buscar_por_sobrenome(cursor,'Gru')
# salvar(conexao, cursor, 'José', 'Mulé',22,'eu@mim')
# alterar(conexao, cursor, 8, 'Gugu Voltolini', 'KingOfBasquete', 17, 5)
# deletar(conexao, cursor, 7)
# deletar(conexao, cursor,(int(input('Digite o id que deseja deletar: '))))
# salvar(conexao, cursor, (input('Digite o nome: ')), (input('Digite o sobrenome '))
# ,(int(input('Digite a idade: '))),(input('Digite o email: ')))
# salvar_end(conexao,cursor,(input('Digite a rua: ')), (input('Digite o bairro: ')), (input('Digite a cidade: ')))
# deletar_end(conexao,cursor,(input('Digite o id do endereço que deseja apagar: ')))

# while True:
#     print('''Digite 
#     (1) para inserir nova pessoa
#     (2) para deletar pessoa
#     (3) para visualizar''')
#     a = int(input('Digite uma opção: '))
#     if a == 1:
#         salvar(conexao, cursor, (input('Digite o nome: ')), (input('Digite o sobrenome '))
#         ,(int(input('Digite a idade: '))),(input('Digite o email: ')))
#         time.sleep(1)
#     elif a == 2:
#         deletar(conexao, cursor,(int(input('Digite o id que deseja deletar: '))))
#     elif a==3:
#         print(f'*'*70)
#         listar_todos(cursor)
#         print(f'*'*70)
#         time.sleep(3)
#     else: 
#         print('******Opção errada******')
#         time.sleep(2)   

