print('1) Dado uma sequência de números, calcule a soma e média dos números.\nATENÇÃO: não vale usar a função SUM()! \n')
lista = [19, 10, -10, 13, 20, 15]
soma = 0
for l in lista:
    soma +=l
print(f'A soma dos valores {lista} é igual a: {soma}')
print(f'A média da soma da lista é: {soma / len(lista)}\n')
print('-'*int(soma/4)+' Fim do primeiro exercício '+ '-'*int(soma/4))

print('\n2) Dado uma sequência de números, calcule o maior valor da sequência.\nATENÇÃO: NÃO vale usar a função MAX()\n')
maior = lista[0]
for l in lista:
    if l > maior:
        maior = l

print(f'O maior valor dentro da listagem {lista} é : {maior}\n')
print('-'*int(soma/4)+' Fim do segundo exercício '+ '-'*int(soma/4))

print('3) Dado uma lista de palavras, print todas as palavras com pelo menos 5 caracteres. \n')

frutas = ['Manga', 'Mamão', 'Uva', 'Pera', 'Maça', 'Melância', 'Morango', 'Tomate', 'Banana']

for fruta in frutas:
    if int(len(fruta)) >= 5:
        print(f'A fruta que possui 5 ou + caracteres é : {fruta}')
