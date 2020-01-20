import sys
sys.path.append('C:/marciano/TrabalhosdePython/TESTE/Aula33-4')
from controller.pessoa_controller import PessoaController

pc = PessoaController()

for p in pc.listar_todos():
    print(p)