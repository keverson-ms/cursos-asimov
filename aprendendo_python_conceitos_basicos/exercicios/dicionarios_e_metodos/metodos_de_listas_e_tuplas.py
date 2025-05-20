tup = (0, 0, 0, 1, 2, 3, 4)

print(tup.index(3))

print(tup.count(3))

l1 = [0, 0, 0, 1, 2, 3, 4]
l2 = l1.copy()

l1.clear()

for n in range(5):
    print(l2.append(n * 3))

vogais = ['a', 'i', 'o', 'u']
vogais.insert(1, 'e')
vogais.insert(5, 'k')
vogais.pop()

valores = [12, 56, 1, 0, 456, 46]
print(valores.sort())

valores.extend([5, 10 ,20])
