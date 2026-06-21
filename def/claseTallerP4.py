# lista=[3,6,8,1.3,5.2,["link", "zelda"], {"pkm":"weedle"}]
# #      0,1,2,  3 ,4,          5,                6         
# print(lista[6]["pkm"]) # muestra weedle porque es el key 
# lista.append({"dias": "lunes", "temp": 25.6, "humedad" : 29})
# print("-"*50)


# #para mostar todo se necesita el for

# for elemnet in lista:
#     print(elemnet)

# creando otra lista haremos lista de:

pintulas=[
    {"color" : "ROjo", "capacidad" : 1500, "formato" : "tarro" },#0 
    {"color" : "blabco", "capacidad" : 1500, "formato" : "bolsa" },#1
    {"color" : "azul", "capacidad" : 3500, "formato" : "tinaja" },#2
    {"color" : "verde", "capacidad" : 500, "formato" : "botella" },#3
   
]
def agregarP():#1
    color=input("Que color será?")
    capacidad=int(input("Que capacidad será?"))
    formato=input("Que formato será?")
    pintulas.append({"color":color, "capacidad" : capacidad, "formato": formato, })
def quitarP():#2
    mostrarP()
    el=int(input("Que pintura va a eliminar? "))
    pintulas.pop(el-1)
def actP():
    mostrarP()
    act=int(input('''Que desea actualizar?
                              1.- color
                              2.- capacidad
                              3.- formato 
                  ''')) 
    if not pintulas:
        return
    p=pintulas[act-1]
    match act:
        case 1:
            color=input("Que color actualizara?")
            p["color"] = input("Nuevo color: ").strip()
            {"color" : color}
            print("✅ Color actualizado.")
        case 2:
            
                capac=input("Que capacidad actualizara?")
                p["capacidad"] = int(input("Nueva capacidad: "))
                {"capacidad":capac}
                print("✅ Capacidad actualizada.")
               
            
        case 3:
            formato=input("Que formato actualizara?")
            p["formato"] = input("Nuevo formato: ").strip()
            {"formato":formato}
            print("✅ Formato actualizado.")
        case _:
            print("❌ Opción inválida.")
def mostrarP():
    if len(pintulas)==0:
        print("No hay pacientes")
    else:
        print("--"*20)
        print("Estas son las pinturas disponibles:")
        print("--"*20)
        c=1
        for p in pintulas:
            print(f"{c} .- {p}")
            c+=1
        print("--"*20)
while True:
    try:
        op=int(input('''selecciona una opcion
                     1.- Agragar pintura
                     2.- Quitar pintura
                     3.- Actualizar pinturas 
                     4.- mostrar pintura
                     0.- salir
                     '''))
        match op:
            case 1:
                agregarP()
            case 2:
                quitarP()
            case 3:
                actP()
            case 4:
                mostrarP()
            case 0:
                print("saliendo") 
                break
    except Exception as e:
        print("error, invalido, reintente", e)
pintulas()