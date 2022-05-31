#Interrompendo repetições while (INTERPOLAÇÃO)
n = s = 0
while True:
   n = int(input('Digite um numero:'))
   if n == 999:
      break
   s += n
print(f'A soma vale {s}')
#print('A soma vale: {}'.format(s))
#------------------------------------------------------
idade = int(input('Qual sua idade?'))
nome = str(input('Digite seu nome:'))
salario = float(input('Qual salário?'))
print(f'{nome} tem {idade} anos e seu salário é R${salario:.2f}')