import csv
import numpy as np
from datetime import date

class Empleado (object):
    """docstring for Empleado"""
    def __init__(self, dni, nombre, direccion, telefono):
        self.dni = dni
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

class EmpleadoPlanta(Empleado):
    """docstring for EmpleadoPlanta"""
    def __init__(self, dni, nombre, direccion, telefono, sueldo_basico, antiguedad):
        super().__init__(dni, nombre, direccion, telefono)
        self.sueldo_basico = sueldo_basico
        self.antiguedad = antiguedad

    def calcular_sueldo(self):
        return self.sueldo_basico + (0.01 * self.sueldo_basico * self.antiguedad)

class EmpleadoContratado(Empleado):
    """docstring for EmpleadoContratado"""
    def __init__(self, dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas_trabajadas, valor_hora):
        super().__init__(dni, nombre, direccion, telefono)
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.horas_trabajadas = horas_trabajadas
        self.valor_hora = valor_hora

    def calcular_sueldo(self):
        return self.horas_trabajadas * self.valor_hora

class EmpleadoExterno(Empleado):
    """docstring for EmpleadoExterno"""
    def __init__(self, dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_fin, monto_viatico, costo_obra, monto_seguro_vida):
        super().__init__(dni, nombre, direccion, telefono)
        self.tarea = tarea
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.monto_viatico = monto_viatico
        self.costo_obra = costo_obra
        self.monto_seguro_vida = monto_seguro_vida

    def calcular_sueldo(self):
        return self.costo_obra - self.monto_viatico - self.monto_seguro_vida

class ColeccionEmpleados (object):
    """docstring for ColeccionEmpleados"""
    def __init__(self, size):
        self.empleados = np.empty(size, dtype=object)

    def agregar_empleado(self, empleado):
        for i in range(len(self.empleados)):
            if self.empleados[i] is None:
                self.empleados[i] = empleado
                break

    def buscar_empleado(self, dni):
        for empleado in self.empleados:
            if empleado is not None and empleado.dni == dni:
                return empleado
        return None

if __name__ == '__main__':
 empleados = ColeccionEmpleados(int(input("Ingrese el tamaño de la colección de empleados: ")))
with open('planta.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dni, nombre, direccion, telefono, sueldo_basico, antiguedad = row
        empleado = EmpleadoPlanta(dni, nombre, direccion, telefono, float(sueldo_basico), int(antiguedad))
        empleados.agregar_empleado(empleado)

with open('contratados.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dni, nombre, direccion, telefono, fecha_inicio, fecha_fin, horas_trabajadas, valor_hora = row
        empleado = EmpleadoContratado(dni, nombre, direccion, telefono, date.fromisoformat(fecha_inicio), date.fromisoformat(fecha_fin), int(horas_trabajadas), float(valor_hora))
        empleados.agregar_empleado(empleado)

with open('externos.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        dni, nombre, direccion, telefono, tarea, fecha_inicio, fecha_fin, monto_viatico, costo_obra, monto_seguro_vida = row
        empleado = EmpleadoExterno(dni, nombre, direccion, telefono, tarea, date.fromisoformat(fecha_inicio), date.fromisoformat(fecha_fin), float(monto_viatico), float(costo_obra), float(monto_seguro_vida))
        empleados.agregar_empleado(empleado)

while True:
    print("\n----- Menú Principal -----")
    print("1. Registrar horas")
    print("2. Total de tarea")
    print("3. Ayuda Económica")
    print("4. Calcular sueldo")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        dni = input("Ingrese el DNI del empleado: ")
        horas_trabajadas = int(input("Ingrese la cantidad de horas trabajadas: "))
        empleado = empleados.buscar_empleado(dni)
        if empleado is not None and isinstance(empleado, EmpleadoContratado):
            empleado.horas_trabajadas += horas_trabajadas
            print("Horas registradas exitosamente.")
        else:
            print("No se encontró un empleado contratado con ese DNI.")

    elif opcion == "2":
        tarea = input("Ingrese la tarea: ")
        total = 0
        for empleado in empleados.empleados:
            if isinstance(empleado, EmpleadoExterno) and empleado.tarea == tarea and empleado.fecha_fin >= date.today():
                total += empleado.costo_obra
        print(f"El monto a pagar para la tarea '{tarea}' es: {total}")

    elif opcion == "3":
        print("Empleados con derecho a ayuda económica:")
        for empleado in empleados.empleados:
            if empleado is not None and empleado.calcular_sueldo() < 150000:
                print(f"Nombre: {empleado.nombre}, Dirección: {empleado.direccion}, DNI: {empleado.dni}")

    elif opcion == "4":
        print("Sueldos de los empleados:")
        for empleado in empleados.empleados:
            if empleado is not None:
                sueldo = empleado.calcular_sueldo()
                print(f"Nombre: {empleado.nombre}, Teléfono: {empleado.telefono}, Sueldo: {sueldo}")

    elif opcion == "0":
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
