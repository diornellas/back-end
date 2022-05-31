# CONTAGEM DE 2 CASAS
for c in range(0,3,2):
    print(c)
# CONAGEM REGRESSIVA
for c in range(10,0,-1):
   print(c)
# CONTAGEM COM INTERAÇÃO
n = int(input('Ate que numero vai ser a contagem:'))
for c in range(0,n+1):
    print(c)

i = int(input('Ate que numero vai ser a contagem:'))
f = int(input('Qual sera o fim da contagem:'))
passo = int(input('Em quantos passos sera a contagem?'))
for c in range(i,f+1, passo):
    print(c)
# SOMA
s = 0
for c in range(1,4):
   n = int(input('Digite o {}o Numero'.format(c)))
   s = s + n
   print('A soma de todos os valores foi {}'.format(s))