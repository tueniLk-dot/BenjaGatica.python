
# Construir el siguiente programa con las siguiente reglas de negocio:
# • Inicio del Programa:

# o El programa comienza inicializando una variable sw en 1, indicando
# que el sistema está activo, puede utilizar también “while true:”

# • Menú Principal:
#        o Se presenta un menú al usuario con las siguientes opciones:
# ▪ Ver mi Saldo
# ▪ Retirar Dinero
# ▪ Salir

# • Selección de Opción:
#       o Se le pide al usuario que seleccione una opción ingresando un
#       número.

# • Validación de Entrada:
#       o Se verifica que la opción ingresada esté en el rango de 1 a 3.
 
# • Acciones según la Opción:
# • Si la opción es 1:
#        a. Se imprime el mensaje "Tiene un saldo de $500000".
#       b. Se solicita al usuario que presione 1 para volver atrás o 2 para
#   salir.
#       c. Si el usuario presiona 2, se imprime "Cierre de sesión exitoso,
#   adiós" y se sale del sistema.
# • Si la opción es 2:
#       a. Se imprime "Transferencia realizada".
#       b. Se solicita al usuario que presione 1 para volver atrás o 2 para
#   salir.
#       c. Si el usuario presiona 2, se imprime "Cierre de sesión exitoso,
#   adiós" y se sale del sistema.
# • Si la opción es 3:
#       a. Se imprime "Cierre de sesión exitoso, adiós".

# domingo de pascua 
# preguntar la cantidad de niños q buscam huevitos de chocolate
# tonces e cuando se termine la busquead los niños , preguntar cuantos huevitos encontraron cada uno
# y clasificarlo de la sgte forma
# - menos de 12 noob
# - entre 12 y 24 es master
# - entre 25 o mas es legend

# mostrar resumen y mostrar la mayor cantidad guardada por un niño


# --------------------------------------------------
# El programa debe tener un menú de opciones de donde se pueda realizar el pago
# del cupo de la tarjeta de crédito, como también simular nuevas compras, y estas
# una vez sumadas se resten al cupo disponible.

# Las opciones disponibles deben estar construidas de la siguiente forma:

# 1. Pago de Tarjeta de Crédito:
#   a. El usuario comienza con una deuda de $100.000
#   b. El usuario puede ingresar un monto para realizar un pago en la
#   tarjeta de crédito.
#   c. Se debe verificar que el monto ingresado sea mayor o igual a cero.
#   d. Se debe verificar que el monto a pagar no exceda el saldo actual de
#   la tarjeta.
#   e. Al pagar el sistema debe descontar de la deuda total
#   f. Si las verificaciones son exitosas, se realiza el pago y se actualiza el
#   saldo de la tarjeta.
# 
# 2. Simulación de Compras:
#   a. El usuario puede simular realizar un número ilimitado de compras.
#   b. Para cada compra, se solicita al usuario ingresar el monto de la
#   compra. El programa suma los montos de cada compra.
#   c. Se verifica que el monto de la compra sea mayor o igual a cero.
#   d. Se realiza la compra y se actualiza el saldo de la tarjeta para cada
#   iteración del bucle for.

# 3. Salir:
#   a. Al seleccionar esta opción, el programa debe cerrarse o finalizar.

# A considerar:
# 1. Manejo de Errores:
#   a. Se utilizan bloques try y except para manejar posibles errores al
#   ingresar datos, validar valores no numéricos y errores inesperados.
#   b. Se debe programar mensajes de error específicos para guiar al
#   usuario sobre posibles problemas.

deuda=100000
usr=0 
acumulador=0


while True:
    try:
        menu=int(input('''
            Cajero automatico
        Selecciona una opcion
           1- Pago de Tarjeta de Credito
           2- Simulacion de compra
           3- Salir
            
            '''))
        match menu:
            case 1:
                print("Has seleccionado el pago de deuda")
                
                while True:
                    try:
                        menu=int(input('''
                            Cajero automatico
                        Selecciona una opcion
                        1- Pago de deuda
                        2- volver al menu
                            
                            '''))
                        
                        match menu:
                            case 1:
                                monto=int(input("ingresa el monto a pagar:"))
                                if monto >=0 and monto <=100000:
                                    print("el monto ingresado es valido")
                                else: print("el ingreso fue inalcanzable")
                            case 2:
                                print("Vuelta al menu principal.")
                                break
                            case 4: 
                                print("opcion no valida")
                    except ValueError:
                        print ("solo numeros presentados")
            case 2:
                print("has seleccionado la simulacion de compra: ")
                while True:
                    try:
                        menu=int(input('''
                            Cajero automatico
                        Selecciona una opcion
                        1- zapatillas = $ 89.990
                        2- ropa de cama = $ 23.500
                        3- cuadernos = $ 1.200
                        4- telefono = $ 100.000
                        5- Volver al menu principal
                            
                            '''))
                        
                        match menu:
                            
                            case 1:
                                zapatillas =  89.990 * 1.19 
                                print(f"zapatillas = ${zapatillas} ")
                                acumulador+= zapatillas
                            case 2:
                                ropaDecama = 23.500 * 1.19 
                                print(f"ropa de cama = ${ropaDecama}")
                                acumulador+= ropaDecama
                            case 3:
                                cuadernos =  1.200 * 1.19
                                print(f"cuadernos = ${cuadernos}")
                                acumulador+= cuadernos
                            case 4:
                                telefono =  100.000 * 1.19
                                print(f"Telefono = ${telefono}")
                                acumulador+= telefono
                            case 5:
                                print("vuelta al menu principal")
                                break
                            case 6: 
                                print("opcion no valida")
                    except ValueError:
                        print ("solo numeros presentados")
                        
            case 3:
                print("Saliendo del sistema")
                break
            case 4: 
                print("opcion ingresadas no valida")
    except ValueError:
        print ("solo numeros presentados")         