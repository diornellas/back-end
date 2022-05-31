#ESTRUTURAS CONDICIANAIS
carro = float(input('Quantos anos tem seu carro:'))
if carro <= 3:
    print('Carro Novo')
else: 
   print('Carro Velho')
#print('Seu carro esta {}'.format(carro))
#print('Carro novo'if carro <= 3 else 'Carro velho')
print('FIM')

nome = str(input('Digite seu nome: '))
if nome == 'Mateus':
   print('Que nome lindo!')
print('E aí {}'.format(nome))

n1 = float(input('Digite a Primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('Sua média é {}'.format(m))
print('Parabéns'if m>=6 else'Estude Mais um pouco!')

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
m = (n1 + n2) / 2
print('Sua Média é: {}'.format(m))
if m < 5:
   print('Reprovado')
else:
   print('Aprovado')
