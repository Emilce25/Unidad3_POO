import json

class AgenteUniversitario (object):
    """docstring for AgenteUniversitario"""
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad):
        self.cuil = cuil
        self.apellido = apellido
        self.nombre = nombre
        self.sueldo_basico = sueldo_basico
        self.antiguedad = antiguedad

    def calcular_sueldo(self):
        pass

class Docente(AgenteUniversitario):
    """docstring for Docente"""
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.carrera = carrera
        self.cargo = cargo
        self.catedra = catedra

    def calcular_sueldo(self):
        porcentaje_cargo = 0.1
        sueldo = self.sueldo_basico + (self.sueldo_basico * self.antiguedad) + (self.sueldo_basico * porcentaje_cargo)
        return sueldo

class PersonalApoyo(AgenteUniversitario):
    """docstring for PersonalApoyo"""
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.categoria = categoria

    def calcular_sueldo(self):
        sueldo = self.sueldo_basico + (self.sueldo_basico * self.antiguedad)
        return sueldo

class Investigador(AgenteUniversitario):
    """docstring for Investigador"""
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion):
        super().__init__(cuil, apellido, nombre, sueldo_basico, antiguedad)
        self.area_investigacion = area_investigacion
        self.tipo_investigacion = tipo_investigacion

    def calcular_sueldo(self):
        sueldo = self.sueldo_basico + (self.sueldo_basico * self.antiguedad)
        return sueldo

class DocenteInvestigador(Docente, Investigador):
    """docstring for DocenteInvestigador"""
    def __init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra, area_investigacion, tipo_investigacion, categoria, importe_extra):
        Docente.__init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, carrera, cargo, catedra)
        Investigador.__init__(self, cuil, apellido, nombre, sueldo_basico, antiguedad, area_investigacion, tipo_investigacion)
        self.categoria = categoria
        self.importe_extra = importe_extra

    def calcular_sueldo(self):
        porcentaje_categoria = 0.1
        sueldo_docente = super().calcular_sueldo()
        sueldo = sueldo_docente + (sueldo_docente * porcentaje_categoria) + self.importe_extra
        return sueldo

class ColeccionAgentes (object):
    """docstring for ColeccionAgentes"""
    def __init__(self):
        self.agentes = []

    def insertarElemento(self, agente, posicion):
        if posicion < 0 or posicion > len(self.agentes):
            raise Exception("Posición inválida")
        self.agentes.insert(posicion, agente)

    def agregarElemento(self, agente):
        self.agentes.append(agente)

    def mostrarElemento(self, posicion):
        if posicion < 0 or posicion >= len(self.agentes):
            raise Exception("Posición inválida")
        agente = self.agentes[posicion]
        print(f"Tipo de agente: {type(agente).__name__}")

if __name__ == '__main__':

 coleccion_agentes = ColeccionAgentes()

while True:
    print("\n==== Menú de opciones ====")
    print("1) Insertar agentes a la colección.")
    print("2) Agregar agentes a la colección.")
    print("3) Mostrar tipo de agente en una posición específica.")
    print("4) Listar docentes investigadores de una carrera ordenados por nombre.")
    print("5) Contar docentes investigadores e investigadores en un área de investigación.")
    print("6) Listar todos los agentes ordenados por apellido.")
    print("7) Listar docentes investigadores con una categoría y calcular el importe total.")
    print("8) Almacenar los datos de los agentes en el archivo 'personal.json'.")
    print("9) Salir")

    opcion = int(input("Ingrese el número de opción: "))

    if opcion == 1:
        pass

    elif opcion == 2:
        pass

    elif opcion == 3:
        posicion = int(input("Ingrese la posición: "))
        try:
            coleccion_agentes.mostrarElemento(posicion)
        except Exception as e:
            print("Error:", e)

    elif opcion == 4:
        carrera = input("Ingrese el nombre de la carrera: ")
        pass

    elif opcion == 5:
        area_investigacion = input("Ingrese el área de investigación: ")
        pass

    elif opcion == 6:
        pass

    elif opcion == 7:
        categoria = input("Ingrese la categoría de investigación (I, II, III, IV o V): ")
        pass

    elif opcion == 8:
        pass

    elif opcion == 9:
        break

    else:
        print("Opción inválida. Intente nuevamente.")
