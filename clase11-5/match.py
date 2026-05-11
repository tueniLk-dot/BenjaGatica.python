#ejemplo y ecplicacion de match
# op=0
# total=0 # acumulador de valores
# cantProd=0 # contador de valores por uno
# while op!=4:
#     try:
#         print("1.- Radio sterero Sony $70.000")
#         print("2.- LGTV 55 pulgadas Super gamer $500.000 ")
#         print("3.- PS5 $580.000")
#         print("4.- Salir")
#         print("Seleccione una opcion")
#         op=int(input())
#         match op:
#             case 1:
#                 print("El precio a pagar es ", 70000*1.19)
#                 total+=70000*1.19
#                 cantProd+=1
#             case 2:
#                 print("El precio a pagar es ", 500000*1.19)
#                 total+=500000*1.19
#                 cantProd+=1
#             case 3:
#                 print("El precio a pagar es ", 580000*1.19)
#                 total+=580000*1.19
#                 cantProd+=1
#             case 4:
#                 print(f"Su total a pagar es {total}")
#                 print(f"la cantidad de productos comprados es: {cantProd}")
#             case _:
#                 print("Opcion Inválida")  # opcion por defecto
                
#     except:
#         print("Debe ingresar solo numeros enteros")

        ## un porcentaje % no puede ser ni pos
        # itvio ni negativo
        ## si puede estar entre 0 y 100

porc=int(input("ingresa el procentae de rucos en su comuna "))
if porc >0 and porc < 100:
    print("porcentaje correcto")
else: 
    print("porcentaje fuera de rango")





# name="Carlos"
# def saludo():
#     print("Hola como van?")
# def chao():
#     print(f"YA nos vamos? { name}")

# def suma():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1+n2}")
# def resta():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1-n2}")
# def multi():
#     n1=int(input("Ingrese un numero: "))
#     n2=int(input("Ingrese otro numero: "))
#     print(f"El resultado es {n1*n2}")
# def divi():
    n1=int(input("Ingrese un numero: "))
    n2=int(input("Ingrese otro numero: "))
    print(f"El resultado es {n1/n2}")


# def 

# op=0
# while op!=5:
#     # 3
#     op=int(input('''Ingrese una operacion  
#                         1.-Suma
#                         2.-Resta
#                         3.-Mutltiplicacion
#                         4.-Division
#                         5.-Salir
#                         '''))
#     match op:
#         case 1:
#             suma()
#         case 2:
#             resta()
#         case 3:
#             multi()
#         case 4:
#             divi()
#         case 5:
#             print("Saliendo del programa")
#         case _:
#             print("Opción Inválida")
    
# op=0
# cantPersonas=0 #contar la cant de personas que ingresan al zoo
# total=0 # total a pagar por las entradas
# while op!=4:
#     print('''
#         1.- Niño (1-17) 1000
#         2.- Adulto (18-64) 3000
#         3.- Adulto Mayor (64 o mas) 1500
#         4.- Salir''')
#     op=int (input("Seleccione una opcion"))
#     match op:
#         case 1:
#             #Preguntar cuantos son en cada persona
#             print("Pagando el precio de niño: ")
#             cantN=int(input("ingrese cuantos niños son"))
#             # limitar la cant de personas de 1 a 10
#             while cantN<1 or cantN>10:
#                 print("EL numero esta fuera de rango (1-10)")
#                 cantN=int(input("ingrese cuantos niños son: "))
#             cantPersonas+=cantN
#             total+=1000*cantN
#         case 2:
#             print("Pagando el precio de adulto")
#             cantN=int(input("ingrese cuantos adulto son"))
#             cantPersonas+=cantN
#             total+=3000*cantN
#         case 3:
#             print("Pagando el precio de Viejito")
#             cantN=int(input("ingrese cuantos ancianos son"))
#             cantPersonas+=cantN
#             total+=1500*cantN
#         case 4:
#             print("Saliendo del programa")
#             print(f"EL total a pagar es {total}")
#             print(f"LA cantidad de personas son {cantPersonas}")
#         case _:
#             print("Opción Inválida")



# Preguntar el folio de una entrada a un concierto
# validar que los folios esten entre 7.000 y 21.000
# Preguntar si esa en cancha vip, cancha general, o tribuna
# Cada entrada vale 40000, pero los impuestos son
# vip * 1.8, genral, 1.4, y tibuna 1.2
# Mostrar el valor a pagar al final 

# folio=int(input("Ingese su folio: "))
# while folio<7000 or folio>21000:
#     print("Folio fuera de rango")
#     folio=int(input("Ingese su folio: "))

# cancha=int(input('''Cual cancha es?
# 1.- VIP
# 2.- General
# 3.- Tribuna'''))

# match cancha:
#     case 1:
#         print(f"Su total a pagar es {40000*1.8}")
#     case 2:
#         print(f"Su total a pagar es {40000*1.4}")
#     case 3:
#         print(f"Su total a pagar es {40000*1.2}")
#     case _:
#         print("Opcion invalida")