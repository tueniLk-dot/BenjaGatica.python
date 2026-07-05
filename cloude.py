
"""
Solución - Guía de Ejercicios: Sistema de Gestión de Automotora
================================================================
Se trabaja con dos diccionarios relacionados por el mismo ID de vehículo:
 
autos       -> { id_auto: [marca, modelo, año, ranking] }
operaciones -> { id_auto: [fecha_ingreso, fecha_venta] }  (fecha_venta = "Pendiente" si no se ha vendido)
 
Todas las acciones están programadas dentro de funciones, y el programa
principal arma el menú de interacción con el usuario.
"""
 
# --------------------------------------------------------------------
# Datos iniciales (diccionarios preexistentes de ejemplo)
# --------------------------------------------------------------------
autos = {
    "A001": ["Toyota", "Corolla", 2020, 4],
    "A002": ["Chevrolet", "Sail", 2018, 3],
    "A003": ["Toyota", "Yaris", 2022, 5],
    "A004": ["Nissan", "Versa", 2019, 2],
    "A005": ["Chevrolet", "Onix", 2021, 4],
}
 
operaciones = {
    "A001": ["2023-01-10", "2023-03-15"],
    "A002": ["2023-02-05", "Pendiente"],
    "A003": ["2023-04-01", "Pendiente"],
    "A004": ["2022-11-20", "2023-01-05"],
    "A005": ["2023-05-10", "Pendiente"],
}
 
 
# ======================================================================
# EJERCICIO 1: Búsqueda y conteo por marca
# ======================================================================
def autos_vendidos_por_marca(marca):
    """
    Recorre 'autos' buscando coincidencias con la marca indicada
    (sin distinguir mayúsculas/minúsculas). Por cada coincidencia,
    revisa en 'operaciones' si ya fue vendido (fecha_venta != "Pendiente")
    y acumula el total. Muestra el resultado por pantalla (no retorna nada).
    """
    total_vendidos = 0
 
    for id_auto, datos_auto in autos.items():
        marca_auto = datos_auto[0]
        if marca_auto.lower() == marca.lower():
            fecha_venta = operaciones[id_auto][1]
            if fecha_venta != "Pendiente":
                total_vendidos += 1
 
    print(f"Total de vehículos vendidos de la marca '{marca}': {total_vendidos}")
 
 
# ======================================================================
# EJERCICIO 2: Búsqueda de vehículos por rango de año
# ======================================================================
def busqueda_por_anio(anio_min, anio_max):
    """
    Busca vehículos cuyo año esté dentro del rango [anio_min, anio_max]
    y cuya fecha de venta sea "Pendiente" (stock disponible).
    Construye una lista con formato "Marca Modelo--ID", la ordena
    alfabéticamente (marca y modelo) y la muestra por pantalla.
    """
    resultados = []
 
    for id_auto, datos_auto in autos.items():
        marca, modelo, anio, ranking = datos_auto
        fecha_venta = operaciones[id_auto][1]
 
        if anio_min <= anio <= anio_max and fecha_venta == "Pendiente":
            resultados.append(f"{marca} {modelo}--{id_auto}")
 
    if resultados:
        resultados.sort()  # orden alfabético por "Marca Modelo..."
        print(f"Vehículos disponibles entre {anio_min} y {anio_max}:")
        for item in resultados:
            print(f"  - {item}")
    else:
        print(f"No existen vehículos disponibles entre {anio_min} y {anio_max}.")
 
 
# ======================================================================
# EJERCICIO 3: Actualizar el estado de venta
# ======================================================================
def actualizar_fecha_venta(id_auto, nueva_fecha):
    """
    Verifica si id_auto existe en 'operaciones'. Si existe, actualiza
    la fecha de venta y retorna True. Si no existe, retorna False.
    """
    if id_auto in operaciones:
        operaciones[id_auto][1] = nueva_fecha
        return True
    else:
        return False
 
 
# ======================================================================
# EJERCICIO 4: Incorporar un nuevo vehículo al catálogo
# ======================================================================
def validar_id(id_auto):
    return isinstance(id_auto, str) and id_auto.strip() != "" and id_auto not in autos
 
 
def validar_texto(texto):
    return isinstance(texto, str) and texto.strip() != ""
 
 
def validar_anio(anio):
    return isinstance(anio, int) and anio > 1900
 
 
def validar_ranking(ranking):
    return isinstance(ranking, int) and 1 <= ranking <= 5
 
 
def validar_fecha_ingreso(fecha):
    return isinstance(fecha, str) and fecha.strip() != ""
 
 
def validar_fecha_venta(fecha):
    # Puede ser "Pendiente" o una fecha en texto, pero no vacía
    return isinstance(fecha, str) and fecha.strip() != ""
 
 
