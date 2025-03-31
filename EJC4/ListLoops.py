palabra = "Python"

lista = []

for letra in palabra:
    lista.append(letra)

print(lista)

lista = [letra for letra in "Python"]
print(lista)


lista = [n for n in range(0,21,2)]
print(lista)

lista = [n/2 for n in range(0,21,2)]
print(lista)

lista = [n if n * 2 > 10 else "no" for n in range(0,21,2)  ]
print(lista)

pies =[10,20,30,40]
metros = [n * 3.281 for n in pies]


