idade = 18
validador=False
validador= True
validador=(idade==18)
print(validador)

if validador:
    print('Maior')

validador=(idade>18)
print(validador)    

validador=(idade<18)
print(validador)

validador=(idade>=18)
print(validador)

validador=(idade<=18)
print(validador)

validador= not True # not inverte o valor expresso
print(validador)
validador = not False
print(validador)

sorteado='Marcela'

validador=(sorteado=='Mateus' and sorteado=='Marcela')
print(validador)
validador=(sorteado=='Mateus' or sorteado=='Marcela')
print(validador)
