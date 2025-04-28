
def suma(a,b):
    return a+b

print(suma(1,2))

def suma_arg(*args):
    total =0
    for arg in args:
        total +=arg
    return total

print(suma_arg(5,4,53,53,5))

def suma_arg_Sum(*args):
    return sum(args)

print(suma_arg_Sum(5,4,53,53,5))


def suma_cuadrados(*args):
    return sum(x ** 2 for x in args)
print(suma_cuadrados(1, 2, 3))

#sumo de numeros negartivo y positivo
def suma_absolutos(*args):
    return sum(abs(x) for x in args )

def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"