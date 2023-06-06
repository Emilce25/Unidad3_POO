import json

class Vehiculo (object):
    """docstring for Vehiculo"""
    def _init_(self, modelo, cantidad_puertas, color, precio_base):
        self.modelo = modelo
        self.cantidad_puertas = cantidad_puertas
        self.color = color
        self.precio_base = precio_base

    def calcular_precio_venta(self):
        pass

class VehiculoNuevo(Vehiculo):
    """docstring for VehiculoNuevo"""
    def _init_(self, modelo, cantidad_puertas, color, precio_base, version):
        super()._init_(modelo, cantidad_puertas, color, precio_base)
        self.version = version

    def calcular_precio_venta(self):
        porcentaje_patentamiento = 0.10
        porcentaje_version = 0.02

        precio_venta = self.precio_base + (self.precio_base * porcentaje_patentamiento)
        if self.version == "full":
            precio_venta += self.precio_base * porcentaje_version

        return precio_venta

class VehiculoUsado(Vehiculo):
    """docstring for VehiculoUsado"""
    def _init_(self, modelo, cantidad_puertas, color, precio_base, marca, patente, anio, kilometraje):
        super()._init_(modelo, cantidad_puertas, color, precio_base)
        self.marca = marca
        self.patente = patente
        self.anio = anio
        self.kilometraje = kilometraje

    def calcular_precio_venta(self):
        porcentaje_antiguedad = 0.01
        porcentaje_kilometraje = 0.02
        anio_actual = 2023

        antiguedad = anio_actual - self.anio
        porcentaje_descuento = antiguedad * porcentaje_antiguedad

        if self.kilometraje > 100000:
            porcentaje_descuento += porcentaje_kilometraje

        precio_venta = self.precio_base - (self.precio_base * porcentaje_descuento)
        return precio_venta

class ListaVehiculos(object):
    """docstring for ListaVehiculos"""
    def _init_(self):
        self.vehiculos = []

    def _iter_(self):
        return iter(self.vehiculos)

    def insertar_vehiculo(self, vehiculo, posicion):
        self.vehiculos.insert(posicion, vehiculo)

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def obtener_tipo_vehiculo(self, posicion):
        vehiculo = self.vehiculos[posicion]
        if isinstance(vehiculo, VehiculoNuevo):
            return "Vehículo Nuevo"
        elif isinstance(vehiculo, VehiculoUsado):
            return "Vehículo Usado"
        else:
            return "Tipo de vehículo desconocido"

    def modificar_precio_venta(self, patente, nuevo_precio_base):
        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, VehiculoUsado) and vehiculo.patente == patente:
                vehiculo.precio_base = nuevo_precio_base
                print(f"El nuevo precio base del vehículo con patente {patente} es: {vehiculo.precio_base}")
                print(f"El precio de venta del vehículo es: {vehiculo.calcular_precio_venta()}")

    def obtener_vehiculo_mas_economico(self):
        if not self.vehiculos:
            return None

        vehiculo_mas_economico = self.vehiculos[0]
        for vehiculo in self.vehiculos:
            if vehiculo.calcular_precio_venta() < vehiculo_mas_economico.calcular_precio_venta():
                vehiculo_mas_economico = vehiculo

        return vehiculo_mas_economico

    def mostrar_vehiculos(self):
        for vehiculo in self.vehiculos:
            print(f"Modelo: {vehiculo.modelo}, Puertas: {vehiculo.cantidad_puertas}, Precio de venta: {vehiculo.calcular_precio_venta()}")


def leer_archivo_vehiculos():
    with open("vehiculos.json", "r") as file:
        data = json.load(file)

    lista_vehiculos = ListaVehiculos()

    for vehiculo_data in data:
        modelo = vehiculo_data["modelo"]
        cantidad_puertas = vehiculo_data["cantidad_puertas"]
        color = vehiculo_data["color"]
        precio_base = vehiculo_data["precio_base"]

        if "version" in vehiculo_data:
            version = vehiculo_data["version"]
            vehiculo = VehiculoNuevo(modelo, cantidad_puertas, color, precio_base, version)
        else:
            marca = vehiculo_data["marca"]
            patente = vehiculo_data["patente"]
            anio = vehiculo_data["anio"]
            kilometraje = vehiculo_data["kilometraje"]
            vehiculo = VehiculoUsado(modelo, cantidad_puertas, color, precio_base, marca, patente, anio, kilometraje)

        lista_vehiculos.agregar_vehiculo(vehiculo)

    return lista_vehiculos

