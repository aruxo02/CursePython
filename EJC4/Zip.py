#zip
nombres = ['Ana','Hugo','Valeria']
edades =[65,29,42]

combinados =list(zip(nombres,edades))
print(combinados)

ciudades=['Lima','Madrid']

combinados =list(zip(nombres,edades,ciudades))
print(combinados)

for nombre , edad ,ciudad in combinados:
    print(f"{nombre} tiene {edad} anos y vive en la ciudad {ciudad}" )


