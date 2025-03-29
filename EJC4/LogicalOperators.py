#logical operators

my_bool =10==10
print(my_bool)

my_bool =5+5==10
print(my_bool)

my_bool ="blanco" == "blanco"
print(my_bool)

my_bool =10.0==10
print(my_bool)

my_bool =10!=10
print(my_bool)

my_bool =10>=10
print(my_bool)

my_bool =4<5<6
print(my_bool)

my_bool =4<5 and 5 >6
print(my_bool)

my_bool =20==10+10 and "Perro" =="Perro"
print(my_bool)

my_bool =20==10+10 or "Gato" =="Perro"
print(my_bool)

my_bool =20==11+10 or "Gato" =="Perro"
print(my_bool)

text ="esta frase es breve"
my_bool =('frase' in text ) and ('breve' in text )

text ="esta frase es breve"
my_bool =('frase' in text ) or ('Python' in text )

mi_bool = not ('a' != 'a')
print(mi_bool)