def agregar_auto(id_auto, marca, modelo, anio, ranking, fecha_ingreso, fecha_venta):
    """
    Valida cada campo de forma independiente. Si alguno falla, alerta
    del error y aborta el registro. Si todo es correcto y el ID no
    existe previamente, agrega el vehículo a ambos diccionarios.
    """
    if not validar_id(id_auto):
        print("Error: el ID no es válido o ya se encuentra registrado.")
        return False
 
    if not validar_texto(marca):
        print("Error: la marca no puede estar vacía.")
        return False
 
    if not validar_texto(modelo):
        print("Error: el modelo no puede estar vacío.")
        return False
 
    if not validar_anio(anio):
        print("Error: el año debe ser un entero mayor a 1900.")
        return False
 
    if not validar_ranking(ranking):
        print("Error: el ranking debe ser un entero entre 1 y 5.")
        return False
 
    if not validar_fecha_ingreso(fecha_ingreso):
        print("Error: la fecha de ingreso no puede estar vacía.")
        return False
 
    if not validar_fecha_venta(fecha_venta):
        print("Error: la fecha de venta no puede estar vacía.")
        return False
 
    # Todas las validaciones pasaron: se registra en ambos diccionarios
    autos[id_auto] = [marca, modelo, anio, ranking]
    operaciones[id_auto] = [fecha_ingreso, fecha_venta]
    print(f"Vehículo '{id_auto}' agregado correctamente.")
    return True
 
 
# ======================================================================
# EJERCICIO 5: Dar de baja un automóvil del sistema
# ======================================================================
def eliminar_auto(id_auto):
    """
    Comprueba si el ID existe en el sistema. Si existe, elimina la
    clave y sus valores en ambos diccionarios y retorna True.
    Si no existe, retorna False.
    """
    if id_auto in autos and id_auto in operaciones:
        del autos[id_auto]
        del operaciones[id_auto]
        return True
    else:
        return False
 
 
# ======================================================================
# PROGRAMA PRINCIPAL (menú de interacción)
# ======================================================================
def menu_ejercicio_1():
    marca = input("Ingrese la marca a consultar: ")
    autos_vendidos_por_marca(marca)
 
 
def menu_ejercicio_2():
    # Manejo de excepciones para garantizar años enteros
    while True:
        try:
            anio_min = int(input("Ingrese año mínimo: "))
            anio_max = int(input("Ingrese año máximo: "))
            break
        except ValueError:
            print("Error: debe ingresar números enteros. Intente nuevamente.")
 
    busqueda_por_anio(anio_min, anio_max)
 
 
def menu_ejercicio_3():
    continuar = "s"
    while continuar.lower() == "s":
        id_auto = input("Ingrese el ID del vehículo a actualizar: ")
        nueva_fecha = input("Ingrese la nueva fecha de venta: ")
 
        if actualizar_fecha_venta(id_auto, nueva_fecha):
            print("Fecha de venta actualizada con éxito.")
        else:
            print("Error: el identificador no existe.")
 
        continuar = input("¿Desea actualizar otro vehículo (s/n)? ")
 
 
def menu_ejercicio_4():
    id_auto = input("ID del nuevo vehículo: ")
    marca = input("Marca: ")
    modelo = input("Modelo: ")
 
    try:
        anio = int(input("Año: "))
        ranking = int(input("Ranking (1-5): "))
    except ValueError:
        print("Error: año y ranking deben ser números enteros.")
        return
 
    fecha_ingreso = input("Fecha de ingreso: ")
    fecha_venta = input("Fecha de venta (o 'Pendiente'): ")
 
    agregar_auto(id_auto, marca, modelo, anio, ranking, fecha_ingreso, fecha_venta)
 
 
def menu_ejercicio_5():
    id_auto = input("Ingrese el ID del vehículo a eliminar: ")
    if eliminar_auto(id_auto):
        print(f"Vehículo '{id_auto}' eliminado correctamente.")
    else:
        print("Error: el identificador no fue encontrado.")
 
 
def menu_principal():
    opciones = {
        "1": menu_ejercicio_1,
        "2": menu_ejercicio_2,
        "3": menu_ejercicio_3,
        "4": menu_ejercicio_4,
        "5": menu_ejercicio_5,
    }
 
    while True:
        print("\n===== MENÚ AUTOMOTORA =====")
        print("1. Contar autos vendidos por marca")
        print("2. Buscar autos disponibles por rango de año")
        print("3. Actualizar fecha de venta")
        print("4. Agregar nuevo vehículo")
        print("5. Eliminar vehículo")
        print("0. Salir")
 
        opcion = input("Seleccione una opción: ")
 
        if opcion == "0":
            print("Saliendo del sistema...")
            break
        elif opcion in opciones:
            opciones[opcion]()
        else:
            print("Opción inválida, intente nuevamente.")
 
 
if __name__ == "__main__":
    menu_principal()