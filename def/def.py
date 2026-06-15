
# sin argumento y sin retorno
def saludo():
    print("Hola que tal?")
saludo()

#sin argumento y con retorno
def suma():
    num1 = 3
    num2 = 5
    return(num1 + num2)
print(suma()) 
# # def esMayor():
# #     edad=18
# #     if edad>=18:
# #         return True
# #     else:
# #         return False



# # print(esMayor())

# #Con  argumento y sin retorno

# def saludaMe(name):
#     print("Hola", name)


# # saludaMe("Yoshy")

# def calculaIVA(neto):
#     print(f"El precio con IVA es {neto*1.19}")
    
# # calculaIVA(4000)

# #Con  argumento y con retorno
# def sumaCA(n1,n2):
#     return(n1 + n2)

# def calculaIVAca(neto):
#     return neto*1.19


# # print("El resultado es:",sumaCA(7, 10))
# # print("El total con IVA es: ", calculaIVAca(30000))


# # v=int(input("Ingrese el valor neto: "))

# # print("El total con IVA es: ", calculaIVAca(v))


# def calculaDescuento(valor, desc):
#     return valor -(valor*desc/100)
# datos=[29500, 22]
# # print("El valor con descuento es", calculaDescuento(*datos))


# # nombre=input("Ingresa tus numeros:")
# # nom=nombre.split()
# # print(nom)

# # Solucion Actividad 3.3.3

# # def paresIMpares():
# #     numeros = input("Ingresa una lista de numeros para saber cuales " \
# #     "son pares y cuales son impares. Separelos por espacios:")
# #     listanum = numeros.split()
# #     for a in range(len(listanum)):
# #         listanum[a] = int(listanum[a])
# #     pares = []
# #     impares = []

# #     for i in listanum:
# #         if i % 2 == 0:
# #             pares.append(i)
# #         else:
# #             impares.append(i)

# #     print("Los nueros pares son:",pares)
# #     print("Los numeros impares son:",impares)

# # # Cree una funcion para pedir notas
# # # y ponerlas en el argumento 
# # # para sacr el promedio

# # cNotas=int(input("Ingrese la cantidad de notas: "))
# # notas=[]
# # for n in range(cNotas):
# #     nota=int(input(f"Ingrese la nota {n+1}: "))
# #     notas.append(nota)

# # def calcularProm(no):
# #     return sum(no)/len(no)

# # print("El promedio es ",calcularProm(notas), notas )


# # Crear una funcion para poder 
# # validar si un input es numero

# nota=input("Ingresa la nota").isdigit()


# if nota:
#     print(" si es numero")
# else:
#     print(" No  es numero")


def suma(a, b):
    return a + b
print(suma(a=4, b= 5
))