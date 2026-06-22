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
#diccionario dentro de diccio
pacientes={
    1:{"nombre":"Luci",
       "edad":34,
       "prevision": "fonasa"}
}
def ingresarPaciente():
    ingresa=input("Registrar al paciente: ")
    prevision=input("Indique su provision: ")
    edad=int(input("Ingrese su edad: "))
    idx=len(pacientes)
    idx=list(pacientes.key())[-1]
    pacientes[idx+1]={"nombre":ingresa,
                "edad":edad,
                "prevision": prevision}
def mostrarP(dictt):
    for key,paciente in dictt.items():
        print(key,paciente)
def retirarPaciente():
    mostrarP(pacientes)
    eli=int(input("Seleccionar al paciente a retirar: "))
    del pacientes[eli]
while True:
    try:
        print('''
1.- regustrar al paciente
2.- mostrar pacioente
3.- actualizxar datos 
4.- Quitar paciente
0.- salir
                              ''')
        op=int(input("seleccione una opcion: "))
        match op:
            case 1: 
                ingresarPaciente()
            case 2:
                mostrarP(pacientes)
            case 3:
                print
            case 4: 
                retirarPaciente()
            case 0:
                print("saliendo")
                break
            case _:
                print("error")
    except Exception as e:
        print("Invalido", e)