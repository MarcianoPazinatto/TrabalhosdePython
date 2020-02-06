#--- Exercício 3 - Foreach
#--- Escreva programa que leia as notas (4) de 10 alunos
#--- Armazene as notas e os nomes em listas
#--- Imprima:
#           1- O nome dos alunos 
#           2- Média do aluno
#           3- Resultado (Aprovado>=7.0)

listanome=[]
listanotas=[]
for i in range (0,3):
    for i in range(0,1):
        listanome.append(input(f'Digite o nome  do aluno {i+1} : '))
    for i in range(0,4):
        listanotas.append(int(input(f'Digite as notas {i+1}: '))) 

nota1=(sum(listanotas[:4])/4)
print(f'Media do aluno {listanome[0]} é {nota1}')
if nota1>=7:
    print('aprovado')
else:
    print('reprovado')
    
nota2=(sum(listanotas[4:8])/4)
print(f'Media do aluno {listanome[1]} é {nota2}')
if nota2>=7:
    print('aprovado')
else:
    print('reprovado')
nota3=(sum(listanotas[8:12])/4)
print(f'Media do aluno {listanome[2]} é {nota3}')
if nota3>=7:
    print('aprovado')
else:
    print('reprovado')

'''nota4=(sum(listanotas[12:16])/4)
print(f'Media do aluno {listanome[3]} é {nota4}')
if nota4>=7:
    print('aprovado')
else:
    print('reprovado')
nota5=(sum(listanotas[16:20])/4)
print(f'Media do aluno {listanome[4]} é {nota5}')
if nota5>=7:
    print('aprovado')
else:
    print('reprovado')
nota6=(sum(listanotas[20:24])/4)
print(f'Media do aluno {listanome[5]} é {nota6}')
if nota6>=7:
    print('aprovado')
else:
    print('reprovado')
nota7=(sum(listanotas[24:28])/4)
print(f'Media do aluno {listanome[6]} é {nota7}')
if nota7>=7:
    print('aprovado')
else:
    print('reprovado')
nota8=(sum(listanotas[28:32])/4)
print(f'Media do aluno {listanome[7]} é {nota8}')
if nota8>=7:
    print('aprovado')
else:
    print('reprovado')
nota9=(sum(listanotas[32:36])/4)
print(f'Media do aluno {listanome[8]} é {nota9}')
if nota9>=7:
    print('aprovado')
else:
    print('reprovado')
nota10=(sum(listanotas[36:40])/4)
print(f'Media do aluno {listanome[9]} é {nota10}')
if nota10>=7:
    print('aprovado')
else:
    print('reprovado')
print(listanotas)  
print(listanome)'''


'''for i in range(0,12,4):
   sum(listanotas)
    print(listanotas)'''