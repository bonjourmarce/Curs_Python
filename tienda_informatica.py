# Ejercicio 2 — Gestión de una tienda de informática

# Crea un programa en Python que simule la gestión de una tienda de informática. El
# programa debe funcionar mediante un menú que se repita hasta que el usuario elija
# salir. El usuario podrá vender productos, añadir stock, consultar información de la
# tienda y generar un resumen final.
# El programa debe mostrar un menú con las siguientes opciones:

# 1. Mostrar productos disponibles
# 2. Vender productos
# 3. Añadir stock
# 4. Aplicar descuento a una venta
# 5. Mostrar resumen de ventas
# 6. Salir

# La tienda tendrá tres productos: teclados, ratones y monitores. Cada producto
# tendrá un precio y un stock inicial. El programa debe controlar en todo momento
# cuántas unidades quedan de cada producto.
# En la opción de mostrar productos disponibles, el programa debe enseñar el
# nombre de cada producto, su precio y el stock actual.
# En la opción de vender productos, el programa debe preguntar qué producto quiere
# comprar el cliente y cuántas unidades quiere comprar. El programa debe
# comprobar si hay stock suficiente. Si hay stock, debe restar las unidades vendidas,
# calcular el precio total de la venta y sumarlo al dinero total ganado. Si no hay stock
# suficiente, debe mostrar un mensaje indicando que no se puede realizar la venta

# En la opción de añadir stock, el programa debe preguntar a cuántos productos se
# les quiere añadir stock. Después, usando un for, debe pedir el producto y la
# cantidad que se quiere añadir. El programa debe controlar que la cantidad
# introducida sea positiva.
# En la opción de aplicar descuento a una venta, el programa debe pedir el precio de
# una venta y un porcentaje de descuento. Si el descuento es válido, debe calcular el
# precio final. Si el descuento no es válido, debe mostrar un mensaje de error.
# En la opción de mostrar resumen de ventas, el programa debe mostrar el dinero
# total ganado, el número total de productos vendidos, el producto más vendido, el
# producto menos vendido y el stock restante de cada producto.
# El programa debe usar obligatoriamente while para repetir el menú principal, for
# para repetir procesos de introducción de datos, e if, elif y else para controlar las
# opciones del menú, las ventas, los descuentos y las comprobaciones de stock.
# El programa debe finalizar únicamente cuando el usuario elija la opción de salir. Al
# salir, debe mostrar un resumen final con el total ganado, el total de productos
# vendidos y el stock final de la tienda.

# VARIABLES

opcion = 0

precio_teclado = 25
precio_raton = 15
precio_monitor = 180

stock_teclado = 10
stock_raton = 15
stock_monitor = 5

vendidos_teclado = 0
vendidos_raton = 0
vendidos_monitor = 0

dinero_total = 0
productos_vendidos = 0

# MENU

