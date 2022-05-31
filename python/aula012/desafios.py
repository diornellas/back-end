# NUMEROS COM FLAG
c = 1
tot = s = 0
while True:
   num = int(input('Digite um numero:[999 parar programa!]'))
   if num == 999:
      break
   tot += c
   s += num
print(f'Total de Numeros digitados {tot} a soma deles é {s}')
#-----------------------------------------------------------------------
# TABUADA V3.0
num = t = c = cont = 0
while True:
   cont += 1
   print('-='*40)
   num = int(input('Quer ver a tabuada de qual valor? (Negativos encerra programa)'))
   print('-='*40)
   if num < 0:
      break
   for c in range(1,10):
      c += 1
      t = num * c
      print(f'{num} x {c} = {t}')
print('PROGRAMA TABUADA ENCERRADO.', end='')
print('Volte sempre!!!')
#---------------------------------------------------------------------
# JOGO DO PAR OU IMPAR
from random import randint
num = soma = v = 0
opcao = r = escolheu = ''
print('=-'*25)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*25)
print('--'*25)
while True:
   pc = randint(0,10)
   num = int(input('Diga o valor: '))
   opcao = str(input('Par ou Impar? [PAR/IMPAR] ')).upper()
   soma = pc + num
   if soma % 2 == 0:
      r = 'PAR'
   elif soma % 2 == 1:
         r = 'IMPAR'
   if num and pc % 2 == 0:
      escolheu = 'PAR'
   elif num and pc % 2 == 1:
         escolheu = 'IMPAR'
   if opcao == r:
      print('--'*25)
      v += 1
      print(f'Você jogou {num} e o computador {pc}. Total {soma} DEU {r}')
      print('--'*25)
      print('Você VENCEU!')
      print('Vamos Jogar Novamente...')
      print('~~'*25)
   elif escolheu != r:
      print('--'*25)
      print(f'Você jogou {num} e o computador {pc}. Total {soma} DEU {r}')
      print('--'*25)
      print('Você PERDEU!')
      print('~~'*25)
      break
print(f'GAME OVER! Você venceu {v} vezes.')
#-----------------------------------------------------------------------------------
# ANALISE DE DADOS DO GRUPO
idade = tot = masc = novinha = 0
sexo = resp = ''
while True:
   print('--'*25)
   print('CADASTRO UMA PESSOA')
   print('--'*25)
   idade = int(input('Idade: '))
   sexo = str(input('Sexo: ')).upper()
   print('--'*25)
   resp = str(input('Quer continuar?[S/N] ')).upper()
   if idade > 18:
      tot += 1
   if sexo == 'M':
      masc += 1
   elif sexo == 'F' and idade < 20:
      novinha += 1
   if resp == 'N':
      break
print('========FIM DO PROGRAMA========')
print(f'Total de pessoas com mais de 18 anos {tot}!')
print(f'Ao todo temos {masc} homens cadastrados!')
print(f'E temos {novinha} mulheres com menos de 20 anos!')
#-------------------------------------------------------------------------------------
# ESTATÍSTICAS EM PRODUTOS
total = acao = maisMil = 0
while True:
   print('=~'*25)
   produto = str(input('Nome do produto: '))
   preco = float(input('Qual o preço do produto: R$'))
   print('~='*25)
   acao = str(input('Quer continuar?[S/N] ')).upper()
   total += preco
   if preco > 1000:
      maisMil += 1
   if acao == 'N':
      break
print('~~~~~~~~~~FIM~~~~~~~~~~')
print(f'Total da compra: R${total:.2f}')
print(f'Total {maisMil} produtos mais que R$1000,00')
#-------------------------------------------------------------------------------------
#  SIMULADOR DE CAIXA ELETRONICO