import sys
sys.path.append('/marciano/TrabalhosdePython/Aula33_1/Aula33-4')
from controller.pessoa_controller import PessoaController
from controller.endereco_controler import EnderecoController

pc = PessoaController()
ec = EnderecoController()

for p in pc.listar_todos():
    print(p)

print('\n\n')    

for e in ec.listar_todos_enderecos():
    print(e)
