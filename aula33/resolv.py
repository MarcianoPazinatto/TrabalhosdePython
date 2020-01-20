from TABELA_INSERIR import *

b = True
while b :
    print(f'''
    {'*'*50} 
    {'*'*5}(1) Inserir nova pessoa
    {'*'*5}(2) Deletar pessoa
    {'*'*5}(3) Visualizar
    {'*'*5}(4) Finalizando programa
    {'*'*50}
    ''')
    a = int(input('Digite uma opção: '))
    if a == 1:
        salvar(conexao, cursor, (input('Digite o nome: ')), (input('Digite o sobrenome '))
        ,(int(input('Digite a idade: '))),(input('Digite o email: ')))
        time.sleep(1)
    elif a == 2:
        deletar(conexao, cursor,(int(input('Digite o id que deseja deletar: '))))
    elif a == 3:
        print(f'*'*70)
        listar_todos(cursor)
        print(f'*'*70)
        time.sleep(3)
    elif a == 4:
        b = False
        print('Finalizando programa...')    
    else: 
        print('******Opção errada******')
        time.sleep(2)   