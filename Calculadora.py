# Una pequeña calculadora necesita un programa que permita 
# al usuario realizar distintas operaciones matemáticas 
# sin tener que ejecutar el programa varias veces. 
# El programa deberá mostrar un menú con las operaciones disponibles 
# (sumar, restar, multiplicar, dividir y salir) y permanecer 
# en funcionamiento hasta que el usuario decida finalizarlo. 
# En cada operación se solicitarán los datos necesarios, se mostrará 
# el resultado correspondiente y, si se introduce una opción no válida 
# o se intenta dividir entre cero, el programa deberá informar del error 
# y volver a mostrar el menú.

opcion = 0
while opcion != 5:
    print("--Calculadora--")
    print("-Opciones-")
    print("1 sumar")
    print("2 restar")
    print("3 multiplicar")
    print("4 dividir")
    print("99 exit")
    num1 = float(input("Dime el primer numero: "))
    num2 = float(input("Dime el segundo numero: "))
    numero = int(input("Elije una opción: "))
    print("Numero: " , numero)
    if numero == 1:
        print("suma!")
        suma = num1 + num2
        print("La suma del primer y el segundo numero es: ", suma)
    elif numero == 2:
        print("Resta!")
        resta = num1 - num2
        print("La resta de los dos numeros es: ", resta)
    elif numero == 3:
        print("multiplicacion: ")
        multi = num1 * num2
        print("La multiplicacion de lso dos numeros es: ", multi)
    elif numero == 4:
        print("Divison")
        divi = num1 / num2
        print("La multiplicacion de lso dos numeros es: ", divi)
    elif numero == 99:
        print("saliendo...")
        opcion = 5
    else:
        print("Elige otra opcion, esta es inexistente")







