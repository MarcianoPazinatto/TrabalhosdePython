nota1=int(input('digite a primeira nota: '))
nota2=int(input('Digite a segunda nota: '))
nota3=int(input('Digite a terceira nota: '))
nota4=int(input('Digite a quarta nota: '))

if (nota1>nota2)&(nota1>nota3)&(nota1>nota4):
    print(f'nota {nota1} é maior')
elif (nota2>nota1)&(nota2>nota3)&(nota2>nota4):
    print(f'nota {nota2} é maior')
elif (nota3>nota1)&(nota3>nota2)&(nota3>nota4):
    print(f'nota {nota3} é maior')
elif (nota4>nota1)&(nota4>nota2)&(nota4>nota3):
    print(f'nota {nota4} é maior')
elif(nota1==nota2)&(nota2==nota3)&(nota3==nota4):
    print('notas iguais')    
   
<<<<<<< HEAD
=======
   
>>>>>>> a74527b1a2afd16b8190703f48187523a66ed9c8

if (nota1<nota2)&(nota1<nota3)&(nota1<nota4):
    print(f'nota {nota1} é menor')
elif(nota2<nota1)&(nota2<nota3)&(nota2<nota4):
    print(f'nota {nota2} é menor')
elif (nota3<nota1)&(nota3<nota2)&(nota3<nota4):
    print(f'nota {nota3} é menor')    
elif (nota4<nota1)&(nota4<nota2)&(nota4<nota3):
    print(f'nota {nota4} é menor')


if(nota1==nota2):
    print('nota 1{nota1} e nota 2{nota2}' são iguais)    

if(nota2==nota3):
    print('nota 2{nota2} e nota 3{nota3}' são iguais)    

if(nota1==nota3):
    print('nota 1{nota1} e nota 3{nota3}' são iguais)        

if(nota1==nota4):
    print('nota 1{nota1} e nota 4{nota4}' são iguais)   

if(nota2==nota4):
    print('nota 2{nota2} e nota 4{nota4}' são iguais)   

if(nota3==nota4):
    print('nota 3{nota3} e nota 4{nota4}' são iguais)   

media=(nota1+nota2+nota3+nota4)/4
print(f'Media: {media}')

if media>7:
    print('aprovado')
else:
    print('reprovado')    