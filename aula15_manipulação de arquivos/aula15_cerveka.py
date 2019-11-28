def salvar_cerveja(dicio_cerveja):
    arq=open('cerveja.txt','w')
    arq.write(f"{dicio_cerveja['tipo']};{dicio_cerveja['marca']};{dicio_cerveja['teor']}\n")
    arq.close()

def ler():
    lista=[]
    arq=open('cerveja.txt','r')
    for linha in arq:
        linha=linha.strip()
        linha_linha=linha.split(';') 
        cerveja={'tipo':linha_linha[0],'marca':linha_linha[1],'teor':linha_linha[2]}   
        lista.append(cerveja)
    arq.close()  
    return lista

tipo=input('Digite o tipo de cerveja: ')     
marca=input('Digite a marca da cerveja: ') 
teor=float(input('Digite o teor da cerveja: '))
cerveja={'tipo':tipo,'marca':marca,'teor':teor}
salvar_cerveja(cerveja)

lista=ler()
for p in ler():
    print(f"{p['tipo']} - {p['marca']} - {p['teor']}")