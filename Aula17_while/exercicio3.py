#Faça um programa que leia um numero inteiro de 1 a 10 no teclado e mostre se você acertou ou o número digitado é maior ou menor
#quando vc acertar o programa deve ser finalizado
from random import randint

aleatorio = randint(1,10)
numero=0


while aleatorio != numero:
    numero=int(input('Tente acertar o número de 1 a 10: '))
    if numero < aleatorio:
        print(f'\nDigite um número maior que {numero}')
    elif numero > aleatorio:
        print(f'\nDigite um número menor {numero}')  
    elif numero == aleatorio:
        print('\n************************************')
        print(f'ACERTOU o numero era {numero} !!!!!')  
        print('\n************************************')
        