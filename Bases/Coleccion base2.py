''''Hacer un menu con todas las funciones
que hicismos y usamos en clase,
debe tener manejo de errores o sea
Try- except'''

pcs = {
    'PC01' : ['Lenovo','IdeaPad','i5-8794f',"8gb"],
    'PC02' : ['Hp', 'Pavilion',"i3-6600","4gb"],
    'PC03' : ['Asus', 'TUF Gaming',"i7-13436klg","8gb"],
    'PC04' : ['Hp', 'Aerio',"i5-7032","6gb"],
    'PC05' : ['Lenovo','ThinkPad Serie T',"AMD 5 Pro","12gb"],
    'PC06' : ['Dell', 'XPS',"AMD 3 4321","4gb"],
}
fechaDeVenta = { # "pendiente" significa que no se ha vendido el producto aun
    'PC01' : ['01-01-2024','12-12-2025'],
    'PC02' : ['07-08-2024','Pendiente'],
    'PC03' : ['09-01-2025','Pendiente'],
    'PC04' : ['24-03-2025','Pendiente'],
    'PC05' : ['24-03-2024','24-07-2024'],
    'PC06' : ['24-03-2024','24-09-2024'],
}
def agregrarpcs():
    id=input("Ingrese el id del pc ")
    marca=input("Ingrese la marca del pc ")
    modelo=input("Ingrese el modelo del pc ")
    procesador=input("Ingrese el procesador del pc ")
    ram=input("Ingrese la ram del pc ")
    fechaDeIngreso=input("Ingrese la fecha de ingreso del pc ")
    fechaDeVenta=input("Ingrese la fecha de venta del pc ")
    pcs[id]=[marca, modelo,procesador,ram]
    fechaDeVenta[id]=[fechaDeIngreso,fechaDeVenta]
def pcs_vendidos_por_marca(marca):
    total=0
    for id in pcs:
        if pcs[id][0].lower()==marca.lower():
            if fechaDeVenta[id][-1]!="Pendiente":
                total+=1
    print(f"Los PCS en stock de la marca {marca} son: {total} ")
# pcs_vendidos_por_marca("lenovo")

def buscarPorProcesador(procesador):
    for id in pcs:
        if pcs[id][2].lower()==procesador.lower():
            print(f"El pc con procesador {procesador} es: {id}: {pcs[id]}")
# buscarPorProcesador("i5-8794f")

def actualizar_proce_venta(proce, ram):


# def menu():
    int(input('''Ingrese la opcion que desea realizar
                     1. Agregar un nuevo pc
                     2. Mostrar pcsvendidos por marca
                     3. buscar pc por procesador 
                     4. mostrar pcs
                     5. salir
                     
                    '''))

# while True:
#     try:
#         menu()
#         match op:
#             case 1:
#                     agregrarpcs()
#             case 2:
#                     marca=input("Ingrese la marca del pc ")
#                     pcs_vendidos_por_marca()
#             case 3:
#                     procesador=input("Ingrese el procesador del pc ")
#                     buscarPorProcesador()
#     except Exception as e:
#         print(f"Error: {e}")    