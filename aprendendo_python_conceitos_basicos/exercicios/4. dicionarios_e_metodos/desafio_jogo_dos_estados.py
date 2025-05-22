# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder o nome da capital
# de cada Estado do Brasil. O jogo deve perguntar ao usuário "Qual a capital do Extado X?",
# e checar se o usuário respondeu de forma correta. Após cada pergunta, o usuário pode
# escolher parar o jogo ou continuar para a próxima pergunta. Quando o usuário decidir parar
# ou quando todas as perguntas forem respondidas, o código mostra o número bruto e porcentagem de acertos.

estados_capitais = {
	'Acre': 'Rio Branco',
	'Alagoas': 'Maceió',
	'Amapá': 'Macapá',
	'Amazonas': 'Manaus',
    'Bahia': 'Salvador',
    'Ceará': 'Fortaleza',
    'Distrito Federal': 'Brasília',
    'Espírito Santo': 'Vitória',
    'Goiás': 'Goiânia',
    'Maranhão': 'São Luís',
    'Mato Grosso': 'Cuiabá',
    'Mato Grosso do Sul': 'Campo Grande',
    'Minas Gerais': 'Belo Horizonte',
    'Pará': 'Belém',
    'Paraíba': 'João Pessoa',
    'Paraná': 'Curitiba',
    'Pernambuco': 'Recife',
    'Piauí': 'Teresina',
    'Rio de Janeiro': 'Rio de Janeiro',
    'Rio Grande do Norte': 'Natal',
    'Rio Grande do Sul': 'Porto Alegre',
    'Rondônia': 'Porto Velho',
    'Roraima': 'Boa Vista',
    'Santa Catarina': 'Florianópolis',
    'São Paulo': 'São Paulo',
    'Sergipe': 'Aracaju',
    'Tocantins': 'Palmas'
}

itens = list(estados_capitais.items())
acertos = 0
i = 0

while i < len(itens):
    estado, capital = itens[i]
    i+=1

    resposta = input(f'Qual a capital do Estado {estado.upper()}: ')
    acertos = acertos + 1 if resposta.lower() == capital.lower() else acertos

    continuar = input(f'Deseja seguir para a próxima pergunta: [s] para sim [n] para não: ')

    continuar = True if continuar.lower() == 's' else False
    print(i == len(itens), i, len(itens))
    if continuar == False:
        print(f'Você acertou {acertos} pergunta de {i} respondidas de um total de {len(itens)} perguntas.')
        print(i / acertos)
        break
    elif(i == len(itens)) :
        print(f'Você respondeu todas as {len(itens)} perguntas: ')
        print(f'Acertos/Erros {acertos}/{len(itens) - acertos}')

#for estado, cidade in estados_capitais.items():
#    resposta = input(f'Qual a capital do estado {estado.upper()}?')
#    print(f'{resposta}')
#    if(resposta == cidade):
#        print(f'{estado} -> {cidade}')
#    elif (resposta != cidade):
#        print('Você errou!')
#        input(f'Deseja prosseguir com o Jogo?')

