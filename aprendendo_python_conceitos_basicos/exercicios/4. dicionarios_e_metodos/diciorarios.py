capitais = {
    'Brasil' :'Brasília',
    'França': 'Paris',
    'Japão' : 'Tóquio'
}

frutas = dict();
frutas[1] = 'Banana'
frutas[2] = 'Maça'
frutas[3] = 'Laranja'
frutas[4] = 'Uva'

print(frutas)
print(capitais)

for k in frutas:
    rst = frutas[k]
    print(f'Chave: {k} | Valor: {frutas[k]}')
