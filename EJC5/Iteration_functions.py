#iteration_functions
from random import shuffle

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




