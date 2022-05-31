# NUMEROS COM FLAG
tot = s = 0
while True:
   num = int(input('Digite um numero:[999 parar programa!]'))
   if num == 999:
      break
   tot += 1
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
print('=-'*25)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-'*25)
print('--'*25)
while True:
   num = int(input('Diga o valor: '))
   pc = randint(0,10)
   soma = pc + num
   opcao = ' '
   while opcao not in 'PI':
      opcao = str(input('Par ou Impar? [PAR/IMPAR] ')).strip().upper()[0]
   print(f'Você jogou {num} e o computador {pc}. Total {soma}', end=' ')
   print('Deu PAR' if soma % 2 == 0 else 'Deu IMPAR')
   if opcao == 'P':
      if soma % 2 ==0:
         print('Você venceu!')
         v += 1
      else:
         print('Você perdeu!')
         break
   elif opcao == 'I':
      if soma % 2 ==1:
         print('Você venceu!')
         v += 1
      else:
         print('Você Perdeu!')
         break
   print('Vamos Jogar Novamente...')
print(f'GAME OVER! Você venceu {v} vezes.')
#-----------------------------------------------------------------------------------
# ANALISE DE DADOS DO GRUPO
idade = tot = masc = novinha = 0
while True:
   print('--'*25)
   print('CADASTRO UMA PESSOA')
   print('--'*25)
   sexo = resp = ' '
   idade = int(input('Idade: '))
   while sexo not in 'MF':
      sexo = str(input('Sexo:[M/F]')).strip().upper()
   print('--'*25)
   while resp not in 'SN':
      resp = str(input('Quer continuar?[S/N] ')).strip().upper()
   if idade >= 18:
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
barato = ''
total = preco = maisMil = menor = c = 0
while True:
   print('=~'*25)
   produto = str(input('Nome do produto: '))
   preco = float(input('Qual o preço do produto: R$'))
   c += 1
   print('~='*25)
   acao = str(input('Quer continuar?[S/N] ')).upper()
   total += preco
   if preco > 1000:
      maisMil += 1
   if c == 1:
      menor = preco
      barato = produto
   else:
      if preco < menor:
         menor = preco
         barato = produto
   if acao == 'N':
      break
print('~~~~~~~~~~FIM~~~~~~~~~~')
print(f'Total da compra: R${total:.2f}')
print(f'Total {maisMil} produtos que custa mais que R$1000,00')
print(f'O produto mais barato foi {barato} custa R${menor:.2f}')
#-------------------------------------------------------------------------------------
#  SIMULADOR DE CAIXA ELETRONICO
banco = 'BANCO MD'
print('='*20)
print('BANCO MD')
print('='*20)
valor = int(input('Que Valor Quer Sacar? R$'))
total = valor
cedula = 50
totced = 0
while True:
   if total >= cedula:
      total -= cedula
      totced += 1
   else:
      if totced > 0:
         print(f'Total {totced} cédulas de R${cedula}')
      if cedula == 50:
         cedula = 20
         totced = 0
      elif cedula == 20:
         cedula = 10
         totced = 0
      elif cedula == 10:
         cedula = 1
         totced = 0
      if total == 0:
         break
print(f'Volte Sempre ao {banco}')