#
lista = ['Mateus', 'Matheus','Marcela','Nicole', 'Tonho','Pablo']
for i in range(0,6):
    print(lista[i])
#Exemplificando o problema do uso de for em lista usando range
lista.append('Natan')    
for sortudo in lista:
    print(sortudo)
#for usando os elementos da propria lista foreach
numero=10
for i in range(0,11):
    print(f'{i} x {numero} = {i*numero}')