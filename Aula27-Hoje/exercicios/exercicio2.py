# Aula 21 - 16-12-2019
#Operadores in is ==

from geradorlista import lista_simples_int_str
from geradorlista import lista_simples_int
from geradorlista import lista_simples_str
from geradorlista import embaralhar


# A função embaralhar() irá criar listas aleátorias, copiar-las
# e embaralhar. Desta forma não se sabe se as listas são iguais ou
# se as listas são as mesmas. Como defult ela irá criar 3 listas
# diferentes com 30 itens, copiálas e embaralar randomicamente
# retornando uma lista com o dobro (6) de itens.

lista = embaralhar(2,10)

a = lista[0]
b = lista[1]
c = lista[2]
d = lista[3]

# print(a)
# print(b)
# print(c)
# print(d)

# Neste caso, ele irá criar 2 listas com 10 itens, e retornará
# uma lista com 4 listas podendo cada uma ser cópia ou uma só.




lista = embaralhar(2,10,2)

print(lista)

# 1) Analisnado a lista gerada (possui 2 listas), diga se as duas listas são elas
# mesmas (is) ou são somente iguais (==).
if (lista[0])is(lista[1]):
    print (f'As listas são as mesmas ')
else:
    if (lista[0])==(lista[1]):
        print (f'As listas são iguais ')
    else:
        print(f'não são iguais e nem as mesmas')




# 2) Qual é o maior valor destas duas listas 
# print(max(lista[0]))
lista3=(lista[0]+ lista[1])
print(max(lista3))

# 3) Qual é o maior valor de cada lista
print(max(lista[0]))
print(max(lista[1]))
# 4) Há o número 10 dentro da lista[0]?
if '10' in lista[0]:
    print(f'Tem numero 10 na lista[0]')
else:
    print(f'Não tem 10 na lista[0]')    

# 5) Há o número 20 dentro da lista[1]?
if '20' in lista[1]:
    print(f'há o número 20 dentro da lista[1]')
else:
    print(f'Não tem o número 20')    


# 6) Quantos números da lista[0] tem dentro da lista[1]?
lixta = []
for i in lista[0]:
    if lista[1].count(i):
        lixta.append(i)
print(f'Tem na lista 1 e lista 2 {len(lixta)} ocorrencias')        
        


# 7) Mostre os números da lista[0] que estão dentro da lista[1]
print(f'Tem na lista 1 e na lista 2 essas ocorrencias: {lixta}')

# 8) Mutliplique a soma da lista[0] com cada item da lista[1]

a = sum(lista[0])
print(a)
for m in lista[1]:
    print(f'A multiplicação do {a} * {m} = {a*m}') 



# 9) Faça uma divizão inteira do maior número da lista pelo menor numero da lista. Após verifique 
# se o resultado está dentro de uma das listas, se sim, diga qual!
a= max(max(lista[0],lista[1]))
b= min(min(lista[0],lista[1]))
print(f'{a//b}')



# 10) Ferifique se o maior número da lista[0] está dentro da lista[1] e se o menor número da
# lista[1] está na lista[0]
c = (max(lista[0]))
if c in lista[1]:
    print(f'O maior número da lista 0 esta na lista 1')
else:
    print(f'O maior número da lista 0 não está na lista 1')    

d = (min(lista[1]))
if d in lista[0]:
    print(f'O menor valor da lista 1, está na lista 0')
else:
    print(f'O menor valor da lista 1, não está na lista 0')    

# print(f'{lista[1].count(c)}')




