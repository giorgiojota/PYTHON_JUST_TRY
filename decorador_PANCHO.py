
def armar_pancho(func):
    def envoltura():
        print("pan arriba")
        func()
        print("pan abajo")
    return envoltura # Retorna la función 'envoltura'

@armar_pancho
def salchicha():
    print("salchicha")
    # Llamamos a la función decorada
salchicha()

@armar_pancho
def fiambre():
    print("jamon y queso")
    # Llamamos a la función decorada
fiambre()

#Ejemplo de decorador con parámetros 