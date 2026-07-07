# El programa debe mostrar un menú con las siguientes opciones:
# 1. Registrar alumnos
# 2. Introducir notas de un alumno
# 3. Calcular media de un alumno
# 4. Mostrar alumnos aprobados y suspendidos
# 5. Mostrar estadísticas generales
# 6. Salir
# En la opción de registrar alumnos, el programa debe preguntar cuántos alumnos se
# quieren registrar. Después, usando un for, debe pedir el nombre de cada alumno. El
# programa debe guardar la cantidad total de alumnos registrados.
# En la opción de introducir notas, el programa debe pedir cuántas notas se quieren
# introducir para un alumno. Después, usando un for, debe pedir cada una de las
# notas. El programa debe controlar con if si cada nota es válida, es decir, si está entre
# 0 y 10. Si una nota no es válida, debe mostrar un mensaje de error.
# En la opción de calcular media, el programa debe calcular la media de las notas
# introducidas y mostrar si el alumno está aprobado o suspendido. Un alumno se
# considera aprobado si su media es igual o superior a 5.
# En la opción de mostrar alumnos aprobados y suspendidos, el programa debe
# mostrar cuántos alumnos han aprobado y cuántos han suspendido.
# En la opción de estadísticas generales, el programa debe mostrar el número total
# de alumnos registrados, el número total de notas introducidas, la nota más alta, la
# nota más baja y la media general de todas las notas.
# El programa debe usar obligatoriamente while para repetir el menú principal, for
# para repetir la introducción de alumnos o notas, e if, elif y else para controlar las
# opciones del menú y las condiciones del programa.
# El programa debe finalizar únicamente cuando el usuario elija la opción de salir

opcion = 0
alumnos_registrados = 0
notas = 0
suma_notas = 0
aprobados = 0
suspendidos = 0
nota_alta = 0
nota_baja = 10
media = 0

while opcion != 6:

    print("\nMENÚ")
    print("1 - Registrar alumnos")
    print("2 - Introducir notas de un alumno")
    print("3 - Calcular media de un alumno")
    print("4 - Mostrar alumnos aprobados y suspendidos")
    print("5 - Mostrar estadísticas generales")
    print("6 - Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:

        cantidad_alumnos = int(input("¿Cuántos alumnos quieres registrar? "))

        for i in range(cantidad_alumnos):
            nombre = input("Nombre del alumno: ")
            alumnos_registrados += 1

    elif opcion == 2:

        nombre = input("¿De qué alumno son las notas? ")

        notas = 0
        suma_notas = 0
        nota_alta = 10
        nota_baja = 0

        cantidad_notas = int(input("¿Cuántas notas vas a introducir? "))

        for i in range(cantidad_notas):

            nota = float(input("Introduce una nota: "))

            if nota >= 0 and nota <= 10:

                notas += 1
                suma_notas += nota

                if nota < nota_alta:
                    nota_alta = nota

                if nota > nota_baja:
                    nota_baja += 1

            else:
                print("ERROR. Nota no válida.")

    elif opcion == 3:

        if notas > 0:

            media = suma_notas / notas

            print("Media:", media)

            if media >= 5:
                print("Alumno APROBADO")
                
            else:
                print("Alumno SUSPENDIDO")

        else:
            print("No hay notas.")

    elif opcion == 4:

        aprobados = 0
        suspendidos = 0

        if notas > 0:

            if media >= 5:
                aprobados += 1
            else:
                suspendidos += 1

        print("Aprobados:", aprobados)
        print("Suspendidos:", suspendidos)

    elif opcion == 5:

        print("Alumnos registrados:", alumnos_registrados)
        print("Número de notas:", suma_notas)

        if notas > 0:

            print("Nota más alta:", nota_alta)
            print("Nota más baja:", nota_baja)
            print("Media general:", media)

        else:
            print("No hay notas.")

    elif opcion == 6:

        print("Programa finalizado.")

    else:

        print("Opción incorrecta.")
    
    