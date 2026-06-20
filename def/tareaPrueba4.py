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
    1:["ab1234", "ggwn13",],
    2:["Ke2324"],
    3:[],
    4:[],
}
maximEsp=80
ganancia=0
def ingresarVehiculo():
    global ganancia
    patente= input('''Ingrese la PATENTE de su vehiculo''')
                        
    tiposs=input("Ingrese el tipo de su veihiculo \n1- ligero = $2000 \n2- mediano = $3000 \n3- grande = $3500 ")  
    
    match tiposs:
        case 1:
            precio=2000
            tiposs=print(f"Tu vehiculo es tipo: {precio}")
        case 2:
            precio=3000
            tiposs=print(f"Tu vehiculo es tipo: {precio}")
        case 3:
            precio=3500
            tiposs=print(f"Tu vehiculo es tipo: {precio}")
        case _:
            print("seleccion invalida.")
            # piso con espacio
    piso_disponible = None
    for i in parking(1,20):
        print(i, "x" , i+1 , "=", i*(i+1))
    print(i)

    # for piso, patente in parking.items():
    #     if len(patente) < maximEsp:
    #         piso_disponible = piso
    #         break
 
    if piso_disponible is None:
        print("❌ Estacionamiento lleno. No hay espacios disponibles.")
        return
 
    parking[piso_disponible].append(patente)
    ganancia += precio
    print(f"✅ Vehículo {patente} ({tiposs}) ingresado en el Piso {piso_disponible}.")
    print(f"   Cobro: ${precio}")
    # if patente in tipo==ligero:
    #     tipo=2000
    # elif patente in tipo==mediano:
    #     tipo=3000
    # elif patente in tipo==grance:
    #     tipo=3500
    # else:   
    #     print("Seleccion invalida, reintenta")
    

def contarGanancias():
     
    print(f"ganancias totales= ${ganancia}" )

def contarVehiculos():

    for  estacionamientos in parking[estacionamientos]:    
        print(f"Los {estacionamientos} ocupados son: {parking}")

    
    
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
                print()
            case 0: 
                print("Salida")
                break
            case _:
                print("Seleccion invalida.")
    except Exception as e:
        print("Error", e)