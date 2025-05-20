capitais = {
    'Brasil' :'Brasília',
    'França': 'Paris',
    'Japão' : 'Tóquio'
}

pais = 'Brasil'

if pais in capitais:
    print(f'A capital de {pais} é {capitais[pais]}');
else:
    print(f'Não há capital registrada para o país {pais}')
