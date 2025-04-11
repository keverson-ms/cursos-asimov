usuarios = [
    ('Keverson', 'keverson.souza@sfiemt.ind.br', 'xxx.xxx.xxx-xx'),
    ('Pitter', 'pitter.maciel@sfiemt.ind.br', 'yyy.yyy.yyy-yy'),
    ('Marcos', 'marcos.ralmeida@sfiemt.ind.br', 'zzz.zzz.zzz-zz')
]

for nome, email, cpf in usuarios :
    print(f'nome: {nome}');
    print(f'email: {email}');
    print(f'cpf: {cpf}\n');

print('-'*25+'\n')

for usuario in usuarios :
    nome, email, cpf = usuario
    print(f'nome: {nome}');
    print(f'email: {email}');
    print(f'cpf: {cpf}\n');
