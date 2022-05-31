#Validação de Dados
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
print(sexo)
while sexo not in 'MmFf':
    sexo = str(input('Dados Invalido. Por Favor digite seu sexo:')).strip().upper()[0]
print('Dados {} registrado com sucesso"'.format(sexo))
#-------------------------------------------------------------------------------------------
#Jogo da Adivinhação v2.0
from random import randint 
pc = randint(0,10)
print('''Sou seu Computador...
Acabei de pensar em um numero entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
acertou = False
chutes = 0
while not acertou:
   palpite = int(input('Qual é seu palpite? '))
   chutes += 1
   if palpite == pc:
      acertou = True
   elif palpite < pc:
      print('Mais...Tente outra uma vez.')
   elif palpite > pc:
       print('Menos...Tente outra vez.')
print('Acertou com {} tentativas. Parabens!'.format(chutes))
#-------------------------------------------------------------------------------------------
# Criando um Menu de Opções
from time import sleep
v1 = int(input('Primeiro Valor:'))
v2 = int(input('Segundo Valor:'))
opcao = 0
while opcao != 5:
   print('''      [1] Somar
      [2] Multiplicar
      [3] Maior
      [4] Novos numeros
      [5] Sair do programa''')
   opcao = int(input('Qual sua opção:'))
   print('')
   sleep(1)
   if opcao == 1:
      s = v1 + v2
      print('{} + {} == {}.'.format(v1,v2,s))
   elif opcao == 2:
      p = v1 * v2
      print('{} x {} == {}'.format(v1,v2,p))
   elif opcao == 3:
      if v1 > v2:
         print('{} É O MAIOR!'.format(v1))
      elif v1 < v2:
         print('{} É O MAIOR!'.format(v2))
      else:
         print('Os dois numeros são iguais!')
   elif opcao == 4:
       print('Informe o numero novamente:')
       v1 = int(input('Digite o primeiro valor:'))
       v2 = int(input('Digite o Segundo numero:'))
   else:
       print('Opção incorreta. TENTE NOVAMENTE!')
   print('==~'*25)
print('FIM DO PROGRAMA!')
#------------------------------------------------------------------------------------------
# Cálculo do Fatorial
from math import factorial
n = int(input('Digite um numero:'))
f = factorial(n)
print('O fatorial de {} é {}!'.format(n,f))

n = int(input('Digite um numero:'))
c = n
f = 1
print('Calculando {}!'.format(n))
while c > 0:
   f = f * c
   print('{}'.format(c), end='')
   print('x ' if c > 1 else' = ', end='')
   c -= 1
print('{}'.format(f))
#-----------------------------------------------------------------------------------------
# Progressão Aritmética v2.0
primeiro = int(input('Digite o Primeiro Termo:'))
razao = int(input('Digite o Segundo Termo:'))
termo = primeiro
c = 1
while c <= 10:
   print('{} ->'.format(termo), end='')
   termo += razao
   c += 1
print('FIM')
#-----------------------------------------------------------------------------------------
# Super Progressão Aritmética v3.0
primeiro = int(input('Digite o Primeiro Termo:'))
razao = int(input('Digite a Razão:'))
termo = primeiro
c = 1
total = 0
mais = 10
while mais != 0:
   total = total + mais
   while c <= total:
      print('{} ->'.format(termo), end='')
      termo += razao
      c += 1
   print('PAUSA')
   mais = int(input('Quantos termos você quer mostrar a mais?'))
print('Progressão finalizada com {} termos mostrados.'.format(total))
#-------------------------------------------------------------------------------------------
# Sequência de Fibonacci v1.0
print('-='*20)
print('Sequencia de fibonacci')
n = int(input('Quantos termos você quer mostrar:'))
t1 = 0
t2 = 1
print('~'*20)
print('{} -> {}'.format(t1,t2), end='')
c = 3
while c <= n:
   t3 = t1 + t2
   t1 = t2
   t2 = t3
   print('-> {}'.format(t3), end='')
   c += 1
print('-> FIM')
#--------------------------------------------------------------------------------------------
# Tratando vários valores v1.0
c = tot = s = 0
while c != 999:
   n = int(input('Digite um numero [999 para parar]: '))
   c = n
   if n != 999:
      tot += 1
      s += n
print('Você digitou {} números e a soma entre eles foi {}'.format(tot, s))
#---------------------------------------------------------------------------------------------
# Maior e Menor valores
c = tot = s = 0
while c != 999:
   n = int(input('Digite um numero [999 para parar]: '))
   c = n
   if n != 999:
      tot += 1
      s += n
print('Você digitou {} números e a soma entre eles foi {}'.format(tot, s))
#---------------------------------------------------------------------------------------------
# Maior e Menor valores
resp = 'S'
tot = m = s = maior = 0
while resp != 'N':
   n = int(input('Digite um numero: '))
   menor = n
   resp = str(input('Quer continuar:[S/N]')).upper()
   tot += 1
   s = s + n
   if n > maior:
      maior = n
   if n < menor:
      menor = n
m = s / tot
print('Você digitou {} numeros e a média foi {:.2f}'.format(tot,m))
print('O maior valor foi {} e o menor {}'.format(maior, menor))