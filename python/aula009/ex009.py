# SENÃO SE == ELIF 
nome = str(input('Digite seu nome:'))
sexo = str(input('Qual o sexo?[Masculino/Feminino]'))
if nome == 'Mateus':
    print('Você é foda!')
if sexo == 'Masculino':
    print('Procura Trabalhar!')
elif sexo == 'Feminino':
    print('oii')
print('Tenha uma boa noite {}'.format(nome))