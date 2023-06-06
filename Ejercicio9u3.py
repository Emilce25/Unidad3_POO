import json
import unittest

class Vehiculo (object):
    """docstring for Vehiculo"""
    def _init_(self, modelo, cantidad_puertas, color, precio_base):
        self.modelo = modelo
        self.cantidad_puertas = cantidad_puertas
        self.color = color
        self.precio_base = precio_base

class VehiculoNuevo(Vehiculo):
    """docstring for VehiculoNuevo"""
    def _init_(self, modelo, cantidad_puertas, color, precio_base, version):
        super()._init_(modelo, cantidad_puertas, color, precio_base)
        self.version = version

    def calcular_precio_venta(self):
        precio_venta = self.precio_base + self.precio_base * 0.1
        if self.version == "full":
            precio_venta += self.precio_base * 0.02
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
        antiguedad = 2023 - self.anio
        porcentaje_descuento = antiguedad * 0.01
        if self.kilometraje > 100000:
            porcentaje_descuento += 0.02
        precio_venta = self.precio_base - self.precio_base * porcentaje_descuento
        return precio_venta

class TestFuncionalidades(unittest.TestCase):
    def setUp(self):
        with open('vehiculos.json', 'r') as file:
            self.vehiculos = json.load(file)

    def test_insertar_vehiculo_en_posicion(self):
        vehiculo = Vehiculo("Fiesta", 4, "Rojo", 150000)
        self.vehiculos.insert(0, vehiculo)
        self.assertEqual(self.vehiculos[0].modelo, "Fiesta")
        
        vehiculo = Vehiculo("Civic", 4, "Azul", 200000)
        self.vehiculos.insert(2, vehiculo)
        self.assertEqual(self.vehiculos[2].modelo, "Civic")
        
        vehiculo = Vehiculo("Gol", 2, "Blanco", 100000)
        self.vehiculos.insert(len(self.vehiculos), vehiculo)
        self.assertEqual(self.vehiculos[-1].modelo, "Gol")

    def test_agregar_vehiculo(self):
        vehiculo = Vehiculo("Corolla", 4, "Gris", 180000)
        self.vehiculos.append(vehiculo)
        self.assertEqual(self.vehiculos[-1].modelo, "Corolla")

    def test_obtener_vehiculo_por_posicion(self):
        vehiculo = self.vehiculos[2]
        self.assertEqual(vehiculo.modelo, "Gol")

    def test_modificar_precio_base_y_precio_venta(self):
        patente = "ABC123"
        nuevo_precio_base = 80000
        nuevo_precio_venta = 76000

        for vehiculo in self.vehiculos:
            if isinstance(vehiculo, VehiculoUsado) and vehiculo.patente == patente:
                vehiculo.precio_base = nuevo_precio_base
                precio_venta = vehiculo.calcular_precio_venta()
                self.assertEqual(precio_venta, nuevo_precio_venta)


if __name__ == '__main__':
    unittest.main()