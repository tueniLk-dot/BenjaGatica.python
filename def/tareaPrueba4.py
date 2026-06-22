# # Funcion sin argumento y sin return
# def suma():
#     n1=("ingresa un numero ")
#     n2=("ingresa otro numero ")
#     print(n1+n2)
# # con argumento y sin return
# def suma_arg(n1,n2):
#     print(n1+n2)
# # sin argumento y con return
# def suma_ret():
#     n1= int(input("Ingrese un numero"))
#     n2= int(input("Ingrese otro numero"))
#     return n1+n2
# # con argumento con return
# def sumass(n1,n2):
#     return n1 + n2 

# product={
#     1:{"nombre" : "agua con gas 500cc", "precio": 1000},
#     2:{"nombre" : "CocaCola en lata 374cc", "precio": 1000},
#     3:{"nombre" : "Kilogramo de pan", "precio": 1000},
    
# }
# print(product[3])

# # perros de caza

# perros= { #Diccionario de diccionario 
#     1: {"nombre ": "Doppy", 
#         "Raza" : "Doghount",
#         "Codigo" : "Dphh06"}
# }

# while True:
#     try:
#         print('''
#             1.- Resgistrar un perro
#             2.- Mostrar perros
#             3.- Salir ''')
#         op= int(input("seleccione una opcion "))
#         match op:
#             case 1:
#                 nombre=input("ingrese un nombre: ")
#                 raza=input("Ingrese la raza: ")
#                 code=input("ingrese su codigo: ")
#                 perros [2]={1: {"nombre ": nombre, 
#                                 "Raza" : raza,
#                                 "Codigo" : code}}
#             case 2:
#                 print(perros)
#             case 3:
#                 print("Saliendo")
#                 break
#             case _:
#                 print("Opcion invalida")
#     except Exception as e:
#         print("El error es: ",e)
# # ❌
''' lista[], con diccionario{} dentro'''
# personajes= [
#     {"name": "Arturo Prat", "edad" : 93},
#     {"name": "Cristobal Colon", "edad" : 99},
#     {"name": "Benjamin Gatica", "edad" : 23},
# ]
# print(f"{personajes[0]['name']} - bajo la edad de {personajes[1]['edad']} años")
# personajes= {
#     "VideoJuegos Shooter: ":{
#         "Shooter" : "Warzone", 
#         "Shooter" : "Valorant",
#         "Shooter" : "CS 2",
#     },
#     "VideoJuegos Indie: ":{
#         "indie" : "Hello Knight",
#         "indie" : "Paper Please",
#     }
# }
# personajes = {
#     1: {
#         "name": "Arturo Prat",
#         "edad": 93,
#         "info": {
#             "nacionalidad": "Chileno",
#             "ocupacion":    "Militar"
#         }
#     },
#     2: {
#         "name": "Cristobal Colon",
#         "edad": 99,
#         "info": {
#             "nacionalidad": "Italiano",
#             "ocupacion":    "Navegante"
#         }
#     },
#     3: {
#         "name": "Benjamin Gatica",
#         "edad": 23,
#         "info": {
#             "nacionalidad": "Chileno",
#             "ocupacion":    "Estudiante"
#         }
#     }
# }
## crear un gestor de estacionamiento
# Un estacionamiento tiene 4 pisos
# y cada piso tiene 20 espacios

#  Preguntar cuando entra un vehiculo, que tipo de vheiculo es
# vehículo ligero 2000
# vehículo mediano 3000
# vehículo pesado 3500

# luego , acomodarlo en algun lugar de algun piso disponible.
# el menu dsebe tener las sigueintes alternativas
''' 1.- ingresar vehiculo
2.- contar ganancias
3.- contar vehiculos'''

# usa lista o diccionario segun le acomode mas
parking={
    1:[],
    2:[],
    3:[],
    4:[],
}
maximEsp=80
ganancia=0
def ingresarVehiculo():
    nievoIngreso=int(input('''Ingresa el tipo de tu vehiculo: 
                           1- Ligero=2000
                           2- Mediano=3000
                           3- Largo=3500
                           '''))
    costo=0
    if parking[nievoIngreso-1]=="ligero".lower():
        costo==2000
    elif nievoIngreso=="mediano".lower():
        costo==3000
    elif nievoIngreso=="grande".lower():
        costo==3500
    else: print("Seleccion invalida")
                
def contarGanancias():
    tiposs=int(input("Ingrese el tipo de su veihiculo \n1- ligero = $2000 \n2- mediano = $3000 \n3- grande = $3500 "))  
    if tiposs== "ligero":
        tiposs=2000
    elif tiposs=="mediano":
        tiposs=3000
    elif tiposs=="grande":
        tiposs=3500
    else: print("seleccion invalida")

    print(f"ganancias totales= ${tiposs}" )

def contarVehiculos():
    parking
    contador=0
    for  estacionamientos in parking:
        if estacionamientos<10:
            estacionamientos+=1   
        print(f"Los {contador} ocupados son: {parking}")

    
    
while True:
    try:
        print("Selecciona: ")
        op=int(input('''
                    1.- Ingresar vehiculo 
                    2.- Contar ganancias 
                    3.- Contar vehiculos 
                    0.- Salir
                    '''))
        match op:
            case 1:
                ingresarVehiculo()
            case 2:
                contarGanancias()
            case 3:
                contarVehiculos()
            case 0: 
                print("Salida")
                break
            case _:
                print("Seleccion invalida.")
    except Exception as e:
        print("Error", e)