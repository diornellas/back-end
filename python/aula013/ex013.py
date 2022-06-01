# TUPLAS são Variáveis Composta em que o vetor fica entre () -> PARENTESE
# LISTAS são Variaveis compostas em que o vetor fica entr [] -> COLCHETES
# DICIONÁRIOS são  Variaveis Compostas em que o vetor fica entre {} -> CHAVES
#------------------------------------------------------------------------------------
#   TUPLAS
lanche = ('Hamburguer', 'Suco', 'Pudim', 'Café')
print(lanche[:1])
#
lanche = ('Hamburguer', 'Suco', 'Pudim', 'Café')
for comida in lanche:
   print(f'Vou comer {comida}')
print('Estou satisfeito!')
#
lanche = ('Hamburguer', 'Suco', 'Pudim', 'Café')
for c in range(0,len(lanche)):
   print(f'Vou comer {lanche[c]}')
print('Estou satisfeito!')
# COLOCANDO A LISTA EM ORDEM ALFABETICA
lanche = ('Hamburguer', 'Suco', 'Pudim', 'Café')
print(lanche)
print(sorted(lanche))
#
