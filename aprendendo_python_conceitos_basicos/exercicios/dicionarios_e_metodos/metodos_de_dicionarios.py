produtos = {
    'banana': 3.60,
    'leite': 4.90,
    'carne': 15.50,
    'pão'  : 9.00
}

novos_produtos = {
    'carro': 5000.00,
    'pão' : 5.89
}

#print(produtos.get('banana', 'Não encontrado!'))
#print(produtos.setdefault('leit', 0))

#for produto in produtos.keys():
#    print(produto)

#for produto in produtos.values():
#    print(produto)

#for par in produtos.items():
#    print(par)

#for k, v in produtos.items():
#    print(f'chave: {k} -> valor: {v}')

#produtos.update(novos_produtos)
#print(produtos)

produtos_copia = produtos.copy()

produtos_copia['morango'] = 25.00
print(produtos)
print(produtos_copia)
