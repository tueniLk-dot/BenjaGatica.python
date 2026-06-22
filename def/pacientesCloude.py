parking = {
    1: [],
    2: [],
    3: [],
    4: [],
}

MAX_POR_PISO = 20
ganancia = 0

TIPOS = {
    1: ("ligero", 2000),
    2: ("mediano", 3000),
    3: ("grande", 3500),
}


def ingresarVehiculo():
    global ganancia

    # Verificar si hay espacio disponible
    total_vehiculos = sum(len(espacios) for espacios in parking.values())
    if total_vehiculos >= MAX_POR_PISO * len(parking):
        print("El estacionamiento está lleno.")
        return

    print("Ingresa el tipo de tu vehículo:")
    for key, (nombre, precio) in TIPOS.items():
        print(f"  {key}- {nombre.capitalize()} = ${precio}")

    try:
        seleccion = int(input("Selección: "))
    except ValueError:
        print("Entrada inválida.")
        return

    # ❌ Antes: comparabas int con strings como "ligero" → siempre False
    # ✅ Ahora: validas directamente contra las claves del diccionario
    if seleccion not in TIPOS:
        print("Selección inválida.")
        return

    nombre_tipo, costo = TIPOS[seleccion]  # ❌ Antes: costo == 2000 (comparación, no asignación)

    # Buscar piso con espacio disponible
    piso_asignado = None
    for piso, espacios in parking.items():
        if len(espacios) < MAX_POR_PISO:
            piso_asignado = piso
            break

    if piso_asignado is None:
        print("No hay espacio disponible.")
        return

    # ❌ Antes: nunca se agregaba el vehículo al diccionario
    parking[piso_asignado].append(nombre_tipo)
    ganancia += costo  # ❌ Antes: ganancia nunca se actualizaba

    print(f"Vehículo '{nombre_tipo}' ingresado en el piso {piso_asignado}. Costo: ${costo}")


def contarGanancias():
    # ❌ Antes: pedía tipo de vehículo de nuevo y no usaba la variable global ganancia
    print(f"Ganancias totales: ${ganancia}")


def contarVehiculos():
    # ❌ Antes: iteraba claves pero el contador nunca contaba correctamente
    total = 0
    for piso, espacios in parking.items():
        cantidad = len(espacios)
        total += cantidad
        print(f"  Piso {piso}: {cantidad} vehículo(s) → {espacios}")
    print(f"Total de vehículos: {total}")


while True:
    try:
        print("\n--- MENÚ ---")
        op = int(input("1- Ingresar vehículo\n2- Contar ganancias\n3- Contar vehículos\n0- Salir\nSelección: "))

        match op:
            case 1:
                ingresarVehiculo()
            case 2:
                contarGanancias()
            case 3:
                contarVehiculos()
            case 0:
                print("Salida.")
                break
            case _:
                print("Selección inválida.")
    except ValueError:
        # ❌ Antes: Exception genérico ocultaba todos los errores
        print("Por favor ingresa un número válido.")