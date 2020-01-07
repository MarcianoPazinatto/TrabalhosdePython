# Aula 21 - 16-12-2019
#Funções para listas

from geradorlista import lista_simples_int
from random import randint

lista1 = lista_simples_int(randint(5,100))
lista2 = lista_simples_int(randint(5,75))
lista3 = lista_simples_int(randint(5,70))


# 1) Com as listas aleatórias (lista1,lista2,lista3) e usando as funções para listas,
# f-string, responda as seguintes questões:


# 1.1) Qual é o tamanho da lista1?
print(f'O tamanho da lista 1 é {len(lista1)}.')


# 1.2) Qual é o maior valor da lista2?
print(f'O maior valor da lista 2 é {max(lista2)}')


# 1.3) Qual seria a soma do maior valor com o menor valor da lista2?
print(f'A soma do núemro {max(lista2)} com {min(lista2)} é {max(lista2)+min(lista2)}')


# 1.4) Qual é a média aritmética da lista1?
print(f'A média aritmética da lista 1 é {sum(lista1)/len(lista1)}')


# 1.5) Qual o valor da soma de todas as listas e a soma total delas?
# quero que mostre a soma individual (por lista) e a soma total de todas elas (soma das somas das listas)
print(f'A soma da lista 1: {sum(lista1)} lista 2: {sum(lista2)} lista 3: {sum(lista3)} e a soma total delas é {sum(lista1)+sum(lista2)+sum(lista3)}')

# 1.6) Usando o f-string, imprima todos os valores da lista1 um de baixo do outro.
for i in lista1:
    print(f'{i}')


# 1.7) Com a indexação e f-string, mostre o valor das posições 5, 9, 10 e 25 de cada lista.
# trate para evitar o erro: IndexError
try:
    print(f'\n')
    print(f'Posição 5 lista 1 é :{lista1[4]}, posição 9: {lista1[8]}, posição 10: {lista1[9]} posição 25: {lista1[24]}')
    print(f'Posição 5 lista 1 é :{lista2[4]}, posição 9: {lista2[8]}, posição 10: {lista2[9]} posição 25: {lista2[24]}')
    print(f'Posição 5 lista 1 é :{lista3[4]}, posição 9: {lista3[8]}, posição 10: {lista3[9]} posição 25: {lista3[24]}')
except IndexError:
    print(f'Posição dada inválida')
finally:
    print(f'Fim...')    
# 1.8) Mostre qual das listas tem mais itens (lembre-se, as listas são randômicas, não há como prever o 
# tamanho delas).
print(f'\n')
if len(lista1) > len(lista2) and len(lista1) > len(lista3):
    print(f'Lista 1 é a maior.')
elif len(lista2) > len(lista1) and len(lista2) > len(lista3):
    print(f'lista 2 é a maior.')
elif len(lista3) > len(lista1) and len(lista3) > len(lista2):
    print(f'Lista 3 é a maior.')    
else:
    print(f'As listas são iguais de tamanho')      


# 1.9) Some os maiores números de todas as listas e subtraia pelo menor número dos menores valores das listas.
# Para obter o menor valor, pegue o menor valor das listas e veja qual deles é o menor e use ele.
print(f'A soma dos maiores itens dividindo pelos menores itens é: {(max(lista1)+max(lista2)+max(lista3))-min(lista1)+min(lista2)+min(lista3)}')


# 1.10) Pegue o maior valor de todas as listas e some com o menor valor de todas as listas
lista4 = (lista1 + lista2 + lista3)

print(f'{max(lista4)+min(lista4)}')







