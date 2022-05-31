#QUEBRANDO UM NUMERO
#MANEIRA SIMPLES DE MOSTRAR A PARTE INTEIRA DE UM NUMERO
n = float(input('Digite um numero:'))
print('O numero digitado foi {} e sua parte inteira é {}'.format(n, int(n)))
#MANEIRA COM BIBLIOTECAS
from cmath import sin
import math
n = float(input('Digite um numero:'))
print('O valor digitado foi {} e sua parte inteira é {}'.format(n, math.trunc(n)))
#--------------------------------------------------------------------------------------
#CATETOS E HIPOTENUSA
#MANEIRA SIMPLES DE CALCULAR
co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#MANEIRA COM BIBLIOTECAS
import math
co = float(input('Comprimento do Cateto Oposto:'))
ca = float(input('Comprimento do cateto adjacente:'))
hi = math.hypot(co,ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))
#--------------------------------------------------------------------------------------
#SENO, COSSENO, TANGENTE
import math
angulo = float(input('Digite o angulo: '))
sen = math.sin(math.radians(angulo))
print('O angulo de {} tem o SENO de {:.2f}'. format(angulo,sen))
cos = math.cos(math.radians(angulo))
print('O angulo de {} tem o COSENO de {:.2f}'.format(angulo,cos))
tan = math.tan(math.radians(angulo))
print('O angulo de {} tem a tangente {:.2f}'.format(angulo,tan))

from math import radians, sin, cos, tan
angulo = float(input('Digite o angulo: '))
sen = sin(radians(angulo))
print('O angulo de {} tem o SEN de {}'.format(angulo,sen))
coss = cos(radians(angulo))
print('O angulo de {} tem o COSSENO de {}'.format(angulo,coss))
tangen = tan(radians(angulo))
print('O angulo de {} tem a TANGENTE {}'.format(angulo,tangen))
#----------------------------------------------------------------------------------------
#SORTEANDO UM ITEM NA LISTA
import random
n1 = str(input('Primeiro aluno: '))
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))

from random import choice
n1 = str(input('Primeiro aluno: '))
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
#---------------------------------------------------------------
#SORTEANDO UMA ORDER NA LISTA
import random
n1 = str(input('Primeiro aluno: '))
n2 = input('Segundo aluno: ')
n3 = input('Terceiro aluno: ')
n4 = str(input('Quarto aluno: '))
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('A ordem de apresentação será:')
print(lista)

from random import shuffle
n1 = input('Primeiro aluno:')
n2 = input('Segundo aluno:')
n3 = input('Terceiro aluno:')
n4 = input('Quinto aluno:')
lista = [n1,n2,n3,n4]
shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)