while opcion != 6:
    print("\nMENÚ")
    print("1 - Mostrar productos disponibles")
    print("2 - Vender productos")
    print("3 - Añadir stock")
    print("4 - Aplicar descuento a una venta")
    print("5 - Mostrar resumen de ventas")
    print("6 - Salir")

    opcion = int(input("Elige una opción: "))

    # OPCIÓN 1

    if opcion == 1:
        print("\nPRODUCTOS DISPONIBLES")
        print("-------------------------")

        print("Teclado")
        print("Precio:", precio_teclado, "€")
        print("Stock:", stock_teclado)

        print()

        print("Ratón")
        print("Precio:", precio_raton, "€")
        print("Stock:", stock_raton)

        print()

        print("Monitor")
        print("Precio:", precio_monitor, "€")
        print("Stock:", stock_monitor)

    # OPCIÓN 2

    elif opcion == 2:
        producto = input("¿Qué producto desea comprar (teclado, raton o monitor)? ")
        cantidad = int(input("¿Cuántas unidades desea comprar? "))
        if producto == "teclado":
            if cantidad <= stock_teclado:
                stock_teclado = stock_teclado - cantidad
                vendidos_teclado = vendidos_teclado + cantidad
                productos_vendidos = productos_vendidos + cantidad
                precio_venta = cantidad * precio_teclado
                dinero_total = dinero_total + precio_venta

                print("Venta realizada correctamente.")
                print("Total venta:", precio_venta, "€")
            else:
                print("No hay stock suficiente.")
        elif producto == "raton":
            if cantidad <= stock_raton:
                stock_raton = stock_raton - cantidad
                vendidos_raton = vendidos_raton + cantidad
                productos_vendidos = productos_vendidos + cantidad
                precio_venta = cantidad * precio_raton
                dinero_total = dinero_total + precio_venta

                print("Venta realizada correctamente.")
                print("Total venta:", precio_venta, "€")
            else:
                print("No hay stock suficiente.")
        elif producto == "monitor":
            if cantidad <= stock_monitor:
                stock_monitor = stock_monitor - cantidad
                vendidos_monitor = vendidos_monitor + cantidad
                productos_vendidos = productos_vendidos + cantidad
                precio_venta = cantidad * precio_monitor
                dinero_total = dinero_total + precio_venta

                print("Venta realizada correctamente.")
                print("Total venta:", precio_venta, "€")
            else:
                print("No hay stock suficiente.")
        else:
            print("Producto inexistente.")

    # OPCIÓN 3

    elif opcion == 3:
        cantidad_productos = int(input("¿A cuántos productos desea añadir stock? "))
        for i in range(cantidad_productos):
            producto = input("Producto: ")
            cantidad = int(input("Cantidad a añadir: "))
            if cantidad > 0:
                if producto == "teclado":
                    stock_teclado = stock_teclado + cantidad
                elif producto == "raton":
                    stock_raton = stock_raton + cantidad
                elif producto == "monitor":
                    stock_monitor = stock_monitor + cantidad
                else:
                    print("Producto inexistente.")
            else:
                print("La cantidad debe ser positiva.")
    # OPCIÓN 4

    elif opcion == 4:
        precio_venta = float(input("Introduce el precio de la venta: "))
        descuento = float(input("Introduce el porcentaje de descuento: "))
        if descuento >= 0 and descuento <= 100:
            precio_final = precio_venta - (precio_venta * descuento / 100)
            print("Precio final de la venta:", precio_final, "€")
        else:
            print("ERROR. El descuento no es válido.")

    # OPCIÓN 5

    elif opcion == 5:
        print("\nRESUMEN DE VENTAS")
        print("----------------------")

        print("Dinero total ganado:", dinero_total, "€")
        print("Productos vendidos:", productos_vendidos)

        if vendidos_teclado >= vendidos_raton and vendidos_teclado >= vendidos_monitor:
            print("Producto más vendido: Teclado")
        elif vendidos_raton >= vendidos_teclado and vendidos_raton >= vendidos_monitor:
            print("Producto más vendido: Ratón")
        else:
            print("Producto más vendido: Monitor")

        if vendidos_teclado <= vendidos_raton and vendidos_teclado <= vendidos_monitor:
            print("Producto menos vendido: Teclado")
        elif vendidos_raton <= vendidos_teclado and vendidos_raton <= vendidos_monitor:
            print("Producto menos vendido: Ratón")
        else:
            print("Producto menos vendido: Monitor")


        print("\nSTOCK RESTANTE")

        print("Teclados:", stock_teclado)
        print("Ratones:", stock_raton)
        print("Monitores:", stock_monitor)

    # OPCIÓN 6

    elif opcion == 6:
        print("\nPROGRAMA FINALIZADO")
        print("----------------------")

        print("Dinero total ganado:", dinero_total, "€")
        print("Productos vendidos:", productos_vendidos)

        print("Stock final")

        print("Teclados:", stock_teclado)
        print("Ratones:", stock_raton)
        print("Monitores:", stock_monitor)
    else:
        print("Opción no válida.")