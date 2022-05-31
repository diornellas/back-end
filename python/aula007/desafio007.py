#ANALIZADOR DE TEXTO
nome = str(input('Digite seu nome completo:')).strip()#Tira o [ESPAÇO] do começo e do fim
print('Analisando seu nome...')
print('Seu nome em letras maiúscula é {}.'.format(nome.upper()))
print('Seu nome em minúscula é {}.'.format(nome.lower()))
print('Seu nome tem {} letras'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letra'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))
#-----------------------------------------------------------------------------------------
# SEPARANDO DIGITOS DE UM NUMERO
n = int(input('Digite um numero:'))
print('Analisando numero digitado {}...'.format(n))
n = str(n)
print('Unidade: {}'.format(n[3]))
print('Dezena: {}'.format(n[2]))
print('Centena {}'.format(n[1]))
print('Milhar: {}'.format(n[0]))

n = int(input('Digite um numero:'))
print('Analisando numero digitado {}'.format(n))
u = n // 1 % 10
d = n// 10 % 10
c = n // 100 % 10
m = n // 1000 % 10
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
#------------------------------------------------------------------------------------------
#VERIFIANDO AS PRIMEIRAS LETRAS DE UM TEXTO
cid = str(input('Digite o nome da cidade:')).strip()
print(cid[0:6].upper() == 'SANTOS')
#------------------------------------------------------------------------------------------
#PROCURANDO UMA STRING DENTRO DE OUTRA
nome = str(input('Qual é o seu nome? ')).strip()
print('Seu nome tem Silva? {}'.format('silva' in nome.lower()))
#------------------------------------------------------------------------------------------
#PRIMEIRA E ULTIMA OCORRENCIA DE UMA STRING
frase = str(input('Digite uma frase: ')).upper().strip()
print('Esta frase tem {} letras A'. format(frase.count('A')))
print('A primeira letra "A" aparece na posição {}'.format(frase.find('A')+1))
print('A ultima letra "A" aparece na posição {}'.format(frase.rfind('A')+1))
#------------------------------------------------------------------------------------------
#PRIMEIRO E ULTIMO NOME DE UMA PESSOA
n = str(input('Digite o Nome Completo: ')).strip()
nome = n.split()
print('Muito Bom lhe Conhecer!')
print('Primeiro nome: {}'.format(nome[0]))
print('Seu Segundo nome {}'.format[len(nome)-1])