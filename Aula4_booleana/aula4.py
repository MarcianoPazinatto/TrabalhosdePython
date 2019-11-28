n1=int(input('Digite um número: '))
n2=int(input('Digite outro número '))
soma=n1+n2
sub=n1-n2
mul=n1*n2
div=n1/n2

print(f'Soma: {soma}, Subtração: {sub}, multiplicação: {mul}, divisão: {div}')

if n1>n2:
    print('O primeiro número é maior que o segundo')
if n1==n2:
    print('Números são iguais')
else:
    print('O segundo número é maior')
