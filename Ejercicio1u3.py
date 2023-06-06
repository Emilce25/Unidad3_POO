import csv
class Facultad (object):
    """docstring for Facultad"""
    def _init_(self, codigo, nombre, direccion, localidad, telefono):
        self.codigo = codigo
        self.nombre = nombre
        self.direccion = direccion
        self.localidad = localidad
        self.telefono = telefono
        self.carreras = []

    def agregar_carrera(self, carrera):
        self.carreras.append(carrera)

    def obtener_carreras(self):
        return self.carreras


class Carrera (object):
    """docstring for Carrera"""
    def _init_(self, codigo, nombre, fecha_inicio, duracion, titulo):
        self.codigo = codigo
        self.nombre = nombre
        self.fecha_inicio = fecha_inicio
        self.duracion = duracion
        self.titulo = titulo


class ManejaFacultades (object):
    """docstring for ManejaFacultades"""
    def _init_(self):
        self.facultades = []

    def cargar_facultades_desde_archivo(self, archivo):
        with open(archivo, 'r') as file:
            lineas = file.readlines()
            for i in range(0, len(lineas), 2):
                datos_facultad = lineas[i].strip().split(',')
                codigo = datos_facultad[0]
                nombre = datos_facultad[1]
                direccion = datos_facultad[2]
                localidad = datos_facultad[3]
                telefono = datos_facultad[4]
                facultad = Facultad(codigo, nombre, direccion, localidad, telefono)

                lineas_carreras = lineas[i + 1].strip().split('\n')
                for linea_carrera in lineas_carreras:
                    datos_carrera = linea_carrera.split(',')
                    codigo_carrera = datos_carrera[0]
                    nombre_carrera = datos_carrera[1]
                    fecha_inicio = datos_carrera[2]
                    duracion = datos_carrera[3]
                    titulo = datos_carrera[4]
                    carrera = Carrera(codigo_carrera, nombre_carrera, fecha_inicio, duracion, titulo)
                    facultad.agregar_carrera(carrera)

                self.facultades.append(facultad)

    def buscar_facultad_por_codigo(self, codigo_facultad):
        for facultad in self.facultades:
            if facultad.codigo == codigo_facultad:
                return facultad
        return None

    def buscar_carrera_por_nombre(self, nombre_carrera):
        for facultad in self.facultades:
            carreras = facultad.obtener_carreras()
            for carrera in carreras:
                if carrera.nombre == nombre_carrera:
                    return carrera
        return None


def mostrar_carreras_facultad(manejador_facultades):
    codigo_facultad = input("Ingrese el código de la facultad: ")
    facultad = manejador_facultades.buscar_facultad_por_codigo(codigo_facultad)
    if facultad:
        print("Nombre de la facultad:", facultad.nombre)
        carreras = facultad.obtener_carreras()
        for carrera in carreras:
            print("Nombre de la carrera:", carrera.nombre)
            print("Duración:", carrera.duracion)
    else:
        print("No se encontró la facultad con el código ingresado.")


def mostrar_facultad_por_carrera(manejador_facultades):
    nombre_carrera = input("Ingrese el nombre de la carrera: ")
    carrera = manejador_facultades.buscar_carrera_por_nombre(nombre_carrera)
    if carrera:
        codigo_facultad = carrera.codigo[0]
        facultad = manejador_facultades.buscar_facultad_por_codigo(codigo_facultad)
        if facultad:
            print("Código de la carrera:", carrera.codigo)
            print("Nombre de la carrera:", carrera.nombre)
            print("Localidad de la facultad:", facultad.localidad)
        else:
            print("No se encontró la facultad asociada a la carrera.")
    else:
        print("No se encontró la carrera con el nombre ingresado.")
        
if __name__ == '__main__':
 manejador_facultades = ManejaFacultades()
 manejador_facultades.cargar_facultades_desde_archivo('Facultades.csv')

 opcion = 0
 while opcion != 3:
    print("------ MENÚ ------")
    print("1. Mostrar carreras de una facultad")
    print("2. Mostrar facultad por carrera")
    print("3. Salir")

    opcion = int(input("Ingrese una opción: "))

    if opcion == 1:
        mostrar_carreras_facultad(manejador_facultades)
    elif opcion == 2:
        mostrar_facultad_por_carrera(manejador_facultades)
    elif opcion == 3:
        print("¡Hasta luego!")
    else:
        print("Opción inválida. Intente nuevamente.")