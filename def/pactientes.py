## Crear un gestor de pacientes



'''crear al gestor de pacientes en un centro medico
Para poner el nombre se debe validar que no este vacio 
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
FOnasa 54%
Isapre 27%
Fodesa 12,5%

'''
pacientes=[
    {"nombre": " Aquiles Baeza", "prevision": "Fonasa", 
     "temperatura":34.6, "grave": False}
]

pacientes.append({"nombre": "Alan Brito", "prevision": "Isapre", 
     "temperatura":39.6, "grave": True})



def validarEstado(tempe):
   if tempe>39:
       return True 
   else:
       return False
def mostrarPacientes():
    if len(pacientes)==0:
        print("No hay pacientes")
    else:
        c=1
        for p in pacientes:
            print(f"{c} .- {p}")
            c+=1
def agregarPaciente():
    nombre=input("Ingrese nombre: ")
    prevision=input("Ingrese prevision: ")
    temp=float(input("Ingrese temp: "))
    pacientes.append({"nombre": nombre, "prevision": prevision, 
                "temperatura":temp, "grave": validarEstado(temp)})
    print("Paciente agregado al listado")
def eliminarPaciente():
    mostrarPacientes()
    paci=int(input("Que paciente se vá?: "))
    pacientes.pop(paci-1)
    print("Paciente eliminado.")
def tomarTemp():
    mostrarPacientes()
    paciente=int(input ("A que paciente le tomamos temperatura?: "))
    tomarTemp=float(input("ingrese su temperatura: "))
    pacientes[paciente-1]["temperatura"]=tomarTemp
    pacientes[paciente-1]["grave"]=validarEstado(tomarTemp)
def cobrarAtencion():
    mostrarPacientes()
    pa=int(input("¿que paciente va a pagar?: "))
    if pacientes[pa-1]["prevision"].lower()=="fonasa":
        pagar=25000*0.46
    elif pacientes[pa-1]["prevision"].lower()=="isapre":
        pagar=25000*0.73
    elif pacientes[pa-1]["prevision"].lower()=="fodesa":
        pagar=25000*0.875
    else:
        print("prevision incorrecta")
    print("Su total a pagar es: ", pagar)
while True:
    try:
        print("1.- Ingresar paciente")
        print("2.- Quitar paciente")
        print("3.- Tomar Temperatura")
        print("4.- Cobra atencion")
        print("5.- Mostrar Pacientes")
        print("9.- Salir")
        op=int(input("Ingrese una opcion: "))
        match op:
            case 1:
                agregarPaciente()
            case 2:
                eliminarPaciente()
            case 3:
                tomarTemp()
            case 4:
                cobrarAtencion()
            case 5:
                mostrarPacientes()
            case 9:
                print("Saliendo")
                break
            case _:
                print("Opción inválida")
    except Exception as e:
        print("Error:" , e)