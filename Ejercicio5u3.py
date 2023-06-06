class Coleccion (object):
    """docstring for Coleccion"""
    def insertarElemento(self, elemento, posicion):
        pass

    def agregarElemento(self, elemento):
        pass

    def mostrarElemento(self, posicion):
        pass

class MiColeccion(Coleccion):
    """docstring for MiColeccion"""
    def __init__(self):
        self.elementos = []

    def insertarElemento(self, elemento, posicion):
        if posicion < 0 or posicion > len(self.elementos):
            raise Exception("Posición inválida")
        self.elementos.insert(posicion, elemento)

    def agregarElemento(self, elemento):
        self.elementos.append(elemento)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= len(self.elementos):
            raise Exception("Posición inválida")
        print(self.elementos[posicion])

if __name__ == '__main__':
 coleccion = MiColeccion()
 coleccion.agregarElemento("Elemento 1")
 coleccion.agregarElemento("Elemento 2")
 coleccion.insertarElemento("Elemento 3", 1)

try:
    coleccion.mostrarElemento(0) 
    coleccion.mostrarElemento(2)  
    coleccion.mostrarElemento(3)  
except Exception as e:
    print("Error:", e)
