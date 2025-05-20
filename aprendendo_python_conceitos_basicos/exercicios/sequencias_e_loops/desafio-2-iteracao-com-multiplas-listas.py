print('1) Dado duas listas, print todos os valores que aparecerem duplicados nas duas listas.\n')

lista1 = list(range(0, 26, 2))
lista2 = list(range(0, 26, 3))
duplicados = list()

for l1 in lista1:
   for l2 in lista2:
       if l1 == l2:
           duplicados.append(l1)
           print(f'O valor {l1} está presente nas duas listagens')

if len(duplicados):
    print(f'\nValores {duplicados} existentes nas 2 listas.\n')
else:
    print('\nNão há valores duplicados nas 2 listas.\n')

print('-'*len(duplicados)+' Fim do exercício 1 '+'-'*len(duplicados))

print('\n2) Dado duas listas, print uma mensagem dizendo se existe algum elemento em comum entre elas ou não.\n')

elemento_comum = False

for l1 in lista1:
   for l2 in lista2:
       if l1 == l2:
           elemento_comum = True

if elemento_comum :
    print(f'As listas {lista1} e {lista2} possuem elementos em comum, que são: {duplicados}')
else:
        print(f'As listas {lista1} e {lista2} NÃO possuem elementos em comum')

print('-'*len(lista1)+' Fim do exercício 2 '+'-'*len(lista1))


