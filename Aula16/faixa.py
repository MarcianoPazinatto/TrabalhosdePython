########################################################FUNÇÃO PARA CRIAÇÃO DA FAIXA MÚSICAL ATRÁVEZ DA BIBLIOTÉCA
def criar_faixa(musica,album,artista):
    faixa ={'musica':musica,'artista':artista,'album':album} 
    return faixa

########################################################FUNÇÃO PARA ARMAZENAR EM ARQUIVO TXT A FAIXA, OU AS FAIXAS DE MÚSICA    

def salvar_faixa(faixa):
    arquivo = open('Aula16/faixas.txt','a')
    arquivo.write(f"{faixa['musica']};{faixa['album']};{faixa['artista']}\n")
    arquivo.close()

#########################################################FUNÇÃO REFERENTE A LEITURA DAS FAIXAS

def ler_faixa():
    lista_faixa=[]
    arquivo = open('Aula16/faixas.txt','r')    
    for linha in arquivo:
        linha=linha.strip()
        dados_faixa=linha.split(';')
        faixa=criar_faixa(dados_faixa[0],dados_faixa[1],dados_faixa[2])
        lista_faixa.append(faixa)
    arquivo.close()        
    return lista_faixa