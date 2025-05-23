# Crie um "jogo dos estados". Neste jogo, o jogador precisa responder o nome da capital
# de cada Estado do Brasil. O jogo deve perguntar ao usuário "Qual a capital do Estado X?",
# e checar se o usuário respondeu de forma correta. Após cada pergunta, o usuário pode
# escolher parar o jogo ou continuar para a próxima pergunta. Quando o usuário decidir parar
# ou quando todas as perguntas forem respondidas, o código mostra o número bruto e porcentagem de acertos.

estados_capitais = {
	'Acre'                  : 'Rio Branco',
	'Alagoas'               : 'Maceió',
	'Amapá'                 : 'Macapá',
	'Amazonas'              : 'Manaus',
    'Bahia'                 : 'Salvador',
    'Ceará'                 : 'Fortaleza',
    'Distrito Federal'      : 'Brasília',
    'Espírito Santo'        : 'Vitória',
    'Goiás'                 : 'Goiânia',
    'Maranhão'              : 'São Luís',
    'Mato Grosso'           : 'Cuiabá',
    'Mato Grosso do Sul'    : 'Campo Grande',
    'Minas Gerais'          : 'Belo Horizonte',
    'Pará'                  : 'Belém',
    'Paraíba'               : 'João Pessoa',
    'Paraná'                : 'Curitiba',
    'Pernambuco'            : 'Recife',
    'Piauí'                 : 'Teresina',
    'Rio de Janeiro'        : 'Rio de Janeiro',
    'Rio Grande do Norte'   : 'Natal',
    'Rio Grande do Sul'     : 'Porto Alegre',
    'Rondônia'              : 'Porto Velho',
    'Roraima'               : 'Boa Vista',
    'Santa Catarina'        : 'Florianópolis',
    'São Paulo'             : 'São Paulo',
    'Sergipe'               : 'Aracaju',
    'Tocantins'             : 'Palmas'
}

itens = list(estados_capitais.items())
acertos = 0
i = 0
calc = 0
tot = 0
opcao = 'n'
resposta = ''

while i <= len(itens):
    estado, capital = itens[i]

    if opcao in ['s', 'n']:
        i += 1
        resposta = input(f'Qual a capital do Estado {estado.upper()}: ').lower()
        print(f'Você acertou: {capital}' if resposta == capital.lower() else f'você errou a opção correta seria: {capital}')

    if resposta == capital.lower():
        acertos +=1

    opcao = input(f'Deseja continuar: [s] sim [n] não: ').lower()

    if opcao not in ['s', 'n']:
        print(f'Opção {opcao} inválida.')
        opcao

    calc = round(acertos / i * 100, 2)
    tot = round(acertos / len(itens) * 100, 2)

    if opcao == 'n' or len(itens) == i:
        print(f'Você respondeu {i} pergunta(s): ')
        print(f'Sua taxa de acerto das perguntas respondidas é: {calc}% de {i} respondidas.')
        print(f'Sua taxa de acerto em relação ao total de perguntas é {len(itens)}/{acertos}, margem de acerto des: {tot}%')
        break

