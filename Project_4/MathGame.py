#Game

from random import randint

name = input("Cual es tu nombre: ")

print(f"Genial {name}, necesito que me digas un numero del 1 al 100 y tienes que adivinarlo antes de 8 intentos")

ran = randint(0,100)

for n in range(1,9):
    while True:
        numero = int (input(f"intento numero {n} , dime el numero: "))
        if numero  in range(1,101):
            break
        else:
            print("Numero fuera de rango")
            
    if numero == ran:
        print(f"Correcto el numero era {numero} te ha llevado {n} intentos")
        break
    elif  numero > ran:
        print(f"numero incorrecto {numero} es mayor al numero a adivinar")
    elif numero < ran:
        print(f"numero incorrecto {numero} es menor al numero a adivinar")

