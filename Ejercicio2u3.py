import csv
class Helado (object):
    """docstring for Helado"""
    def _init_(self, gramos, precio):
        self.gramos = gramos
        self.precio = precio

class Sabor(object):
    """docstring for Sabor"""
    def _init_(self, idSabor, nombreSabor, ingredientes):
        self.idSabor = idSabor
        self.nombreSabor = nombreSabor
        self.ingredientes = ingredientes

class ManejaSabores(object):
    """docstring for ManejaSabores"""
    def _init_(self):
        self.sabores = []

    def cargar_sabores(self, archivo):
        with open(archivo, 'r') as file:
            for line in file:
                idSabor, nombreSabor, ingredientes = line.strip().split(',')
                sabor = Sabor(idSabor, nombreSabor, ingredientes)
                self.sabores.append(sabor)

class ManejaHelados (object):
    """docstring for ManejaHelados"""
    def _init_(self):
        self.helados = []

    def registrar_helado(self, helado):
        self.helados.append(helado)

    def obtener_sabores_mas_pedidos(self):
        sabores_pedidos = {}
        for helado in self.helados:
            for sabor in helado.sabores:
                if sabor in sabores_pedidos:
                    sabores_pedidos[sabor] += 1
                else:
                    sabores_pedidos[sabor] = 1
        
        sabores_mas_pedidos = sorted(sabores_pedidos, key=sabores_pedidos.get, reverse=True)[:5]
        return sabores_mas_pedidos

    def estimar_gramos_vendidos(self, numero_sabor):
        total_gramos = 0
        for helado in self.helados:
            for sabor in helado.sabores:
                if sabor.idSabor == numero_sabor:
                    total_gramos += helado.gramos / len(helado.sabores)
        
        return total_gramos

    def obtener_sabores_por_tipo_helado(self, tipo_helado):
        sabores_vendidos = set()
        for helado in self.helados:
            if helado.gramos == tipo_helado:
                for sabor in helado.sabores:
                    sabores_vendidos.add(sabor.nombreSabor)
        
        return sabores_vendidos

    def obtener_recaudacion_por_tipo_helado(self):
        recaudacion_por_tipo = {}
        for helado in self.helados:
            if helado.gramos in recaudacion_por_tipo:
                recaudacion_por_tipo[helado.gramos] += helado.precio
            else:
                recaudacion_por_tipo[helado.gramos] = helado.precio
        
        return recaudacion_por_tipo


if __name__ == '__main__':
 maneja_sabores = ManejaSabores()
 maneja_sabores.cargar_sabores("sabores.csv")
 maneja_helados = ManejaHelados()

 while True:
    print("\n----- Menú de opciones -----")
    print("1. Registrar un helado vendido")
    print("2. Mostrar los 5 sabores de helado más pedidos")
    print("3. Estimar la cantidad de gramos vendidos para un sabor")
    print("4. Mostrar los sabores vendidos para un tipo de helado")
    print("5. Mostrar recaudación por tipo de helado")
    print("0. Salir")

    opcion = int(input("Ingrese la opción deseada: "))

    if opcion == 1:
        gramos = int(input("Ingrese el peso en gramos del helado: "))
        precio = float(input("Ingrese el precio del helado: "))
        num_sabores = int(input("Ingrese el número de sabores: "))
        
        sabores = []
        for i in range(num_sabores):
            id_sabor = int(input(f"Ingrese el id del sabor {i+1}: "))
            sabor = maneja_sabores.sabores[id_sabor-1]
            sabores.append(sabor)
        
        helado = Helado(gramos, precio)
        helado.sabores = sabores
        
        maneja_helados.registrar_helado(helado)
        print("Helado registrado exitosamente.")

    elif opcion == 2:
        sabores_mas_pedidos = maneja_helados.obtener_sabores_mas_pedidos()
        print("Los 5 sabores de helado más pedidos son:")
        for sabor in sabores_mas_pedidos:
            print(sabor.nombreSabor)

    elif opcion == 3:
        numero_sabor = int(input("Ingrese el número de sabor: "))
        gramos_vendidos = maneja_helados.estimar_gramos_vendidos(numero_sabor)
        print(f"Se estima que se han vendido {gramos_vendidos} gramos de ese sabor.")

    elif opcion == 4:
        tipo_helado = int(input("Ingrese el tipo de helado (en gramos): "))
        sabores_vendidos = maneja_helados.obtener_sabores_por_tipo_helado(tipo_helado)
        print(f"Los sabores vendidos para un helado de {tipo_helado} gramos son:")
        for sabor in sabores_vendidos:
            print(sabor)

    elif opcion == 5:
        recaudacion_por_tipo = maneja_helados.obtener_recaudacion_por_tipo_helado()
        print("Recaudación por tipo de helado:")
        for tipo, recaudacion in recaudacion_por_tipo.items():
            print(f"{tipo} gramos: ${recaudacion}")

    elif opcion == 0:
        print("¡Hasta luego!")
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")