#iteration_functions
from random import *

#create list
palitos =["-","--","---","----"]

#mix list
def mix(list):
    shuffle(list)
    return list

# select line
def select_line():
    intento=''
    while intento not in ['1','2','3','4']:
        intento= input("elige un numero del 1 al 4: ")

    return int(intento)

# check attempt
def chek(lis,attempt):
    if lis[attempt -1] == '-':
        print("A lavar los platos ")
    else:
        print("Esta vez te has salvado")

    print(f"te a tocado {lis[attempt -1]}")


palitos_mezclar = mix(palitos)
selecion= select_line()
chek(palitos_mezclar,selecion)

#-------------------------------------------

def lanzar_dados():
    num1 = randint(1, 6)
    num2 = randint(1, 6)
    return num1, num2


def evaluar_jugada(num1, num2):
    suma_dados = num1 + num2
    if suma_dados <= 6:
        return (f"La suma de tus dados es {suma_dados}. Lamentable")
    elif suma_dados > 6 and suma_dados < 10:
        return (f"La suma de tus dados es {suma_dados}. Tienes buenas chances")
    elif suma_dados >= 10:
        return (f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora")

#-------------------------------------------
lista_numeros = [1, 2, 15, 7, 2]

def reducir_lista(lista):
    lista = list(set(lista))
    mas_alto = max(lista)
    lista.remove(mas_alto)
    return lista

def promedio(lista):
    return sum(lista) / len(lista)





