# uso y eplicacion de diccionarios

# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"piloto"
# }

# # print(alumno)
# # print(alumno["carrera"])

# for key ,value in alumno.items():
#     print(f"{key}= {value} ")
# print("---Cambios de datos---")
# # for dato ,valor in alumno.items():
# #     print(dato, valor )
# alumno["email"]="shinji@nerv.com"
# alumno["carrera"]="escritor"
# del alumno["edad"]
# for key ,value in alumno.items():
#     print(f"{key}= {value} ")

productos={
    1:{"nombre": "Control Inalambrico",
       "categoria": "Electronica",
       "precio": 45000},
    2:{"nombre": "Pilas Recargables",
       "categoria": "Insumos",
       "precio": 5000},
    3:{"nombre": "Pasta Termica",
       "categoria": "Computacion",
       "precio": 7000},
}

print(productos[1]["nombre"])

'''
Crear un diccionario de trabajadores 
'''

##CRUD DE VEGETALES

vegetales={
   1:"Maracuyá",2:"Pera",3:"Cebolla",7:"Papa"
}

print(list(vegetales.keys())[-1])


def agregarVegetales():
   print("-"*20)
   agregar=input("Ingrese un vegetal: ")
   nuevoKey=list(vegetales.keys())[-1]
   vegetales[nuevoKey+1]=agregar
def mostrarVegetales():
   print("-"*40)
   for num, nombre in vegetales.items():
         print(f"{num}.- {nombre} ")
def eliminarVegetal():
   mostrarVegetales()
   borrar=int(input("Cual vegetal borrará?: "))
   del vegetales[borrar]
def actualizarVegetal():
   mostrarVegetales()
   act=int(input("Cual vegetal actualizará?: "))
   vegetales[act]=input("Ingrese nuevo nombre: ")

def vegetalesMenu():
   while True:
      try:
         print("-"*20)
         print("1.- Agregar Vegetal")
         print("2.- Eliminar Vegetal")
         print("3.- Actualizar Vegetal")
         print("4.- Mostrar Vegetal")
         print("5.- Salir")
         op=int(input("Seleccione una opcion: "))
         match op:
               case 1:
                  agregarVegetales()
               case 2:
                  eliminarVegetal()
               case 3:
                  actualizarVegetal()
               case 4:
                  mostrarVegetales()
               case 5:
                  print("Salir")
                  break
               case _:
                    print("Opcion invalida")  
      except Exception as e:
         print("Error:",e)

# vegetalesMenu()

##Diccionario con diccionarios
productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}
productosDicc[4]={"nombre": "Piña", "precio": 3500}
def agregarProducto():
   print("Cual es el nombre del producto?")
   nombre = input()
   print("cual es el precio?")
   precio = int(input())
   nuevoKey=list(productosDicc.keys())[-1]
   productosDicc[nuevoKey+1]= {"nombre": nombre, "precio": precio}
def MostrarProducto():
   for key, producto in productosDicc.items():
      print(f"{key} .{producto}")
def eliminarProducto():
   MostrarProducto()
   borrar=int(input("Cual Producto borrará?: "))
   del productosDicc[borrar]
def actualizarProducto():
   MostrarProducto()
   num=int(input("Que producto desea actualizar?: "))

   nombre=input("Cual es el nombre nuevo?: ")
   precio=int(input("Cual es el precio nuevo?: "))
   productosDicc[num]={"nombre": nombre, "precio": precio}
# print(productosDicc[2]["precio"])  # precio de la pera
# print(productosDicc[3]["nombre"])  # nombre de la cebolla

# for num, veg in productosDicc.items():
#     print(f"{num}.- {veg}")

##Lista con diccionarios
# productosList={
#   1: {"nombre": "Maracuyá", "precio": 3000}, #0
#    2:{"nombre": "Pera", "precio": 1500},     #1  
#    3:{"nombre": "Cebolla", "precio": 1200}   #2
# }

# print(productosList.key())
# print(productosList)
# print(productosList[2]["precio"]) #precio de la cebolla
# print(productosList[0]["nombre"]) #nombre de la naracuya



# def vegetalesMenuDiccionario():
#    while True:
#       try:
#          print("-"*20)
#          print("1.- Agregar Vegetal")
#          print("2.- Eliminar Vegetal")
#          print("3.- Actualizar Vegetal")
#          print("4.- Mostrar Vegetal")
#          print("5.- Salir")
#          op=int(input("Seleccione una opcion: "))
#          match op:
#                case 1:
#                   agregarProducto()
#                case 2:
#                   eliminarProducto()
#                case 3:
#                   actualizarProducto()
#                case 4:
#                   MostrarProducto()
#                case 5:
#                   print("Salir")
#                   break
#                case _:
#                     print("Opcion invalida")  
#       except Exception as e:
#          print("Error:",e)
# vegetalesMenuDiccionario()

#Cambiar la funcion actualizar para que solo 
# actualice una solo key 
# Ademas, crear un CRUD pero con la lista 
# de diccionarios.


 #Diccionario con diccionarios
# pcs={   
#     1:{"name": "MSI", "pecio": 1649.00 },#0
#     2:{"name": "Dell", "precio": 1279.99},  #1  
#     3:{"name": "Lenovo)", "precio": 649.00},   #2
# }

#     #Lista con diccionarios
# # pcs=[
# #    {"nombre": "msi", "precio": 3000}, #0
# #    {"nombre": "hp", "precio": 1500},     #1  
# #    {"nombre": "acer", "precio": 1200}   #2
# # ]
# def addNotebook():
#    print("-"*25)
#    nombre = input("Ingrese el nombre del producto nuevo: ")
#    precio = float(input("Ingrese el precio: "))
#    newKey = list(pcs.keys())[-1]
#    pcs[newKey + 1] = {"nombre": nombre, "precio": precio}
#    print("-"*25)

