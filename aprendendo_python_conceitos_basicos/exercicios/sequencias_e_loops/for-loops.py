# FOR LOOP
# Desafio - crie um programa que:
# - Escolhe um número secreto.
# - Pede por um chute do usuário.
# - Indica se o usuário acertou ou não.
# - Se não acertou, dá uma dica, dizendo
#   - Se o número é mais alto ou mais baixo.
# - Repete isso até 3 vezes!

numero_secreto = 10
tot = 3
tentativas = tot
for n in range(tot):
    tentativas -= 1
    numero_informado = int(input('Chute um número: '))
    if(numero_informado == numero_secreto):
        print('você acertou, o número secreto é 10.')
    elif tentativas:
        dica = "menor" if numero_informado > numero_secreto  else "maior"
        print(f'você errou, uma dica, o número secreto é {dica} do que o número informado.')
        print(f'você possui {str(tentativas)} tentativa(s) ...')
    else:
        print(f'suas tentativas acabaram, o número secreto era {str(numero_secreto)}')


