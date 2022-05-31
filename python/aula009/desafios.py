# APROVANDO EMPRESTIMO
preco = float(input('Digite o valor da casa:'))
sal = float(input('Qual o salario do comprador:'))
anos = int(input('Em quantos anos vai financiar:'))
excesso = sal * (30/100)
parcelas = (preco / anos) / 12
print('Para pagar uma casa de R${:.2f} em {} anos'.format(preco,anos), end=(' '))
print('as parcela são {}'.format(parcelas))
if (parcelas <= excesso):
   print('Empréstimo consedido!')
else:
   print('EMPRESTIMO NEGADO PASSOU SEU SALÁRIO!!!')
#-------------------------------------------------------------------------------------------
#CONVERSOR DE BASES
num = int(input('Digite um numero:'))
print('''Escolha uma opção
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua opção:'))
if (opcao == 1):
   print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif (opcao == 2):
   print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif (opcao == 3):
   print('{} convertido para HEXADECIMAL é igual {}'.format(num,hex(num)[2:]))
else:
   print('Numero invalido Tente Novamente!')
#-------------------------------------------------------------------------------------------
# COMPARANDO NUMEROS
n1 = int(input(('Digite um numero:')))
n2 = int(input('Digite outro numero:'))
if (n1 > n2):
    print('O primeiro Valor é Maior')
elif(n2 > n1):
    print('O segundo valor é maior')
#-------------------------------------------------------------------------------------------
# ALISTAMENTO MILITAR
print()
print('             A IDADE OBRIGATÓRIA PARA ALISTAR-SE É DE 18 ANOS')
print()
from datetime import date
nasc = int(input('Ano de nascimento:'))
atual = date.today().year
idade = atual - nasc
print('Quem nasceu em {} tem {} anos em {}.'.format(nasc,idade,atual))
if idade > 18:
   prazo = idade - 18
   print('Você ja deveria ter alistado há {} anos.'.format(prazo))
   ano = atual - prazo
   print('Seu alistamento foi em {}.'.format(ano))
elif idade == 18:
   print('Seu alistamento é esse ano!')
elif idade < 18:
   faltam = 18 - idade
   print('Você não atingiu a idade necessaria faltam {} anos.'.format(faltam))
   ano = atual + faltam
   print('seu alistamento sera em {}.'.format(ano))
#---------------------------------------------------------------------------------------------
# CLASSICO DAS MÉDIAS
nota1 = float(input('Qual foi a primeira nota:'))
nota2 = float(input('Qual foi a segunda nota:'))
media = (nota1 + nota2) / 2
print('Sua média {:.2f}'.format(media))
if (media < 5):
    print('Media abaixo de 5.0: REPROVADO!')
elif(media >= 5 and media < 6.9):
    print('Média entre 5.0 e 6.9: EM RECUPERAÇÃO')
else:
    print('Media 7.0 ou superior: APROVADO')
#----------------------------------------------------------------------------------------------
#CLASSIFICANDO ATLETAS
nasc = int(input('Digite a data de nascimento:'))
idade = 2022 - nasc
print('Sua idade {} anos'.format(idade))
if(idade <= 9):
   print('Sua categoria é de até 9 anos: MIRIM')
elif (idade > 9 and idade <= 14):
   print('Sua categoria é de até 14 anos: INFANTIL')
elif(idade > 14 and idade <= 19):
   print('Sua categoria é de até 19 anos: JUNIOR')
elif(idade > 19 and idade <= 20):
   print('Sua categoria é de ate 20 anos: SENIOR')
else:
    print('Sua categoria esta acima de 21 anos: MASTER')
#----------------------------------------------------------------------------------------------
# ANALISANDO TRIANGULOS
print('-=-'*20)
print('ANALIZADOR DE TRIÂNGULOS:')
print('-=-'*20)
r1 = float(input('Primeiro Segmento:'))
r2 = float(input('Segundo Segmento:'))
r3 = float(input('Terceiro Segmento:'))
if r1 < r2 + r3 and r2 < r1 + r2 and r3 < r1 + r2:
    print('Os segmentos acima PODEM formar um TRIANGULO!')
    if(r1 == r2 == r3):
       print('EQUILATERO!')
    elif(r1 != r2 != r2 != r3 != r1):
       print('ESCALENO!')
    else:
       print('ISÓCELES')
else:
    print('Os segmentos acima NÃO PODEM formar um Triângulo!')
#-----------------------------------------------------------------------------------------------
# INDICE DE MASSA CORPORAL
peso = float(input('Qual seu peso:'))
altura = float(input('Qual sua altura:'))
imc = peso / (altura ** 2)
print('Seu IMC {}'.format(imc))
if (imc <= 18.5):
   print('Abaixo do peso!')
elif (imc > 18.5) and (imc <= 25):
   print('Peso Ideal!')
elif (imc > 25 and imc <= 30):
   print('Sobre Peso!')
elif(imc > 30 and imc <= 40):
   print('Obesidade!')
else:
   print('Obesiadade Morbida!')
#-----------------------------------------------------------------------------------------------
# GERENCIADOR DE PAGAMENTOS
preco = float(input('Preço das compras: R$'))
print('''FORMAS DE PAGAMENTOS
[1] à vista dinheiro/cheque
[2] à vista cartão
[3] 2x no cartão
[4] 3x ou mais no cartão
''')
opcao = int(input('Qual é a Opção:'))
if opcao == 1:
   desconto = preco * 10/100
   total = preco - desconto
   print('''Valor da compra R${:.2f} com desconto de R${:.2f} fica R${:.2f}
'''.format(preco, desconto, total))
elif opcao == 2:
   desconto = preco * 5/100
   total = desconto + preco
   print('''Valor da compra R${:.2f} com desconto de R${:.2f} fica R${:.2f}
'''.format(preco, desconto, total))
elif opcao == 3:
   parcela = preco / 2
   print('''Valor da compra R${:.2f} 2 parcelas de R${:.2f} SEM juros!
'''.format(preco, parcela))
elif (opcao == 4):
   juros = preco * 20/100
   total = juros+ preco
   print('''Valor da compra R${:.2f} com JUROS de R${:.2f} fica R${:.2f}
parcelas'''.format(preco, juros, total))
#--------------------------------------------------------------------------------------
# GAME: Pedra Papel Tesoura...
from random import randint
from time import sleep
item = ('pedra', 'papel', 'tesoura')
pc = randint(0,2)
print('''ESCOLHA UMA DAS OPÇÕES
[0] PEDRA
[1] PAPEL
[2] TESOURA
''')
jogador = int(input('Qual será sua jogada:'))
print('JO')
sleep(1)
print('KEN')
sleep(1.2)
print('PÔ')
print('=*='*10)
print('O computador escolheu {}'.format(item[pc]))
print('O jogador escolheu {}'.format(item[jogador]))
print('=*='*10)
if (pc == 0):
   if jogador == 0:
      print('EMPATE!')
   elif jogador == 1:
      print('A maquina Venceu!')
   elif jogador == 2:
      print('Você VENCEU!')
   else:
      print('Jogada Invalida!')
elif(pc == 1):
   if jogador == 0:
      print('Você VENCEU!')
   elif jogador == 1:
      print('EMPATE!')
   elif jogador == 2:
      print('A maquina Venceu!')
   else:
      print('Jogada Invalida!')
elif(pc == 2):
   if jogador == 0:
      print('A maquina Venceu!')
   elif jogador == 1:
      print('Você VENCEU!')
   elif jogador == 2:
      print('EMPATE!')
   else:
      print('Jogada Invalida!')