#Match

'''serie="S1"

if serie == "S1":
    print("s1")
elif serie =="S2":
    print("s2")
elif serie == "S3":
    print("s3")
else:
    print("no existe")'''


s="S1"

match s:
    case "S1":
        print("s1")
    case "S2":
        print("s2")
    case "S3":
        print("s3")
    case _:
        print("no existe")

cliente = {"nombre": "Carlos" ,"edad":45 ,"ocupacion": "tutor"}
pelicula = {"titulo": "matrix" ,"fichatecnica":{"protagonista":"Keanu reeces" , "director":"Lalanana"}}

elementos =[cliente,pelicula,"libros"]

for e in elementos:
    match e:
        case {"nombre": nombre,"edad" : edad,"ocupacion":ocupacion}:
            print(nombre,edad,ocupacion)


