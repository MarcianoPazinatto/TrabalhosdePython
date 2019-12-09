# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Faça um programa que abra um arquivo.txt
# 2 - Trate para que não tenha ao abrir o arquivo
# 3 - Caso não haja erro apareça a mensagem de "Arquivo aberto"
# 4 - Se houver erro, apareça a mensagem 
# "Envidando dados para função tratar_dados() "

# Ao finalizar, obrigar o fechamento do arquivo

# dica: linha 204 do arquivo execoes.py
# Aula 21 - 06-12-2019
# Como Tratar e Trabalhar Erros!!!

# 1 - Faça um programa que abra um arquivo.txt
# 2 - Trate para que não tenha ao abrir o arquivo
# 3 - Caso não haja erro apareça a mensagem de "Arquivo aberto"
# 4 - Se houver erro, apareça a mensagem 
# "Envidando dados para função tratar_dados() "

# Ao finalizar, obrigar o fechamento do arquivo

# dica: linha 204 do arquivo execoes.py
def abrir():
    try:
        arquivo = open('lista.txt','a')
    except OSError:
        print('Envidando dados para função tratar_dados()')
    else:
        print('Arquivo aberto')
    finally: 
        if 'arquivo' in dir():
	        print('Fechando Arquivo')
        arquivo.close() 

abrir()