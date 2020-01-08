# A HBSIS Airlines é uma empresa de aviação que opera rotas internacionais a partir de Blumenau.
# Cada voo é tripulado por seis elementos, sendo que estes se dividem em dois grupos: a tripulação
# técnica e a tripulação de cabine. A tripulação técnica é constituída pelo piloto e dois oficiais. 
# A tripulação de cabine é constituída pelo chefe de serviço de voo e duas comissárias.
# O transporte dos tripulantes entre o terminal e o avião é efetuado através de um Smart Fortwo, que
# é um veículo que leva apenas duas pessoas. Por política da empresa, apenas o piloto e o chefe de
# serviço de voo podem dirigir este veículo. É também política da empresa que nenhum dos oficiais
# pode ficar sozinho com o chefe de serviço de bordo, e nem nenhuma das comissárias pode ficar
# sozinha com o piloto.  No terminal de embarque estão os seis tripulantes e ainda um policial 
# junto com um presidiário. Estes oito elementos terão que embarcar segundo as regras descritas acima. 
# A empresa não coloca nenhum limite para o número de viagens entre o terminal e o avião.
# Por motivos de segurança o presidiário não pode ficar sozinho em momento algum com os
# tripulantes sem a presença do policial, nem no terminal e nem no avião. De forma a facilitar o
# processo, a empresa autorizou que o policial pudesse dirigir o veículo também.

# Requisitos:
# 1 - Sempre que o Fortwo se mover, apresentar no console quando ele chega no destino
# 2 - Sempre que acontecer um embarque, apresentar quais elementos estão embarcando
# 3 - Sempre que acontecer um embarque no terminal, apresentar quem está no terminal
# 4 - Sempre que acontecer um embarque no avião, apresentar quem está no avião
# 5 - Deve ser feito em Python

#tripulação técnica = piloto, oficial1 e oficial2
#tripulação de cabine = chefe de serviço de voo, comissária1 e comissária2
#passageiros = policíal e presidiario

#*************************** salvando o arquivo em txt ************

def salvar_aviao(aeroporto):
    arq = open('aviao.txt','w')
    for pessoa in aeroporto:
        arq.write(f'{pessoa}\n')
    arq.close()
#*************************** lendo e salvando em uma lista************
def ler():
    aeroporto1=[]
    arq = open('aviao.txt','r')
    for linha in arq:
        linha = linha.strip()
        aeroporto1.append(linha)      
    arq.close() 
    return aeroporto1  

#*************************** lista das pessoas que estão no aeroporto ************
aeroporto = ['piloto','oficial_A','oficial_B','chefe','comissaria_A',
                            'comissaria_B','policial','presidiario']
aviao = []

#*************************** função que enviara do aeroporto ao avião ************
def viagem ():  

    if len(aeroporto) <= 2:  
        print(f'Viagem ao avião: {aeroporto[0]} e {aeroporto[1]}') 
        aviao.append(aeroporto.pop(0))
        aviao.append(aeroporto.pop(0))
                        
                
    else:
        if aeroporto[1]=='piloto' or aeroporto[1]=='chefe' or aeroporto[1]=='policial':
            aeroporto[0],aeroporto[1]=aeroporto[1],aeroporto[0]
            print(f'Estão no aeroporto: {aeroporto}')
            print(f'Viagem ao avião: {aeroporto[0]} e {aeroporto[1]}')
            aviao.append(aeroporto.pop(1))
                    
        else:
            print(f'Estão no aeroporto: {aeroporto}')
            print(f'Viagem ao avião: {aeroporto[0]} e {aeroporto[1]}')
            aviao.append(aeroporto.pop(1))
                
    if aeroporto:
        print(f'Voltando para aeroporto: {aeroporto[0]}')
        print(f'Dentro do avião {aviao}')
        print('\n') 
    else:
        print(f'Todos no avião {aviao}')  

for i in range(0,7):
    (viagem())
print('\n')
salvar_aviao(aviao)

a=ler()
#*************************** imprimindo o txt ************
print(a)