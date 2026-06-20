# dicci={
#     "nombre": "miguel",
#     "edad": 64,
#     "nacionalidad": "chilena"
# }


# print(dicci)
# print(dicci["nombre"])


# dicci["Email"]="pino@gmail.com"
# dicci["nacionalidad"]="peruana"
# del dicci["edad"]
# print(dicci)
# '''
# Crear un crud con diccionarios
# referido a agregar vegetaes al canasto
# enseñar los productos en stock
# actualizar el carro y eliminar productos.'''
# canasto={}
# def vegetalesMenu():
#     while True:
#         try:
#             print('''
#                   1.- Agregar vegetales
#                   2.- Mostrar vegetales
#                   3.- Actualizar vegetales
#                   4.- Eliminar vegetal
#                   5.- salir''')
#             op=int(input("Selecciona una opcion: "))
#             match op:
#                 case 1:
#                     for clave, valor in canasto.items():
#                         print(f"{clave}: {valor}")
#                 case 2:
#                     print
#                 case 3:
#                     print
#                 case 4:
#                     print
#                 case 5:
#                     print("Salida")
#                     break
#                 case _:
#                     print("Seleccion invalida, reintente")
#         except Exception as e:
#             print("Seleccion incorrecta, reintente")

def saludaMe(name):
    print("Hola", name)
saludaMe(input("Ingresa tu nombre "))
def edad(años):
    print("tienes: ", años, "años de edad")
edad(input("Ingresa tu edad: "))