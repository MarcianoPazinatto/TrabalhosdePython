import sys
sys.path.append('/marciano/TrabalhosdePython/Aula37pronto_trabalhoSquad')
from controller.squad_controller import SquadController
from controller.framework_controller import FrameworkController
from controller.linguagem_controller import LinguagemController

l = LinguagemController()
sc = SquadController()
f = FrameworkController()

# for p in sc.listar_todos():
#     print(p)

for g in f.listar_todos():
    print(g)    

# print('\n')

# for l in f.listar_todos():
#     print(l)    