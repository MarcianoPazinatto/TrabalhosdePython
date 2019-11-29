#Aula 16
#Cadastro de Playlist
#lendo música, artista e album

from faixa import criar_faixa, salvar_faixa

#######################################################################IMPORTANDO DADOS DAS FUNÇÕES



#######################################################################INSERINDO DADOS

musica=input('Digite uma música: ')
artista=input('Digite o nome do artista: ')
album= input('Digite o album: ')

#######################################################################CHAMAR DAS FUNÇÕES AS OPERÇÕES REALIZADAS

faixa=criar_faixa(musica, album, artista)
salvar_faixa(faixa)