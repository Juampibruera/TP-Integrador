from Generador_Contrasenias import gen_contrasenia
from datetime import datetime
from abc import ABC


class Usuario(ABC):
    def __init__(self, nombre, apellido, email, contrasenia):
        self._nombre = nombre
        self._apellido = apellido
        self._email = email
        self._contrasenia = contrasenia

    def get_nombre(self):
        return self._nombre

    def get_apellido(self):
        return self._apellido

    def get_email(self):
        return self._email

    def get_contrasenia(self):
        return self._contrasenia

    def validar_credenciales(self, email, contrasenia):
        return self._email == email and self._contrasenia == contrasenia


class Estudiante(Usuario):
    estudiantes = []

    def __init__(
        self, legajo, anio_inscripcion_carrera, nombre, apellido, email, contrasenia
    ):
        super().__init__(nombre, apellido, email, contrasenia)
        self._legajo = legajo
        self._anio_inscripcion_carrera = anio_inscripcion_carrera
        self._mis_cursos = []

    def matricular_en_curso(self):
        lista_cursos = Curso.cursos
        for indice, curso in enumerate(lista_cursos):
            print(f"{indice + 1}. {curso.get_nombre()}")

        indice_curso = int(input("Ingrese el índice de un curso para matricularse: "))

        if 1 <= indice_curso <= len(lista_cursos):
            curso_seleccionado = lista_cursos[indice_curso - 1]
            contrasenia_ingresada = input("Ingrese la clave de matriculación: ")

            if (
                contrasenia_ingresada
                == curso_seleccionado.get_contrasenia_matriculacion()
            ):
                self._mis_cursos.append(curso_seleccionado)
                print("Se ha matriculado exitosamente.")
            else:
                print("Clave incorrecta.")
        else:
            print("El índice ingresado no es válido.")

    def desmatricular_curso(self):
        if not self._mis_cursos:
            print("No estás matriculado en ningún curso.")
            return

        print("Cursos en los que estás matriculado:")
        for indice, curso in enumerate(self._mis_cursos):
            print(f"{indice + 1}. {curso.get_nombre()}")

        indice_curso = int(
            input("Ingrese el índice del curso del que deseas desmatricularte: ")
        )

        if 1 <= indice_curso <= len(self._mis_cursos):
            curso_desmatricular = self._mis_cursos[indice_curso - 1]
            self._mis_cursos.remove(curso_desmatricular)
            print(
                f"Te has desmatriculado del curso {curso_desmatricular.get_nombre()} con éxito."
            )
        else:
            print("El índice ingresado no es válido.")

    def get_legajo(self):
        return self._legajo

    def get_anio_inscripcion_carrera(self):
        return self._anio_inscripcion_carrera

    def get_mis_cursos(self):
        return self._mis_cursos


class Profesor(Usuario):
    profesores = []

    def __init__(self, titulo, anio_egreso, nombre, apellido, email, contrasenia):
        super().__init__(nombre, apellido, email, contrasenia)
        self._titulo = titulo
        self._anio_egreso = anio_egreso
        self._mis_cursos = []

    def dictar_curso(self):
        nuevo_curso = input("Ingrese el nombre del curso: ")
        nueva_contrasenia = gen_contrasenia(6) 
        curso_creado = Curso(nuevo_curso, nueva_contrasenia)
        Curso.cursos.append(curso_creado)
        self._mis_cursos.append(curso_creado)
        print(f"Se ha creado el siguiente curso exitosamente.")
        print("Nombre: ", nuevo_curso)
        print("Contraseña: ", nueva_contrasenia)
        print("Código del curso:", curso_creado.get_codigo())

    def get_titulo(self):
        return self._titulo

    def get_anio_egreso(self):
        return self._anio_egreso

    def get_mis_cursos(self):
        return self._mis_cursos


class Curso:
    cursos = []
    prox_cod = 1

    def __init__(self, nombre, contrasenia_matriculacion):
        self._nombre = nombre
        self._codigo = Curso.prox_cod
        self._contrasenia_matriculacion = contrasenia_matriculacion
        Curso.prox_cod += 1

    def nuevo_archivo(self, nombre, formato):
        fecha = datetime.now()
        nuevo_archivo = Archivo(nombre, fecha, formato)

    def get_nombre(self):
        return self._nombre

    def get_contrasenia_matriculacion(self):
        return self._contrasenia_matriculacion

    def get_codigo(self):
        return self._codigo

class Carrera:
    def __init__(self, nombre, cant_anios):
        self._nombre = nombre
        self._cant_anios = cant_anios

    def get_nombre(self):
        return self._nombre

    def get_cant_anios(self):
        return self._cant_anios


class Archivo:
    def __init__(self, nombre, fecha, formato):
        self._nombre = nombre
        self._fecha = fecha
        self._formato = formato

    def get_nombre(self):
        return self._nombre

    def get_fecha(self):
        return self._fecha

    def get_formato(self):
        return self._formato
