''''Hacer un menu con todas las funciones
que hicismos y usamos en clase,
debe tener manejo de errores o sea
Try- except'''

# pcs = {
#     'PC01' : ['Lenovo','IdeaPad','i5-8794f',"8gb"],
#     'PC02' : ['Hp', 'Pavilion',"i3-6600","4gb"],
#     'PC03' : ['Asus', 'TUF Gaming',"i7-13436klg","8gb"],
#     'PC04' : ['Hp', 'Aerio',"i5-7032","6gb"],
#     'PC05' : ['Lenovo','ThinkPad Serie T',"AMD 5 Pro","12gb"],
#     'PC06' : ['Dell', 'XPS',"AMD 3 4321","4gb"],
# }
# fechaDeVenta = { # "pendiente" significa que no se ha vendido el producto aun
#     'PC01' : ['01-01-2024','12-12-2025'],
#     'PC02' : ['07-08-2024','Pendiente'],
#     'PC03' : ['09-01-2025','Pendiente'],
#     'PC04' : ['24-03-2025','Pendiente'],
#     'PC05' : ['24-03-2024','24-07-2024'],
#     'PC06' : ['24-03-2024','24-09-2024'],
# }
pcs = {
    'C001' : ['Lenovo', 'ThinkPad', 2010, 5],
    'C002' : ['Apple', 'MacBook Air', 2019, 4],
    'C003' : ['ASUS', 'ROG Zephyrus', 2022, 4],
    'C004' : ['HP', 'Pavilion', 2005, 4],
    'C005' : ['Lenovo', 'IdeaPad', 2015, 5],
    'C006' : ['ASUS', 'VivoBook', 1995, 1]
}

operaciones = {
    'C001' : ['01-01-2024', '12-12-2025'],
    'C002' : ['07-08-2024', 'Pendiente'],
    'C003' : ['09-01-2025', 'Pendiente'],
    'C004' : ['24-03-2025', 'Pendiente'],
    'C005' : ['24-03-2024', '24-07-2024'],
    'C006' : ['24-03-2024', '24-09-2024']
}
# 
def mostrarPcs(pcsm):
    for id, model in pcsm.items():
        print(f"{id}:{model}")
# mostrarPcs(pcs)
def computadoras_vendidas_por_marca(marca):
    total=0
    for id_pcs, pc in pcs.items(): #.items() es primordial
        print(f"{ id_pcs }: {pc}")
        if pc[0].lower()==marca.lower():
            if operaciones[id_pcs][-1] != "Pendientes".lower():
                total+=1
    print(f"La cantidad vendida equivale a {total} de la gran marca {marca} ")
def mostrarPcsVendidos():
    vendidos = []

    for id_pc, fechas in operaciones.items():
        fecha_venta = fechas[1]

        if fecha_venta != "Pendiente":
            marca = pcs[id_pc][0]
            modelo = pcs[id_pc][1]
            elemento = f"{marca} {modelo}--{id_pc}: {fecha_venta}"
            vendidos.append(elemento)

    return vendidos
# computadoras_vendidas_por_marca("hp")
def busqueda_por_anio(anio_min, anio_max):
    res=[]
    for ids, datos in pcs.items():
        marca=datos[0]
        modelo=datos[1]
        anio=datos[2]
        # rank=datos[3]
        fechaVenta= operaciones [ids][1]
        if anio_min <= anio <= anio_max:
            el = f"{marca}:{modelo}--{ids}"
            res.append((marca,modelo,el))
    try:
        anio_min = int(input("Ingrese el año mínimo: "))
        anio_max = int(input("Ingrese el año máximo: "))

        lista_resultado = busqueda_por_anio(anio_min, anio_max)

        if lista_resultado:
            print("\nComputadoras disponibles en el rango de años ingresado:")
            for item in lista_resultado:
                print(item)
        else:
            print("\nNo existen coincidencias para el rango de años ingresado.")

    except ValueError:
        print("Error: Debe ingresar valores numéricos enteros para los años.")
def actualizar_fecha_venta(id_computadora, nueva_fecha):
    if id_computadora in operaciones:
        operaciones [id_computadora][1]=nueva_fecha
        return True
    else: False
    # sig
    while continuar.lower() == "s":
        id_computadora = input("Ingrese el ID de la computadora: ")
        nueva_fecha = input("Ingrese la nueva fecha de venta: ")

        resultado = actualizar_fecha_venta(id_computadora, nueva_fecha)

        if resultado:
            print(f"Éxito: la fecha de venta de '{id_computadora}' fue actualizada a '{nueva_fecha}'.")
        else:
            print(f"Error: el identificador '{id_computadora}' no existe en el sistema.")

        continuar = input("¿Desea actualizar otra computadora (s/n)? ")

    print("Programa finalizado.")
    # print("¿Desea actualizar otra computadora (s/n)?")
    # if "s":
    #     print("Ingrese nuevo pc")
    # else: "n"
    # print("No realizar act")

def validID(idd): # string
    if idd== "" or idd== " ":
        return True
    else: return False
def validAnio(anio):
    if anio <1980 :
        return True
    else: False
def validRKD(rkd):

    if rkd >= 1 and rkd>=5:
        return False
    else: return True  

# creacion
def crearPcs():
    id =input("ingrese id")
    if validID(id):
        print("Dato invalido")
        return
    marca=input("ingrese marca")
    if validID(marca):
        print("Dato invalido")
        return
    modelo =input("ingrese modelo")
    if validID(modelo):
        print("Dato invalido")
        return
    anioFabr =int(input("ingrese año de fabricacion"))
    if validAnio(anioFabr):
        print("Dato invalido")
        return
    rkd=int(input("ingrese ranking"))
    if validRKD(rkd):
        print("Dato invalido")
        return
    fechaIngreso =int(input("ingrese fecha de ingreso"))
    if validAnio(fechaIngreso):
        print("Dato invalido")
        return
    fechaVenta =int(input("ingrese fecha de venta"))
    if validAnio(fechaVenta):
        print("Dato invalido")
        return

def  eliminar_computadora(id_computadora):
    if id_computadora in operaciones:
        del pcs [id_computadora]
        del operaciones [id_computadora] 
        return True
    else: False

def menu():
    print('''--------------------------------------------------
----------MENÚ GESTIÓN DE AUTOS----------
==================================================
1. Mostrar todos los pcs
2. Mostrar pcs vendidos
3. Total de pcs vendidos por marca
4. Actualizar fecha de venta
5. Crear nuevo pc
6. Eliminar pc
0. Salir
--------------------------------------------------''')
def principal():
    while True:
        menu()
        try:
            op=int(input("Seleccione servicio"))
            if op==1:
                mostrarPcs(pcs)
            elif op== 3:
                marca=input("ingresa nombre de marca que buscar")
                computadoras_vendidas_por_marca(marca)
                