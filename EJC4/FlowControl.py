# if else

if 10==9:
    print("Correcto")
else:
    print("Incorrecto")

pet = "Perro"
if pet== "Gato":
    print("Tienes un Gato")
elif pet=="Perro":
    print("Tienes un perro")
else:
    print("No se que mascotas tienes")

age= 16
calif= 9
if age<18:
    print("eres menor de edad ")
    if calif>7 :
        print("Aprobado")
    else:
        print("Suspendido")
else:
    print("No deberias estar aqui ")

    habla_ingles = True
    sabe_python = False

    if habla_ingles and sabe_python:
        print("Cumples con los requisitos para postularte")
    elif not habla_ingles and not sabe_python:
        print("Para postularte, necesitas saber programar en Python y tener conocimientos de inglés")
    elif not habla_ingles and sabe_python:
        print("Para postularte, necesitas tener conocimientos de inglés")
    elif habla_ingles and not sabe_python:
        print("Para postularte, necesitas saber programar en Python")


