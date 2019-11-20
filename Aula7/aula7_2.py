#----Exercício 1 - Dicionário
#----Escreva programa que leia os dados da cerveja
#----Cerveja, Marca, Tipo, IBU, ABV, EBC, Volume
#----Crie um dicionário para armazenar os dados
#----Imprima os dados do dicionário(não dicionário completo)
'''
dicionario={}
dicionario={'marca':input('Digite a marca: '),'Tipo':input('Digite um tipo: '),'IBU':input('Digite IBU: '),'ABV':input('Digite o ABV'),'EBC':input('Digite o EBC: '),'Volume':input('Digite o Volume: ')}
print(f"Marca :{dicionario['marca']}\nTipo: {dicionario['Tipo']}\n IBU: {dicionario['IBU']}\n'ABV: {dicionario['ABV']}\n EBC: {dicionario['EBC']}\nVolume:{dicionario['Volume']} ")
'''

cerveja={}
cerveja['Marca']= (input('Digite a marca:'))
cerveja['Tipo']= (input('Digite o tipo'))
cerveja['IBU']=int(input('Digite o IBU'))
cerveja['ABV']=float(input('Digite o ABV'))