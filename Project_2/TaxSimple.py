#Sistema de comisiones sencilla

name = input("Dime tu nombre: ")
amount= input("Cuanto as vendido este mes :")
amount= float(amount)
print(f"Muy bien {name} la comision de este mes es: {round((amount *13 /100 ),2)}")