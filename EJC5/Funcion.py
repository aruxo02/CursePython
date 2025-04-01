#funcion

def saludar_persona(nombre):
    '''Esta funcion sirve para saludar'''
    print(f"Hola {nombre}")

saludar_persona("Fer")
#-------------------------------------------
def multiplicar (num1, num2):
    ''' multiplica'''
    return num1*num2

resultado = multiplicar(1,3)
print(resultado)

#-------------------------------------------
def chequear(num):
    return num in range(100,1000)

res =chequear(658)
print(res)
#-------------------------------------------
def chequear2(list):
    for n in list:
        if n in range(100,1000):
            return True
        else:
            pass

res =chequear2([55,99,600])
print(res)
#-------------------------------------------
def cafe_mas_caro(precios):
    precio_mayor=0
    cafemas_caro=""
    for cafe,precio  in precios:
        if precio >precio_mayor:
            precio_mayor =precio
            cafemas_caro=cafe
    return (cafemas_caro,precio_mayor)

precios_cafe=[("capuchino",1.5),("Expreso",1.2)]

print(cafe_mas_caro(precios_cafe))
o_cafe,o_precio = cafe_mas_caro(precios_cafe)
print(o_cafe)
print(o_precio)
#-------------------------------------------




