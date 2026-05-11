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

casa=0
while True:
    try:
        depa=int(input("Ingrese piso del dpto: "))
        casa+=depa
        if depa>=3 or depa < 6:
            print("No esta disponibles ")
            break
    except:
            
            print("Solo departamentos sobre el nivel 3 hasta el piso 6 ")
print("El departamento seleccionado es: ",depa)