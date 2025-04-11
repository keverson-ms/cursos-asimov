# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - Se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

numero_secreto = 10

i = 1
tot = 3
while i <= tot:
    numero_informado = int(input('Chute um número: '))
    if(numero_informado == numero_secreto):
        print('você acertou, o número secreto é 10.')
        break
    elif tot - i == 0:
        print(f'suas tentativas acabaram, o número secreto era {str(numero_secreto)}')
        break
    else:
        dica = "menor" if numero_informado > numero_secreto  else "maior"
        print(f'você errou, uma dica, o número secreto é {dica} do que o número informado.')
        print(f'você possui {str(tot - i)} tentativa(s) ...')
    i += 1

