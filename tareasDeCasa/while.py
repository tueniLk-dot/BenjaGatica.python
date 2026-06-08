# Ejercicio 1: Imprimir los números del 1 al 10 utilizando un bucle while
# i = 1
# while i <= 10:
#     print(i)
#     i += 1

# ejercicio 2: Sumar los números del 1 al 10 utilizando un bucle while

# Pide números al usuario y suma solo los positivos.
# El programa termina cuando el usuario ingresa 0.
# Muestra la suma total.

# n1 = int(input("ingrese primer numero para la suma: "))
# n2 = int(input("ingrese segundo numero para la suma: "))

# while n1 + n2:
#     if n1 < 0 and n2 < 0:
#         print("no se pueden sumar numeros negativos")
#     else: print(f"el resultado es: {n1 + n2} ")
#     break
suma = 0
# while True:
#     num = int(input("Ingresa un número (0 para terminar): "))
#     if num == 0:
#         break
#     if num > 0:
#         suma += num
# print(f"Suma total: {suma}")

# ejercicio 3: 
# Genera un número aleatorio entre 1 y 20.
# El usuario tiene 5 intentos para adivinarlo.
# Pista: usa random.randint(1, 20)
# import random

# intentos= 5
# numero_aleatorio = random.randint(1, 20)

# while intentos > 0:
#     adivinanza = int(input("Adivina el número entre 1 y 20: "))
#     if adivinanza == numero_aleatorio:
#         print("¡Felicidades! Has adivinado el número.")
#         break
#     elif adivinanza < numero_aleatorio:
#         print("El número es mayor.")
#         print(f"Te quedan {intentos - 1} intentos.")
#     else:
#         print("El número es menor.")
#         print(f"Te quedan {intentos - 1} intentos.")
#     intentos -= 1