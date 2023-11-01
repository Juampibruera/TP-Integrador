from Clases import Estudiante, Profesor, Curso, Archivo, Carrera
from Generador_Contrasenias import gen_contrasenia

# ----lISTAS---

estudiante1 = Estudiante(
    "1111", 2023, "Nicolas", "Bertoni", "Nicobertoni@gmail.com", "Azul"
)
Estudiante.estudiantes.append(estudiante1)

estudiante2 = Estudiante(
    "2222", 2023, "Juan Pablo", "Bruera", "JuanPabloBruera@gmail.com", "Dorado"
)
Estudiante.estudiantes.append(estudiante2)

estudiante3 = Estudiante(
    "3333", 2023, "Martin", "Honores", "MartinHonores@gmail.com", "Rojo"
)
Estudiante.estudiantes.append(estudiante3)

profesor1 = Profesor(
    "Analista en Sistemas",
    2005,
    "Lucas",
    "Rodriguez",
    "LucasRodriguez@gmail.com",
    "Rosario",
)
Profesor.profesores.append(profesor1)

profesor2 = Profesor(
    "Ingeniero Civil",
    2014,
    "Roberto",
    "Galati",
    "RobertoGalati@gmail.com",
    "Buenos Aires",
)
Profesor.profesores.append(profesor2)

# Menú principal
opcion = 0

while opcion != 4:
    print("Menú:")
    print("1. Ingresar como alumno")
    print("2. Ingresar como profesor")
    print("3. Ver cursos")
    print("4. Salir")

    opcion = int(input("Selecciona una opción (1/2/3/4): "))

    if opcion == 1:
        print("Usted está por ingresar como alumno")
        email = str(input("Ingrese el mail: "))
        contrasenia = str(input("Ingrese su contraseña: "))
        email_encontrado = False
        contrasenia_encontrada = False
        for e in Estudiante.estudiantes:
            if email == e.get_email():
                if e.validar_credenciales(email, contrasenia) == True:
                    print("Verificado")
                    contrasenia_encontrada = True
                    sub_opcion_alumno = 0
                    while sub_opcion_alumno != 4:
                        print("1. Matricularse a un curso")
                        print("2. Desmatricularse a un curso")
                        print("3. Ver curso")
                        print("4. Volver al menú principal")
                        sub_opcion_alumno = int(
                            input("Selecciona una opción (1/2/3) \n")
                        )
                        if sub_opcion_alumno == 1:
                            e.matricular_en_curso()
                        elif sub_opcion_alumno == 2:
                            e.desmatricular_curso()
                        elif sub_opcion_alumno == 3:
                            for indice, curso in enumerate(e.get_mis_cursos()):
                                print(f"{indice + 1}. {curso.get_nombre()}")
                            indice_curso = int(
                                input(
                                    "Ingrese el índice de un curso para ver sus archivos: "
                                )
                            )
                            for indice, curso in enumerate(e.get_mis_cursos()):
                                if (indice + 1) == indice_curso:
                                    print(
                                        f"Nombre del curso:{curso.get_nombre()} \n Listado de archivos del curso: "
                                    )
                                else:
                                    print(
                                        "El índice ingresado no coincide con ningun curso."
                                    )
                        elif sub_opcion_alumno == 4:
                            print("Volviendo al menú principal...")
                            break
                        else:
                            print("Ingrese una opción válida")
                if contrasenia_encontrada == False:
                    "Error: contraseña incorrecta."
                    email_encontrado = True
        if email_encontrado == False:
            print("El email ingresado no existe, debe darse de alta en Alumnado.")

    elif opcion == 2:
        print("Usted está por ingresar como profesor")
        _email = str(input("Ingrese el mail: "))
        _contrasenia = str(input("Ingrese su contraseña: "))
        email_encontrado = False
        contrasenia_encontrada = False
        for p in Profesor.profesores:
            if _email == p.get_email():
                if p.validar_credenciales(_email, _contrasenia) == True:
                    print("Verificado")
                    contrasenia_encontrada = True
                    sub_opcion_profesor = 0
                    while sub_opcion_profesor != 3:
                        print("1. Dictar curso")
                        print("2. Ver curso")
                        print("3. Volver al menú principal")
                        sub_opcion_profesor = int(
                            input("Selecciona una opción (1/2/3) \n")
                        )
                        if sub_opcion_profesor == 1:
                            p.dictar_curso()
                        elif sub_opcion_profesor == 2:
                            print(f"Listado de cursos dictados por {p.get_nombre()}:")
                            for indice, c in enumerate(p.get_mis_cursos()):
                                print(f"{indice + 1}. {c.get_nombre()}")
                            indice_curso = int(
                                input(
                                    "Ingrese el índice de un curso para ver sus datos: "
                                )
                            )
                            for indice, c in enumerate(p.get_mis_cursos()):
                                if (indice + 1) == indice_curso:
                                    if c in p.get_mis_cursos():
                                        print(
                                            f"Nombre del curso: {c.get_nombre()} \n Contraseña: {c.get_contrasenia_matriculacion()} \n Código: {c.get_codigo()} \n Cantidad de archivos:"
                                        )
                                    while True:
                                        agregar_adjunto = int(
                                            input(
                                                "¿Desea agregar un archivo adjunto? \n 1. Si \n 2.No"
                                            )
                                        )
                                        if agregar_adjunto == 1:
                                            c.nuevo_archivo()
                                        elif agregar_adjunto == 2:
                                            break
                                        else:
                                            print("Seleccione una opción válida")
                        elif sub_opcion_profesor == 3:
                            print("Volviendo al menú principal...")
                            break
                        else:
                            print("Ingrese una opción válida")
                if contrasenia_encontrada == False:
                    "Error: contraseña incorrecta."
                email_encontrado = True
        if email_encontrado == False:
            print("El email ingresado no existe.")
            dar_alta = str(
                input("Ingrese la contraseña para darse de alta como profesor: ")
            )
            if dar_alta == "admin":
                registrar_profesor()
                print("Profesor registrado exitosamente.")

    elif opcion == 3:
        print("Cursos disponibles:")
        lista_cursos_ordenada = sorted(Curso.cursos, key=lambda x: x.get_nombre)
        for curso in lista_cursos_ordenada:
            print("-" * 10)
            print(
                f"Nombre: {curso.get_nombre()}, Carrera: Tecnicatura Universitaria en Programación"
            )

    else:
        print("Saliendo del sistema...")
        break
