#JOGO DE ADIVINHAÇÃO
import random
lista = [0,1,2,3,4]
pc = random.choice(lista)
user = int(input('Adivinhe qual numero a maquina pensou? '))
if user == pc:
    print('Você Acertou!')
else:
    print('Você errou!')
print('Numero escolhido pela Maquina {}!'.format(pc))
    #CORREÇÃO
from random import randint
from time import sleep
pc = randint(0,5)
print('-=-'*20)
print('Vou pensar em um numero entre 0 e 5.(-Maquina)')
print('-=-'*20)
user = input('Em que numero pensei?(-User)')
print('Processando..')
sleep(2)
if user == pc:
    print('Você Conseguiu me VENCER!(-Maquina)')
else:
   print('ERROU! Ganhei eu pensei no numero {} (-Maquina)!'.format(pc))
#------------------------------------------------------------------------------------
#RADAR ELETRONICO
limite = 80
multa = 7
vel = float(input('Qual a velocidade do carro: '))
if vel > limite:
    print('Você excedeu o limite da rodovia {}Km/H multa GRAVE'.format(limite))
    tot = (vel - limite) * 7
    print('Valor {:.2f} Reais por 1Km/H. Total à pagar: {:.2f}'.format(multa,tot))
else:
   print('Proibido Ultrapassar 80Km/H')
#-------------------------------------------------------------------------------------
#PAR OU IMPAR
n = int(input('Digite um numero:'))
print('É PAR'if n % 2 == 0 else 'É IMPAR')
#--------------------------------------------------------------------------------------
#CUSTO DE VIAGEM
dist = float(input('Qual a distancia da viagem? '))
''' if dist <= 200:
       passe = dist * 0.50 #50/100
       print('Preço da passagem {:.2f}'.format(passe))
    else:
       passe = dist * 0.45 #45/100
       print('Preço da pasagem: {:.2}'.format(passe)) '''
preco = dist * 0.5 if dist <= 200 else dist * 0.45
print('O preço de sua passagem será {:.2f}'.format(preco))
#----------------------------------------------------------------------------------
#ANO BISSEXTO
from datetime import date
ano = int(input('Qual ano quer analisar? Coloque 0 para analisar o ano atual!'))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é Bissexto'.format(ano))
else:
    print('O ano {} não é Bissexto'.format(ano))
#----------------------------------------------------------------------------------
#MAIOR E MENOR VALOR
a = int(input('Digite um Numero:'))
b = int(input('Digite outro numero:'))
c = int(input('Mais um Numero:'))
menor = a
#Verificando o menor
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
#Verficando o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor {}'.format(menor))
print('O maior valor {}'.format(maior))
#------------------------------------------------------------------------------------
#AUMENTOS MULTIPLOS
sal = float(input('Salario do Funcionario:'))
if sal > 1250:
    nsal = sal + (sal * 10/100)
    print('Novo Salario: R${:.2f}'.format(nsal))
else:
    nsal = sal + (sal * 15/100)
    print('Novo Salário R${:.2f}:'.format(nsal))
#-----------------------------------------------------------------------------------
#ANALISANDO TRIANGULOS
print('-=-'*20)
print('ANALIZADOR DE TRIÂNGULOS:')
print('-=-'*20)
r1 = float(input('Primeiro Segmento:'))
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro Segmento:'))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um TRIANGULO!')
else:
    print('Os segmentos acima NÃO PODEM formar um Triângulo!')