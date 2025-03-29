#loop for
from setuptools.monkey import patch_all

list=["a","b","c"]

for l in list:
    num_l = list.index(l) + 1
    print(f"Letra {num_l} : {l}")

list2 = ["Pablo", "Fede", "luis" , "Julia"]
for name in list2:
    if name.startswith('l'):
        print(name)
    else:
        print(f"{name} no empieza por L")

list_num=[1,2,3,4,5]
value =0
for num in list_num:
    value = value +num
print(value)


palabra ="python s genial "
for letra in palabra:
    print(letra)

for a,b in [[1,2],[3,4],[5,6]]:
    print(a)
    print(b)

dic ={'clave1':'a' ,'clave2':'b'}
for clave in dic:
    print(clave)

for clave in dic.items():
     print(clave)






