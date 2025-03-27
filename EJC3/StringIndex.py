#Metodos string index

text ="Mi texto es una prueba"
result = text[0]
print(result)

result = text[-2]
print(result)

result = text.index("n")
print(result)

#result = text.index("z")
#print(result)

result = text.index("e")
print(result)

result = text.index("texto")
print(result)

result = text.index("e",5)
print(result)

result = text.index("e",5,10)
print(result)

result = text.rindex("e")
print(result)