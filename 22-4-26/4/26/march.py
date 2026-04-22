print("1. opcion 1")
print("2. opcion 2")
print("3. opcion 3")
print('seleccione una opcion')
op=int(input())
match op:
    case 1:
        print('Ha seleccionado la opcion 1')
    case 2:
        print('Ha seleccionado la opcion 2')
    case 3:
        print('Ha seleccionado la opcion 3')
    case _:
        print("opcion invalida")
op=0
total=0
while op!=4:
    print("1. Radio stereo $70.000")
    print("2. LGTV 55 pulgadas $500.000")
    print("3. PS5 $600.000")
    print("4. para salir")
    print('seleccione una opcion')
    op=int(input())
    match op:
        case 1:
            print('Ha seleccionado la opcion 1', 70000*1.19)
            total+=70000*1.19
        case 2:
            print('Ha seleccionado la opcion 2', 500000*1,19)
            total+=500000*1.19
        case 3:
            print('Ha seleccionado la opcion 3', 600000*1.19)
            total+=600000*1.19
        case 4 :
            print("salir")
        case _:
            print("opcion invalida")
op=0
opi=int(input('ingresa una operacion'))

while op!= 10:
    print