# def delPcs():
#    print("-"*25)
#    showPcs()
#    eliminar=input(int("Eliminado"))
#    if 0 <= eliminar < len(pcs):   # ← validar que el índice exista
#       pcs.pop(eliminar)           # ← borrar de la lista "pcs"
#       showPcs()
#    else:
#       print("Eleccion no válido.")
#    print("-"*25)

# def actListPc():
#    print("-" * 25)
#    showPcs()
#    key = int(input("¿Qué computador desea actualizar? "))
#    if key not in pcs:
#       print("Clave no encontrada.")
#       return
#    print("¿Qué desea actualizar?")
#    print("  1.- Nombre")
#    print("  2.- Precio")
#    op = int(input("Opción: "))
#    if op == 1:
#       pcs[key]["nombre"] = input("Nuevo nombre: ")        # ← solo input(), sin int()
#    elif op == 2:
#       pcs[key]["precio"] = float(input("Nuevo precio: "))
#    else:
#       print("Opción inválida.")
#       return
#    showPcs()
#    print("-"*25)
# def showPcs():
#    print("-"*25)
#    for num , nombre in pcs.items():
#          print(f"{num} = {nombre}")
#    print("-"*25)

# def tueniPcs():
#     while True:
#         try:
#             print('''
#             1.- Agregar computadoras        
#             2.- Eliminar computadora
#             3.- Actualizar diccionario de computadora
#             4.- Mostrar computadora
#             5.- Salir
#             ''')
#             op=int(input("Selecciona una opcion "))
#             match op:
#                   case 1:   addNotebook()
#                   case 2:   delPcs()
#                   case 3:   actListPc()
#                   case 4:   showPcs()
#                   case 5:
#                      print("Cerrando programa...")
#                      break
#                   case _:
#                     print("Opcion invalida")
#         except Exception as e:
#             print("Error", e)
# tueniPcs()


pokemon={
   1:{"nombre": "blablabla",
      "lvl": 14,
      "hp" : 32,
      "atk" : 
      {
         1:{"Nombe" : "plakaje", "daño" : 33},
         2:{"Nombe" : "plakaje", "daño" : 33},
         3:{"Nombe" : "plakaje", "daño" : 33},
         4:{"Nombe" : "plakaje", "daño" : 33}
      },
      "def": 10,
      "type" : "normal",
      "vel" : 12,
      
      
         }
}



'''006 ej dicc'''


productosDicc={
   1:{"nombre": "Maracuyá", "precio": 3000},
   2:{"nombre": "Pera", "precio": 1500},
   3:{"nombre": "Cebolla", "precio": 1200}
}
productosDicc[4]={"nombre": "Tomate", "precio": 1500} 


# print(productosDicc.keys())
# print(productosDicc.values())
# print(productosDicc.items())
# listadeKeys=list(productosDicc.keys())

# print(list(productosDicc.keys())[-1])
carrito=[]
def agregaProducto():
    nombreP=input("Ingrese el nombre del Producto: ")
    precioP=int(input("Ingrese el precio del Producto: "))
    productosDicc[list(productosDicc.keys())[-1]+1]={"nombre": nombreP, "precio": precioP} 

def muestraProducto():
    print("-"*30)
    for nombre, precio in productosDicc.items():
        print(f"{nombre} .-  {precio}")
    print("-"*30)

def eliminaProducto():
    muestraProducto()
    borra=int(input("Cual desea eliminar?: "))
    del productosDicc[borra]
    
def actualiazaProducto():
    muestraProducto()
    actualiza=int(input("Cual producto desea actualizar?: "))
    nuevonombre=input("ingrese el nuevo nombre") 
    nuevoPRECIO=input("ingrese el nuevo precio") 
    productosDicc[actualiza]={"nombre":nuevonombre , "precio": nuevoPRECIO}

def comprar():
    muestraProducto()
    try:
        comprar=int(input("Cual producto desea comprar ?: "))
        if comprar in productosDicc:
            print(f"Usted ha comprado {productosDicc[comprar]['nombre']} por un valor de {productosDicc[comprar]['precio']}")
            carrito.append(productosDicc[comprar])
        else:
            print("Producto no existe")
            
    except ValueError:
         print("Debe ingresar un número válido")
          
      
def boleta():
    total=0
    for p in carrito:
        try:
            total+=int(p["precio"])
            nombreP= ""
            precioP = 0 +1
            p[list(productosDicc.keys())[-1]+1]={"nombre": nombreP, "precio": precioP} 

        except (ValueError, TypeError):
            print(f"Precio inválido para {p.get('nombre','?')}, contando como 0")
    iva=total*0.19
    print(f"El total de su compra es {total} y el IVA es {iva}")
    print(f"El total a pagar es  {total+iva} ")
def productosMenu():
    while True:
        try:
            print("1.- Agregar Producto")
            print("2.- Eliminar Producto")
            print("3.- Actualizar Producto")
            print("4.- Mostrar Producto")
            print("5.- Comprar Productos")
            print("6.- Crear Boleta (calcula IVA) y Salir")
            op=int(input("Seleccione una opcion: "))
            match op:
                case 1:
                    agregaProducto()
                case 2:
                    eliminaProducto()
                case 3:
                    actualiazaProducto()
                case 4:
                    muestraProducto()
                case 5:
                    comprar()
                case 6:
                    boleta()
                    print("Salir")
                    break
                case _:
                    print("Opcion invalida")  
        except Exception as e:
            print("Error :", e)
productosMenu()