#calculadora
#Crie um programa que leia dosi numeros inteiros:
#Calcule a soma entre os dois numeros atravez de um método
#Calcule a subtração entre os dois numeros atravez de um método
#Calcule a multiplicação entre os dois numeros atravez de um método
#Calcule a divisão inteira entre os dois   numeros atravez de um método
#Calcule a divisão fracionada entre os dois numeros atravez de um método
#Calcule a resto da divisão entre os dois numeros atravez de um método
#Calcule a raiz entre os dois numeros atravez de um método
#Separa os metodos em outro arquivo

from calculos import soma,sub,mult,div_fra,div_inteira,resto,raiz
num1=float(input('Digite um número: '))
num2=float(input('Digite um outro número'))



print(f'A soma de {num1} e {num2} é = {soma(num1,num2)}\n') 

print(f'A subtração de {num1} e {num2} é = {sub(num1,num2)}\n') 

print(f'A multiplicação  {num1} e {num2} é = {mult(num1,num2)}\n') 

print(f'A divisão inteira  {num1} e {num2} é = {div_inteira(num1,num2)}\n') 

print(f'A divisão fracionada  {num1} e {num2} é = {div_fra(num1,num2)}\n') 

print(f'O resto da divisão dos numeros  {num1} e {num2} é = {resto(num1,num2)}\n')

print(f'a raiz de {num1} e {num2} é ={raiz(num1,num2)}\n')