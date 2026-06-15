# lista= [8,20,12,87,1024]
# ##      0 1  2  3  4 

# print(lista)
# print(lista [4])

# for elemento in lista:
#     print("numero:" ,elemento)

# listafr= ["manzana","pera","uva", "Fritilla"]

# print (listafr[1])

# vocales=("aeiouAEIOU")
# for frutas in listafr:
#     print("numero: ", frutas)
#     if frutas[0] in vocales:
#         print(f"La fruta {frutas} comeinza con vocal")
#     else: print(f"La fruta {frutas} no comienza con vocal")

# nombres=["Jose Miguel", "Arturo", "albert"]
# apellido=["Carrera","prat","einstein",]

# print("Nombre y Apellido",nombres [0], apellido[0])

# for n in range (len(nombres)): #el len es para que lo lea y calcule la cantidad
#     print(nombres[n]), apellido[n]

# # las listas pueden tener tipo de datos dispares

# datos=[4, 6.9,"Alonsonic", False] # lista vacia datos []...

# for d in datos:
#     print(d)

## Lista variada

# matrix=[
#     [5,8,3], [74,"sol",34,24]
# ]
# print(matrix)
# print(matrix[1])
# print(matrix[1][1])

# milista.sort() refleja la lista frente a un espejo
# milista.reverse() cambia de poscision la lista

## DICCIONARIO

#uso y explicacion de diccionario

# alumn={
#     "nombre":"tomas",
#     "edad ": 12,
#     "carrera": "piloto",
# }

# print(alumn) # Se imprime el diccionario entero {}

# # for val in alumn:
# #     print(val) # muestra solo el KEY(izq) no el VALUE(der)

# # for key, val in alumn.items():
# #     print(key, val) #muestra solo el KEY(izq) no el VALUE(der)
# # for key, val in alumn.items():
# #     print(key, val) #muestra solo el KEY(izq) no el VALUE(der)
# for key, val in alumn.items():
#     print(f"{key} = {val}")

# print("---Cambios de datos---")

# alumn=["email"]=""
# alumn=["carrera"]=""

# prod={
#     1:{"name": "joystick",
#        "categoria": "electronico",
#        "precio": 4500},
#     2:{"name": "cargador",
#        "categoria": "electrodomestico",
#        "precio": 5000},
#     3:{"name": "cocina 4 platos",
#        "categoria": "electrodomestico",
#        "precio": 70000}
# }
# print(prod [1]["name"]) # Lista de diccionario
# prod=[
#     {"name": "joystick",
#        "categoria": "electronico",
#        "precio": 4500},
#     {"name": "cargador",
#        "categoria": "electrodomestico",
#        "precio": 5000},
#     {"name": "cocina 4 platos",
#        "categoria": "electrodomestico",
#        "precio": 70000}
# ]
# print(prod [1]["name"])

'''
Tarea:
Modificar el programa del carrito de compras
para poder utilizarlo con listas
El producto debe tener nombre y precio
'''
productos=[] == True
while True:
    print("1.- Agregar producto")
    print("2.- Mostrar producto")
    print("3.- Eliminar  producto")
    print("4.- Actualizar producto")
    print("5.- Salir del programa")
    op=int(input("Seleccion una opcion " ))
    match op:
        case 1:
            nombre=input("Ingrese el nombre del producto ")
            precio=int(input("Ingrese el precio del producto "))
            nuevo_prod={
                "nombre": nombre,
                "precio": precio
            }
            productos.append(nuevo_prod)
        case 2:
            if len (productos==0):
                print("No hay... ")
            else:
                print("si hay xd")
                total=0
                for i, nuevo_prod in enumerate (productos, 0):
                    print(f"{i}. {nombre['nombre']} - ${precio['precio']:.2f}")
                    
        case 3:
            print()
        case 4:
            print()
        case 5: 
            print("Salir")