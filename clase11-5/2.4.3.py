# Deberás construir un programa que esta diseñado para ayudar en la venta
# de pasajes. Inicia preguntándote cuántos pasajes deseas vender. Luego,
# utiliza un proceso organizado (llamado bucle for) para pedirte el precio de
# cada pasaje por separado. Si ingresas un valor que no es un número, te
# indica que necesitas proporcionar un valor numérico válido. Al final, muestra
# el monto total que se ha obtenido por la venta de todos los pasajes
# • Solicita al usuario la cantidad de pasajes a vender.
# • Se utiliza un bucle for para iterar sobre la cantidad de pasajes.
# • Dentro del bucle, se solicita al usuario el precio de cada pasaje y se
# acumula en la variable totalIngresos.
# • Si el usuario ingresa un valor no numérico para el precio del pasaje,
# el programa muestra un mensaje y sale del bucle usando break.
# • Finalmente, se imprime el total de ingresos por la venta de pasajes

# Programa para la gestión de venta de pasajes

# 1. Solicitar la cantidad de pasajes a vender
try:
    cantidad_pasajes = int(input("¿Cuántos pasajes deseas vender?: "))
    total_ingresos = 0.0

    # 2. Utilizar un bucle for para iterar sobre la cantidad
    for i in range(cantidad_pasajes):
        # Pedimos el precio de cada pasaje (usamos i + 1 para que sea legible)
        precio_input = input(f"Ingrese el precio del pasaje {i + 1}: ")

        # 3. Validar si el ingreso es un número
        # Intentamos convertir a float para permitir decimales
        try:
            precio = float(precio_input)
            total_ingresos += precio
        except ValueError:
            # 4. Si no es un número, mostrar mensaje y salir del bucle
            print("Error: Necesitas proporcionar un valor numérico válido.")
            
    else:
        # Este bloque se ejecuta solo si el bucle terminó normalmente (sin break)
        # 5. Mostrar el monto total obtenido
        print("-" * 30)
        print(f"Venta finalizada exitosamente.")
        print(f"Monto total de ingresos: ${total_ingresos:.2f}")

except ValueError:
    print("Error: La cantidad de pasajes debe ser un número entero.")