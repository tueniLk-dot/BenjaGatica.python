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
# print(operaciones["A002"][-1]) # -1 muestra el ltimo y 0 el primero
# pendiente es q aun no se vende

#funcion para mostrar los autos

def mostrarAutos(diccio):
    for id, auto in diccio.items():
        print(f"{id}: {auto}")
# mostrarAutos(autos)
# print("-"*50)
#muestrasolo autos vendidos
def mostrarVendid(ope):
    for id, auto in ope.items():
        if operaciones[id][-1]!="Pendiente":
            print(f"{id}: {auto}")
# mostrarVendid(autos)
# print("-"*25,"Paso 1", "-"*25)
# #paso1
def autos_vendidos_por_marca(marca):
    total=0
    for id, auto in autos.items():
        if auto [0].lower()==marca.lower():
            if operaciones[id][-1]!="Pendiente":
                total+=1
    print(f"El total de autos vendidos es {total} en la marca {marca}")
# autos_vendidos_por_marca("chevrolet")
# print("A013" in operaciones) ## se usa para validar la accion si es true o false
print(operaciones["A003"][-1]) ## validar para usar en codigo
def actualizar_fecha_venta(id_auto, nueva_fecha):
    if id_auto in operaciones:
        operaciones[id_auto][-1]==nueva_fecha
        return True
    else: return False

# while True:

#     id= input("Ingrese el id del auto ") ## estos no existen en la funcion anterior
#     fecha=input("Ingrese la fecha de venta ")
#     if actualizar_fecha_venta(id, fecha):
#         print("exito, buena actualizacion ")
#     else: print("No pudo ser creado ")
#     next=input("desea actualizar otro vehiculo (s/n?")
#     if next.lower()=="n":
#         break

def validaString(h):
    if h=="" or h==" ":
        return True
    else: return False
def validaAño(a):
    if a<1900:
        return False
    else:return True
    
def validaranking(r):
    if r>=1 and r<= 5:
        return False
    else: return True

def independientes():
    id=input("Ingrese el ID ")
    if validaString(id):
        print("Dato invalido ")
        return
    marca=input("Ingrese la marca ")
    if validaString(marca):
        print("Dato invalido ")
        return
    modelo=input("Mencione el modelo ")
    if validaString(modelo):
        print("Dato invalido ")
        return
    año=input("Ingrese añ del vehiculo ")
    if validaAño(año):
        print("Dato invalido ")
        return
    ranking=input("Indique el rating del vehiculo ")
    if validaranking(ranking):
        print("el ranking debe estar entre 1 y 5 ")
        return
    fechaDeIngreso=input("Ingrese la fecha de ingreso ")
    if validaString(fechaDeIngreso):
        print("Dato invalido ")
        return
    fechaDeVenta=input("Ingrese la fecha de venta")
    if validaString(fechaDeVenta):
        print("Dato invalido ")
        return
    autos[id]=[marca, modelo,año,ranking,]
    operaciones[id]=[fechaDeIngreso,fechaDeVenta]
    
print("TILT")
mostrarAutos(autos)
independientes()
mostrarAutos(autos)

def eliminar_auto(id_auto):
    if id_auto in operaciones:
        del autos[id_auto][-1]==nueva_fecha
        del operaciones[id_auto][-1]==nueva_fecha
        return True
    else: return False
    

''''Hacer un menu con todas las funciones
que hicismos y usamos en clase,
debe tener manejo de errores o sea
Try- except'''