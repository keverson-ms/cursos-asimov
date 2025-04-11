# Desafio - crie um programa que:
# - Pede por um nome de usuário e uma senha.
# - Se ambos forem corretos, exibe uma mensagem de sucesso.
# - Caso contrário, exibe uma mensagem de erro. A mensagem é diferente
# - Quando o usuário está incorreto, e quando a senha está incorreta
# - O usuário/senha "corretos" podem ser definidos como 
# variáveis dentro próprio código

usuario_correto = 'keverson'
senha_correta   = '17081992'

usuario = input('Login: ')
senha   = input('Senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print(f'Bem vindo, {usuario_correto}!')
else:
    print('Usuário ou senha informados incorreto!');
    
    