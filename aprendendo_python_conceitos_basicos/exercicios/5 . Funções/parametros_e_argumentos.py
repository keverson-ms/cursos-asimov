def adicionar_final(texto, final="!!!"):
    return texto + final

print(adicionar_final('olá'))

def dividir(a, b):
    if (a == 0 or b == 0):
        return 'não é possível realizar a divisão!'
    elif not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
       return 'não é possível realizar a divisão! (entrada inválida)'
    else:
        return a/b


print(dividir(float('2.3'),2))
