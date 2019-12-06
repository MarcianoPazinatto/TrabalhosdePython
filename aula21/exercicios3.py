# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Crie um metodo que leia 5 valores inteiros e retorne uma lista.
# Esta função deve ter tratamento de excessão evitando erro ValueError.

# 2 - Com a lista retornada, faça a multiplicação por 5 e salve o resultado
# em outra lista.

# Imprima a lista resultante

def numeros():
    lista=[]
    for b in range(5):
        b=int(input('Digite um numero inteiro: '))
        lista.append(b)
    return lista    

a=numeros()
print(a)

listaum=[]
for num in a:
    mm=num*5
    #print(mm)
    listaum.append(mm)
print(listaum)
