# while True:
#     try:   
#         num=input("ingresa tu edad ")
#         break
#     except:
#         print("Solo se aceptan numeros enteros ")
# for i in range(10):
#     n1=int(input("ingresa un numero: "))
#     if n1%2!=0: # % es el resto de la definicion
#         break


# ingrese numeors indefinidamente 
# y sumelos hasta que ponga el numero 0.
# sumelos y muestre el total 
# num=0
# while True:
#     try:
#         n1=int(input("Ingrese un numero para la suma: "))
#         num+=n1
#         if n1==0:
#             break
#     except:
#         print("Soolo numeros enteros: ")
# print("el total es: ", num)

# casa=0
# while True:
#     try:
#         depa=int(input("Ingrese piso del dpto: "))
#         casa+=depa
#         if depa>=3 or depa < 6:
#             print("No esta disponibles ")
#             break
#     except:
            
#             print("Solo departamentos sobre el nivel 3 hasta el piso 6 ")
# print("El departamento seleccionado es: ",depa)

toon1=input("Ingrese el toon 1: ")
toon2=input("Ingrese el toon 2: ")

v1=0
v2=0
while True:
    try:
        cant=int(input("Cauntos votantes son? "))
        break
    except:
        print( " Solo puede ingresar valores enteros positivos")
while cant>0:
    # pedir votos
    while True:
        try:
            voto=int(input(f"Por quien votará? 1.- {toon1} 2.- {toon2}: "))
            break
        except ValueError as r:
            print( " Solo puede ingresar valores enteros positivos")
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("Voto nulo")
    cant-=1

if v1>v2:
    print(f"Gano {toon1} con {v1} votos")
elif v2>v1:
    print(f"Gano {toon2} con {v2} votos")
else:
    print("Fue un empate")
    
    # Preguntar el codigo de descuento de una entrada a un concierto
# validar que los folios esten entre 7.000 y 21.000
# Preguntar si esa en cancha vip, cancha general, o tribuna
# Cada entrada vale 40000, pero los impuestos son
# vip * 1.8, genral, 1.4, y tibuna 1.2
# Mostrar el valor a pagar al final 
# poner manejo de error ára poder solucionarlo