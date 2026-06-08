op=0
total=0 #valor total a pagar
cantG=0 #cantidad de gaseosas
while op != 4:
    print("1. Entrada niños")
    print("2. Entrada adultos")
    print("3. Entrada tercera edad")
    print("4. Salir")
    op = int(input("Seleccione una opción: "))
match op:
    case 1:
        print("Entrada niños: $2000")
        total += 1000
        cantG += 1
        cantG+=cantG
    case 2:
        print("Entrada adultos: $3000")
        total += 3000
        cantG += 1
    case 3:
        print("Entrada tercera edad: $1500")
        total += 1500
        cantG += 1
    
    case 4:
        print(f"Total a pagar: ${total}" )
        print(f"Cantidad de gente ingresada a la sala de transmicion: {cantG}")
        print("Slida del programa")
    case _:
        print("Opcion no valida")
        