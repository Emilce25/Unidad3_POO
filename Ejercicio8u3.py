from abc import ABC, abstractmethod

class ITesorero(ABC):
    @abstractmethod
    def gastosSueldoPorEmpleado(self, dni):
        pass

class IDirector(ABC):
    @abstractmethod
    def modificarBasico(self, dni, nuevoBasico):
        pass

    @abstractmethod
    def modificarPorcentajePorCargo(self, dni, nuevoPorcentaje):
        pass

    @abstractmethod
    def modificarPorcentajePorCategoria(self, dni, nuevoPorcentaje):
        pass

    @abstractmethod
    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        pass



class ColeccionAgentes(ITesorero, IDirector):

    def gastosSueldoPorEmpleado(self, dni):
        total_gastos = 0
        for agente in self.agentes:
            if agente.dni == dni:
                total_gastos += agente.calcular_sueldo()
        return total_gastos

    
    def modificarBasico(self, dni, nuevoBasico):
        for agente in self.agentes:
            if agente.dni == dni:
                agente.sueldo_basico = nuevoBasico

    def modificarPorcentajePorCargo(self, dni, nuevoPorcentaje):
        for agente in self.agentes:
            if isinstance(agente, Docente):
                if agente.dni == dni:
                    agente.porcentaje_cargo = nuevoPorcentaje

    def modificarPorcentajePorCategoria(self, dni, nuevoPorcentaje):
        for agente in self.agentes:
            if isinstance(agente, PersonalApoyo):
                if agente.dni == dni:
                    agente.porcentaje_categoria = nuevoPorcentaje

    def modificarImporteExtra(self, dni, nuevoImporteExtra):
        for agente in self.agentes:
            if isinstance(agente, DocenteInvestigador):
                if agente.dni == dni:
                    agente.importe_extra = nuevoImporteExtra

if __name__ == '__main__':

 coleccion_agentes = ColeccionAgentes()


 username = input("Ingrese el nombre de usuario: ")
 password = input("Ingrese la contraseña: ")

if username == "uTesoreso" and password == "ag@74ck":
    
    opcion_tesorero = int(input("Opciones del Tesorero:\n1) Consultar gastos de sueldos por empleado.\nIngrese la opción: "))

    if opcion_tesorero == 1:
        dni_empleado = input("Ingrese el número de documento del empleado: ")
        gastos = coleccion_agentes.gastosSueldoPorEmpleado(dni_empleado)
        print("Gastos de sueldo para el empleado:", gastos)

elif username == "uDirector" and password == "ufC77#!1":
   
    opcion_director = 0

    while opcion_director != 9:
        print("\nOpciones del Director:")
        print("1) Modificar sueldo básico de todos los agentes.")
        print("2) Modificar porcentaje por cargo de un docente.")
        print("3) Modificar porcentaje por categoría de un personal de apoyo.")
        print("4) Modificar importe extra de un docente investigador.")
        print("9) Salir")
        opcion_director = int(input("Ingrese la opción: "))

        if opcion_director == 1:
            dni_empleado = input("Ingrese el número de documento del empleado: ")
            nuevo_basico = float(input("Ingrese el nuevo sueldo básico: "))
            coleccion_agentes.modificarBasico(dni_empleado, nuevo_basico)
            print("Sueldo básico modificado.")

        elif opcion_director == 2:
            dni_empleado = input("Ingrese el número de documento del docente: ")
            nuevo_porcentaje = float(input("Ingrese el nuevo porcentaje por cargo: "))
            coleccion_agentes.modificarPorcentajePorCargo(dni_empleado, nuevo_porcentaje)
            print("Porcentaje por cargo modificado.")

        elif opcion_director == 3:
            dni_empleado = input("Ingrese el número de documento del personal de apoyo: ")
            nuevo_porcentaje = float(input("Ingrese el nuevo porcentaje por categoría: "))
            coleccion_agentes.modificarPorcentajePorCategoria(dni_empleado, nuevo_porcentaje)
            print("Porcentaje por categoría modificado.")

        elif opcion_director == 4:
            dni_empleado = input("Ingrese el número de documento del docente investigador: ")
            nuevo_importe_extra = float(input("Ingrese el nuevo importe extra: "))
            coleccion_agentes.modificarImporteExtra(dni_empleado, nuevo_importe_extra)
            print("Importe extra modificado.")

        elif opcion_director == 9:
            break

else:
    print("Nombre de usuario o contraseña incorrectos.")
