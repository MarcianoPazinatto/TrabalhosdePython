lista1=[]
lista2=['pessoa1', 'pessoa2','pessoa3']
lista3=[1,2,3,4,5]
lista4=(1,'Maykon',1.3)



print(lista1)
print(lista2)
print(lista3)

lista1.append(lista2)
lista1.append(lista3)

print(lista1)

lista_perguntas=[input('Digite algo:' ), input('digite outro')]
print(lista_perguntas)

posicao=int(input('Digite a posição '))
print(lista2[posicao-1])