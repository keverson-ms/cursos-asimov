#Crie um código que conta o número de vogais de um bloco de texto qualquer.
#O código deve desconsiderar letras maiúsculas/minúsculas, isto é, "a" e "A" contam
#da mesma forma.
#O texto pode ser colado diretamente como un string no código
texto = """
Ao contrário do que se acredita, Lorem Ipsum não é simplesmente um texto randômico.
Com mais de 2000 anos, suas raízes podem ser encontradas em uma obra de literatura latina clássica datada de 45 AC.
Richard McClintock, um professor de latim do Hampden-Sydney College na Virginia, pesquisou uma das mais obscuras palavras em latim, consectetur, oriunda de uma passagem de Lorem Ipsum, e, procurando por entre citações da palavra na literatura clássica, descobriu a sua indubitável origem.
"""

for vogal in ('a', 'e', 'i', 'o', 'u'):
    print(f'Vogal {vogal.upper()} tem {texto.lower().count(vogal)} ocorrências.')
