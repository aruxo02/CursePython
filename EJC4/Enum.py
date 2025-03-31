#Enum
lis=['a','b','c']

for item in enumerate(lis):
    print(lis)

for indice ,item in enumerate(lis):
    print(indice, item)

for indice ,item in enumerate(range(40,50)):
    print(indice, item)

mis_tuples = list(enumerate(lis))
print(mis_tuples[1][0])

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')