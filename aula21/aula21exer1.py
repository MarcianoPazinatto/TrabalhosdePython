# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um arquivo que leia 2 números inteiros e imprima a soma, 
# multiplicação, divisão e subtração com uma f-string.

# 2 - Crie um while que pergunte se deseja continuar. Se digitar 's' o
# programa termina.

#################### até aqui tudo bem! ##########################

# 3 - faça um tratamento de exceção para que ao digitar o valor que 
# não seja inteiro, ele avise o usuário para ele digitar denovo.
# 4 - Faça outro tratamento de exceção para evitar que divida um numero
# por zero.
controle='n'
while controle !='s':
    try:
        num1=int(input('Digite o primeiro numero: '))
        num2=int(input('Digite o segundo número: '))
    except ValueError:
        print('Erro, você não digitou um número')
    else:
        print(f' {num1}+ {num2} = {num1+num2}')
        print(f' {num1}- {num2} = {num1-num2}')
        print(f' {num1}x {num2} = {num1*num2}')
    try:    
        print(f' {num1}/ {num2} = {num1/num2}')

    except:
        print('erro impossível de dividir para 0')

    controle=input(f's para sair ')

# while True:
#     try:
#         print('3213213')
#         numero= int(input('digite um numero: '))
#         print('22222')
#     except ValueError:
#         print('Erro')
#     else:
#         print('THE END')         
#         break 

   