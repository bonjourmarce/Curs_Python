#Crea un programa en Python que simule la gestión básica de una tienda usando un menú con while. 
#El usuario debe poder vender productos, añadir stock, consultar el stock actual, consultar el dinero total ganado y salir del programa. 
#El programa debe controlar que no se puedan vender productos si no queda stock disponible

opened = 0
stockActual = 99
precio = 10
dineroTOTganado = 0

while opened != 4:
    print("--Opciones--")
    print("1 Vender productos")
    print("2 Añadir stock")
    print("3 consultar stock actual")
    print("4 consultar dinero total ganado")
    print("99 exit")

    opt = int(input("Selecciona un numero: "))
    if opt == 1:
        cantProd  = int(input("Dime la cantidad de unidades del producto: "))
        if cantProd <= stockActual:
            dineroTOTganado = dineroTOTganado + cantProd*precio
            stockActual = stockActual - cantProd
            print("Productos vendido!")
        else:
            print("No tienes suficiente stock")
    elif opt == 2: 
        addStock = int(input("Dime cuanto de stock quieres añadir: "))
        if addStock > 0:
            stockActual += addStock
        else:
            print("No puedes agregar 0 o por debajo")
    elif opt == 3:
        print("El stock actual és: ", stockActual)
    elif opt == 4:
        print("El dinero total ganado és de: ",dineroTOTganado,"€")
    elif opt == 99:
        print("saliendo...")
        opened = 4
    else:
        print("Error")

        
        


        
        
    