def mostrar_menu():
    print("Menu de opciones:")
    print("1) Insertar un vehículo en la colección en una posición determinada.")
    print("2) Agregar un vehículo a la colección.")
    print("3) Dada una posición de la Lista, mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.")
    print("4) Dada la patente de un vehículo usado, modificar el precio base, y luego mostrar el precio de venta.")
    print("5) Mostrar todos los datos, incluido el importe de venta, del vehículo más económico.")
    print("6) Mostrar para todos los vehículos que la concesionaria tiene a la venta, modelo, cantidad de puertas e importe de venta.")
    print("7) Almacenar los objetos de la colección Lista en el archivo 'vehiculos.json'.")
    print("0) Salir")

def ejecutar_opcion(opcion, lista_vehiculos):
    if opcion == 1:
        modelo = input("Ingrese el modelo del vehículo: ")
        cantidad_puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
        color = input("Ingrese el color del vehículo: ")
        precio_base = float(input("Ingrese el precio base del vehículo: "))
        version = input("Ingrese la versión del vehículo (base o full): ")
        vehiculo = VehiculoNuevo(modelo, cantidad_puertas, color, precio_base, version)
        posicion = int(input("Ingrese la posición en la que desea insertar el vehículo: "))
        lista_vehiculos.insertar_vehiculo(vehiculo, posicion)
        print("Vehículo insertado correctamente.")

    elif opcion == 2:
        modelo = input("Ingrese el modelo del vehículo: ")
        cantidad_puertas = int(input("Ingrese la cantidad de puertas del vehículo: "))
        color = input("Ingrese el color del vehículo: ")
        precio_base = float(input("Ingrese el precio base del vehículo: "))
        marca = input("Ingrese la marca del vehículo usado: ")
        patente = input("Ingrese la patente del vehículo usado: ")
        anio = int(input("Ingrese el año del vehículo usado: "))
        kilometraje = float(input("Ingrese el kilometraje del vehículo usado: "))
        vehiculo = VehiculoUsado(modelo, cantidad_puertas, color, precio_base, marca, patente, anio, kilometraje)
        lista_vehiculos.agregar_vehiculo(vehiculo)
        print("Vehículo agregado correctamente.")

    elif opcion == 3:
        posicion = int(input("Ingrese la posición de la lista: "))
        tipo_vehiculo = lista_vehiculos.obtener_tipo_vehiculo(posicion)
        print(f"En la posición {posicion} se encuentra un {tipo_vehiculo}.")

    elif opcion == 4:
        patente = input("Ingrese la patente del vehículo usado: ")
        nuevo_precio_base = float(input("Ingrese el nuevo precio base: "))
        lista_vehiculos.modificar_precio_venta(patente, nuevo_precio_base)

    elif opcion == 5:
        vehiculo_mas_economico = lista_vehiculos.obtener_vehiculo_mas_economico()
        if vehiculo_mas_economico:
            print("Vehículo más económico:")
            print(f"Modelo: {vehiculo_mas_economico.modelo}")
            print(f"Cantidad de puertas: {vehiculo_mas_economico.cantidad_puertas}")
            print(f"Precio de venta: {vehiculo_mas_economico.calcular_precio_venta()}")
        else:
            print("No se encontraron vehículos en la lista.")

    elif opcion == 6:
        lista_vehiculos.mostrar_vehiculos()

    elif opcion == 7:
        guardar_vehiculos(lista_vehiculos)
        print("Vehículos almacenados correctamente.")

    elif opcion == 0:
        return False

    else:
        print("Opción inválida. Intente nuevamente.")

    return True

def guardar_vehiculos(lista_vehiculos):
    vehiculos = []

    for vehiculo in lista_vehiculos:
        if isinstance(vehiculo, VehiculoNuevo):
            vehiculo_data = {
                "modelo": vehiculo.modelo,
                "cantidad_puertas": vehiculo.cantidad_puertas,
                "color": vehiculo.color,
                "precio_base": vehiculo.precio_base,
                "version": vehiculo.version
            }
        elif isinstance(vehiculo, VehiculoUsado):
            vehiculo_data = {
                "modelo": vehiculo.modelo,
                "cantidad_puertas": vehiculo.cantidad_puertas,
                "color": vehiculo.color,
                "precio_base": vehiculo.precio_base,
                "marca": vehiculo.marca,
                "patente": vehiculo.patente,
                "anio": vehiculo.anio,
                "kilometraje": vehiculo.kilometraje
            }
        else:
            continue

        vehiculos.append(vehiculo_data)

    with open("vehiculos.json", "w") as file:
        json.dump(vehiculos, file, indent=4)

    return True

def main():
    lista_vehiculos = leer_archivo_vehiculos()

    continuar = True
    while continuar:
        mostrar_menu()
        opcion = int(input("Ingrese una opción: "))
        continuar = ejecutar_opcion(opcion, lista_vehiculos)

if __name__ == '__main__':
    main()