nome='marciano' ' ' 'Pazinatto'
print((nome).count('a'))#conta quantos caracteres tem 
print((nome).lower())#diminui os carácteres 
print((nome).upper())#aumenta os carácteres
print((nome).split(' '))#remove o que for colocado dentro dos parênteses 
print((nome).strip())
print((nome).capitalize())#deixa o primeiro carácter da palavra em maiúsculo


pessoa=[" ","boa ", "Bonita", "barata "]
print(pessoa)
print((' nem ' ).join(pessoa))
frase='banana'
print('a'.join(frase))
print(frase[2:5])
print(pessoa.count(" bonita".strip().capitalize()))