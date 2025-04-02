#ramdom
from random import *

aleatorio = randint(1,50)
print(aleatorio)

aleatorio =  uniform(1,5)
print(aleatorio)
print(round(aleatorio,2))

aleatorio = random()
print(aleatorio)

colores =["Azul","Rojo","Verde"]
aleatorio = choice(colores)
print(aleatorio)

nums = list(range(5,100,5))
shuffle(nums)

print(nums)




