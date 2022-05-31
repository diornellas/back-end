#UTILIZANDO MODULOS
#-----------------------------------------------
import imp
import math 
n = int(input('Digite um numero:'))
r = math.sqrt(n)
print('A raiz quadrada de {} é {}'.format(n,r))

import math
n = int(input('Digite um numero:'))
raiz = math.sqrt(n)
print('A raiz quadrada de {} é {}'.format(n,math.ceil(raiz)))

from math import sqrt
n = int(input('Digite um numero:'))
raiz = sqrt(n)
print('A raiz quadrada de {} é {}'.format(n, raiz))