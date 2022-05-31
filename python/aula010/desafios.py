# CONTAGEM REGRESSIVA
from time import sleep
print('CONTAGEM PARA QUEIMA DE FOGOS...')
for c in range(10,1-1,-1):
   print(c)
   sleep(1)
print('PoW poRoooUUU Pum Pa Cadushee')
#--------------------------------------------------------------------------------
# CONTAGEM DE PARES
s = 0
for c in range(1,50+1):
    if c % 2 == 0:
       s = s + 1
print('De 1 a 50 exitem {} pares!'.format(s))
#---------------------------------------------------------------------------------
# IMPARES MULTIPLOS DE TRÊS
for c in range(1,500+1):
    if (c%3==1):
        impar = c
        print(impar)
#---------------------------------------------------------------------------------
# TABUADA EM REPETIÇÃO
t = int(input('Qual tabuada quer ver?'))
c = 1
for c in range(c, 10+1):
    r = t * c
    print('{} x {} = {}'.format(t,c,r))
#---------------------------------------------------------------------------------
# SOMA DOS PARES
s = 0
for c in range(1,6+1):
    n = int(input('Digite um numero:'))
    if n % 2 == 0:
        s = s + n
print('A soma dos numeros pares é {}'.format(s))
#---------------------------------------------------------------------------------
# PROGRESSÃO ARITMETICA
print('='*35)
print('     10 TERMOS DE UMA PA')
print('='*35)
#
termo = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))
decimo = termo + (10-1) * razao
for c in range(termo, decimo+1, razao):
    print('{}'.format(c), end=' -> ')
#---------------------------------------------------------------------------------
# NUMEROS PRIMOS
n = int(input('Digite um numero:'))
tot = 0
for c in range(1,n+1):
    if n % c == 0:
        tot = tot + 1
    print('{}'.format(c), end=' ')
print('\nO numero {} é divisivel por ele mesmo {} vezes'.format(n,tot))
if tot == 2:
    print('É por isso que ele é PRIMO!')
else:
    print('É por isso que ele não é primo!')
#---------------------------------------------------------------------------------
# DETECTOR DE PALIDROOMO
frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('Você digitou a frase {}.'.format(junto))
for letra in range(len(junto)-1, -1, -1):
    inverso = inverso + junto[letra]
print(junto, inverso)
if inverso == junto:
    print('Temos um PALÍNDROMO!')
else:
    print('A frase digitada não é um PALÍNDROMO!')
#---------------------------------------------------------------------------------
# GRUPO DA MAIORIDADE
from datetime import date
atual = date.today().year
velhos = 0
novos = 0
for c in range(1,7):
    ano = int(input('Em que ano a {}o pessoa nasceu? '.format(c)))
    idade = atual - ano
    if idade > 18:
        velhos = velhos + 1
    else:
        novos = novos + 1
print('Ao todo tivemos {} pessoas maiores de idade!'.format(velhos))
print('E também tivemos {} pessoas menores de idade!'.format(novos))
#---------------------------------------------------------------------------------
# MAIOR E MENOR DA SEQUENCIA
for c in range(1,5):
    peso = float(input('Peso da {}o pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior Peso LIDO foi {:.2f}KG'.format(maior))
print('O menor Peso LIDO foi {:.2f}KG'.format(menor))
#---------------------------------------------------------------------------------
# ANALIZADOR COMPLETO
somaIdade = 0
mediaIdade = 0
maiorIdadeHomem = 0
menorDe20 = 0
nomeVelho = ''
for c in range(1,5):
    print('-'*6, '{}• PESSOA'.format(c), '-'*6)
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F]')).strip() 
    somaIdade += idade
    if c == 1 and sexo in 'Mm':
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Mm' and idade > maiorIdadeHomem:
        maiorIdadeHomem = idade
        nomeVelho = nome
    if sexo in 'Ff' and idade < 20:
        menorDe20 += 1
mediaIdade = somaIdade / 4
print('Media de Idade {}:'.format(mediaIdade))
print('Homem mais velho {} com {} anos'.format(nomeVelho,maiorIdadeHomem))
print('Ao todo são {} mulheres menores de 20 anos'.format(menorDe20))
#---------------------------------------------------------------------------------------
# Cálculo do Fatorial
n = int(input('Digite um numero:'))
f = 1
for c in range(1,n+1):
   print('{} '.format(c), end='')
   print('x ' if c < n else '= ', end='')
   f = f * c
print('{}!'.format(f))
