import csv
from datetime import date

class Persona (object):
    """docstring for Persona"""
    def __init__(self, nombre, direccion, dni):
        self.nombre = nombre
        self.direccion = direccion
        self.dni = dni

class TallerCapacitacion (object):
    """docstrig for TallerCapacitacion"""
    def __init__(self, idTaller, nombre, vacantes, montoInscripcion):
        self.idTaller = idTaller
        self.nombre = nombre
        self.vacantes = vacantes
        self.montoInscripcion = montoInscripcion

class Inscripcion (object): 
    """docstring for Inscripcion"""
    def __init__(self, fechaInscripcion, pago=False):
        self.fechaInscripcion = fechaInscripcion
        self.pago = pago

class TallerManager (object):
    """docstring for TallerManager"""
    def __init__(self):
        self.talleres = []

    def cargar_talleres(self):
        with open('Talleres.csv', 'r') as file:
            reader = csv.reader(file)
            talleres_data = list(reader)[1:]
            for row in talleres_data:
                idTaller, nombre, vacantes, montoInscripcion = row
                taller = TallerCapacitacion(idTaller, nombre, int(vacantes), float(montoInscripcion))
                self.talleres.append(taller)

    def inscribir_persona(self, persona, taller_id):
        for taller in self.talleres:
            if taller.idTaller == taller_id:
                if taller.vacantes > 0:
                    taller.vacantes -= 1
                    inscripcion = Inscripcion(date.today())
                    persona.inscripciones.append((taller, inscripcion))
                    print("Inscripción exitosa.")
                else:
                    print("No hay vacantes disponibles para este taller.")
                return
        print("No se encontró un taller con el ID especificado.")

    def consultar_inscripcion(self, dni):
        for persona in personas:
            if persona.dni == dni:
                for taller, inscripcion in persona.inscripciones:
                    print(f"Nombre del taller: {taller.nombre}")
                    if not inscripcion.pago:
                        print(f"Monto adeudado: {taller.montoInscripcion}")
                    return
        print("No se encontró una persona con el DNI especificado.")

    def consultar_inscriptos(self, taller_id):
        for taller in self.talleres:
            if taller.idTaller == taller_id:
                print(f"Inscriptos en el taller {taller.nombre}:")
                for persona in personas:
                    for inscripcion_taller, _ in persona.inscripciones:
                        if inscripcion_taller == taller:
                            print(f"Nombre: {persona.nombre}, DNI: {persona.dni}")
                return
        print("No se encontró un taller con el ID especificado.")

    def registrar_pago(self, dni):
        for persona in personas:
            if persona.dni == dni:
                for _, inscripcion in persona.inscripciones:
                    inscripcion.pago = True
                print("Pago registrado.")
                return
        print("No se encontró una persona con el DNI especificado.")

    def guardar_inscripciones(self):
        with open('Inscripciones.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["DNI", "idTaller", "fechaInscripcion", "pago"])
            for persona in personas:
                for taller, inscripcion in persona.inscripciones:
                    writer.writerow([persona.dni, taller.idTaller, inscripcion.fechaInscripcion, inscripcion.pago])
        print("Inscripciones guardadas en el archivo 'Inscripciones.csv'.")

class ColeccionPersonas (object):
    """docstring for ColeccionPersonas"""
    def __init__(self):
        self.personas = []

    def agregar_persona(self, persona):
        self.personas.append(persona)

class ColeccionInscripciones (object):
    """docstring for ColeccionInscripciones"""
    def __init__(self):
        self.inscripciones = []

    def agregar_inscripcion(self, inscripcion):
        self.inscripciones.append(inscripcion)


if __name__ == '__main__':
 personas = ColeccionPersonas()
 inscripciones = ColeccionInscripciones()
 taller_manager = TallerManager()
 taller_manager.cargar_talleres()

 while True:
    print("\n----- Menú Principal -----")
    print("1. Inscribir persona en taller")
    print("2. Consultar inscripción")
    print("3. Consultar inscriptos en taller")
    print("4. Registrar pago")
    print("5. Guardar inscripciones en archivo")
    print("0. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Nombre de la persona: ")
        direccion = input("Dirección de la persona: ")
        dni = input("DNI de la persona: ")
        persona = Persona(nombre, direccion, dni)
        personas.agregar_persona(persona)

        taller_id = input("ID del taller: ")
        taller_manager.inscribir_persona(persona, taller_id)

    elif opcion == "2":
        dni = input("Ingrese el DNI de la persona: ")
        taller_manager.consultar_inscripcion(dni)

    elif opcion == "3":
        taller_id = input("ID del taller: ")
        taller_manager.consultar_inscriptos(taller_id)

    elif opcion == "4":
        dni = input("Ingrese el DNI de la persona: ")
        taller_manager.registrar_pago(dni)

    elif opcion == "5":
        taller_manager.guardar_inscripciones()

    elif opcion == "0":
        break

    else:
        print("Opción inválida. Por favor, ingrese una opción válida.")
