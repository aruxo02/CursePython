#loop for

list=["a","b","c"]

for l in list:
    num_l = list.index(l) + 1
    print(f"Letra {num_l} : {l}")

list2 = ["Pablo", "Fede", "luis" , "Julia"]
for name in list2:
    if name.startswith('l'):
        print(name)
    else:
        print(f"{name} no empieza por l")

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

#Loop while

monedas =5

while monedas > 0:
    print(f"Tengo {monedas} monedas")
    monedas -= 1
else:
    print("No tengo monedas")


response ="s"

while response =="s":
    response= input("Quieres seguir? (s/n)")
else:
    print("Gracias")

response= input("Tu nombre:")
while letra in response:
    if letra=="r":
        continue
        print(letra)








