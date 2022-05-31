#ANTECESSOR e SUCESSOR
n = int(input('Digite um numero:'))
a = n - 1
s = n + 1
print('O antecessor de {} é {} e o sucessor é {}'.format(n,a,s))
#FORMA SIMPLIFICADA DE ANTECESSOR E SUCESSOR
n = int(input('Digite um numero:'))
print('Antecessor de {}: {}, sucessor {}'.format(n, (n-1),(n+1)))
#--------------------------------------------------------------------
# DOBRO, TRIPLO, RAIZ QUADRDADA
n= int(input('Digite um numero:'))
dob = n * 2
trip = n * 3
raiz = pow(n, (1/2))
print('O dobro de {} é {}, o triplo {}'.format(n,dob,trip))
print('A raiz quadrada de {} é {}.'.format(n,raiz))
#--------------------------------------------------------------------
# MÉDIA DO ALUNO
nome = str(input('Nome do aluno:'))
n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('A media de {} é {}'.format(nome,m))
#--------------------------------------------------------------------
#CONVERSOR DE MEDIDAS
medida = float(input('Digite uma distancia em metros:'))
cm = medida * 100
mm = medida *1000
print('{} metros é {} centimetros e {} milimetros'.format(medida, cm, mm))
#--------------------------------------------------------------------
#TABUADA
num = int(input('Digite o numero da tabuada:'))
print('{} x {} = {}'.format(num,0,num*0))
print('{} x {} = {}'.format(num,1,num*1))
print('{} x {} = {}'.format(num,2,num*2))
print('{} x {} = {}'.format(num, 3,num*3))
print('{} x {} = {}'.format(num,4,num*4))
print('{} x {} = {}'.format(num,5,num*5))
print('{} x {} = {}'.format(num,6,num*6))
print('{} x {} = {}'.format(num,7,num*7))
print('{} x {} = {}'.format(num,8,num*8))
print('{} x {} = {}'.format(num,9,num*9))
print('{} x {} = {}'.format(num,10,num*10))
#---------------------------------------------------------------------
#CONVERSOR DE MOEDAS
saldo = float(input('Quantos Reais você R$:'))
dolar = saldo / 5.06
print('Com R${:.2f} na cotação atual compra US{:.2f}'.format(saldo, dolar))
#---------------------------------------------------------------------
#PINTANDO PAREDE
larg = float(input('Largura da Parede:'))
alt = float(input('Altura da Parede:'))
area = larg * alt
print('Sua parede tem a dimensão de {} x {} e a área de {}'.format(larg,alt,area))
tinta = area / 2
print('Para pintar essa parede você precisara de {}l te tinta!'.format(tinta))
#----------------------------------------------------------------------
#CALCULANDO  DESCONTOS
preco = float(input('Qual valor do produto:'))
desc = preco * (5/100)
prcDesc = preco - desc
print('Valor do produto R${:.2f}, valor com desconto de 5% R${:.2f}'.format(preco, prcDesc))
#-----------------------------------------------------------------------
#REAJUSTE SALARIAL
sal = float(input('Qual é salário do Funcionario:'))
aum = sal + (sal * 15/100)
print('Um Funcionario que ganhava R${:.2f}, com 15% de aumento, passa a ganhar R${:.2f}'.format(sal, aum))
#------------------------------------------------------------------------
#CONVERSÃO DE TEMPERATURA
c = float(input('Informe a temperatura:'))
f = ((9*c)/5) + 32
print('A temperatura de {} GRAUS corresponde {} FAHRENHEIT'.format(c,f))
#-------------------------------------------------------------------------
#ALUGUEL DE CARROS
dias = float(input('Quantos dias alugados?'))
km = float(input('Quantos Km rodados?'))
tot = dias * 60 + km * 0.15
print('O total a pagar é de R${:.2f}'.format(tot))