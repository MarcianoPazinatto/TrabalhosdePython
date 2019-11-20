#TUPLAS
numero =[1,2,3,4]#lista
usuario={'nome':'user','password':'12345'}#dicionário
pessoa=('eu','bola',0,13.56,'numeros',numero)#tupla, colocando a lista numero dentro da tupla

print(numero)
print(usuario)
print(pessoa)

numero[1]=5 #mudar valores de uma lista

usuario['password']= 124578 #mudar valores de um dicionário

lista_pessoas=[]#criando uma lista vazia

lista_pessoas.append(pessoa)#colocando a tupla que é pessoa, dentro da lista

print(lista_pessoas)#

print(pessoa[4][1])
