#Funciones guia examen
 
 
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}
def mostrarAutos(mostrar):
    for id, auto in mostrar.items():
        print(f"{id}:{auto}")
# mostrarAutos(autos)
print("-"*76)
def mostrarStock(op):
    for id,stock in op.items():
        if operaciones[id][0].lower():
            print(f"{id}:{stock}")
# mostrarStock(operaciones)
# ---------- paso 1--------------
def autos_vendidos_por_marca(marca):
    total=0
    for id_auto, auto in autos.items():    
        if auto[0].lower() == marca.lower():
            if operaciones [id_auto][1]!="Pendiente":
                total+=1
    print(f"El total de autos vendidos de la marca {marca} es la cantidad de {total}")
# autos_vendidos_por_marca("chevrolet")
# ------------------paso2----------
def  busqueda_por_anio(anio_min, anio_max):
    result = []
    for id_auto , datos in autos.items():
        marca,modelo,anio,stock = datos
        if anio_min <= anio <= anio_max:
            fecha_venta=operaciones[1]
            if fecha_venta == 'pendiente':
                result.append(f"{marca}{modelo}--{id_auto}")
        
        

def busqueda_por_anio(anio_min, anio_max):
    resultados = []

    for id_auto, datos in autos.items():
        marca, modelo, anio, stock = datos
        # Condición 1: el año debe estar dentro del rango
        if anio_min <= anio <= anio_max:
            # Condición 2: la fecha de venta debe ser "Pendiente"
            fecha_venta = operaciones.get(id_auto, [None, None])[1]
            if fecha_venta == 'Pendiente':
                resultados.append(f"{marca} {modelo}--{id_auto}")