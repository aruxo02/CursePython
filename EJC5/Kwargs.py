def suma(**kwargs):
    total =0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total+= valor
    return total

print(suma(x=3,y=5,z=2))

def prueba(num1 , num2 ,*args ,**kwargs):
    print(f"el primer valor es {num1}")
    print(f"el segundo valor es {num2}")
    for arg in args:
        print(f"el arg tiene  valor es {arg}")
    for clave , valor in kwargs.items():
        print(f"{clave} = {valor}")

prueba(10,50,233,123,123,13123,13,x='1' ,y='2',z='2')


args = [100,222,33,444]
kwargs = {'x' :'uno' ,'y' :'dos' ,'z' :'tres'}
prueba(10,50 ,*args,**kwargs)


def cantidad_atributos(**kwarg):
    return  len(kwarg)

def  lista_atributos(**kwargs):
  return list(kwargs.values())


def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for nombre_argumento, valor_argumento in kwargs.items():
        print(f"{nombre_argumento}: {valor_argumento}")
