# Aula 15 - 28-11-2019
#Manipulação de Arquivos

#arquivo=open('aula15.txt', 'a')
#arquivo.write('Texto')
#arquivo.close()

arquivo=open('aula15.txt','r')
for linha in arquivo:
    print(linha)
arquivo.close()