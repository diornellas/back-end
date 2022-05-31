c = 1
while c < 10+1:
    print(c)
    c += 1
#---------------------------------------------------------------------------
r = 'S'
while r == 'S':
    n = int(input('Digite um numero:'))
    r = str(input('Quer continuar?[S/N]')).upper()
print('FIM')
#---------------------------------------------------------------------------
par = 0
impar = 0
r = 'S'
while r == 'S':
    n = int(input('Digite um numero:'))
    r = str(input('Quer continuar?[S/N]')).upper()
    if n % 2 == 0:
        par = par + 1
    else:
        impar += 1
print('Você digitou {} numeros PARES e {} numeros IMPARES'.format(par,impar))
print('FIM')