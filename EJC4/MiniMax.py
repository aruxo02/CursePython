#Min y Max

menor = min(58,96,72,74)
print(menor)
maximo = max(58,96,72,74)
print(maximo)

lista = [58,96,72,74]
print(f"el menor es {min(lista)} y el mayor es {max(lista)}")

nombres=["juan","pablo","Alicia"]

print(min(nombres))

nombre ="Carlos"
print(min(nombre))

nombre ="carlos"
print(min(nombre))

nombre ="carLos"
print(min(nombre))

dic = {'C1' :45, 'C2': 11}
print(min(dic))

diccionario_edades ={"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima=min(diccionario_edades.values())
ultimo_nombre=max(diccionario_edades)
print(edad_minima)
print(ultimo_nombre)
