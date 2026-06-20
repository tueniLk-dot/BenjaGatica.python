# crear un gestor de peliculas
# EL titulo debe tener mas de 2 caracteres
# el año debe ser mayor a 1960 y debe der menor al año actual
# El director debe tener nombre y apellido
# mostar el sigueinte menú
#  
'''
1.- ingresar Pelucula
2.- quitar Pelucula
3.- ingresar Pelucula
4.- Mostar Peluculas
5.- Mostrar solo los titulos
6.- Ordenar de mas reciente a mas antigua
7.- Salir
'''

pelis=[
    {"tittle" : "Ice Age", "anio" : 2002, "director" : "Chris Wedge", "genero": "animado"},
    {"tittle" : "Fast and forious", "anio" : 2001, "director" : "Rob Cohen", "genero": "accion"},
    {"tittle" : "Marix", "anio" : 1999, "director" : "Lana Wachowski, Lilly Wachowski", "genero": "ciencia ficcion"},
]
def addPeli():
    titulo=input("Ingresa un nuevo titulo: ")
    anio=int(input("Ingresa año de la pelicula: "))
    director=input("Ingrese al director de la pelicula: ")
    genero=input("Ingresa el genero de la pelicula: ")
    pelis.append({"tittle" : titulo, "anio" : anio, "director" : director, "genero": genero})
    mostrarTitulos()
def quitarPelis():
    mostrarPeli()
    peli=int(input("Que pelicula se quita ?: "))
    pelis.pop(peli-1)
    print("Pelicula eliminada ")
def actTitulo():
    mostrarPeli()    
    actName=int(input("A que pelicula actualzara/ cambiaras el nombre?: " ))
    pelis  [actName-1]["tittle"]=input("nombre actualizado a: ")

def mostrarPeli():
    if len(pelis)==0:
        print("No hay peliculas")
    else:
        c=1
        for p in pelis:
            print(f"{c} .- {p}")
            c+=1
def mostrarTitulos():
    for mostrar in pelis:
        print(mostrar["tittle"])
def salir7():
    print("Salida")

while True:
    try:
        op=int(input('''
        1.- ingresar Pelucula
        2.- quitar Pelucula
        3.- actualizar Pelicula
        4.- Mostar Peluculas
        5.- Mostrar solo los titulos
        6.- Ordenar de mas reciente a mas antigua
        7.- Salir
        '''))
        match op:
            case 1:
                addPeli()
            case 2:
                quitarPelis()
            case 3:
                actTitulo()
            case 4:
                mostrarPeli()
            case 5:
                mostrarTitulos()
            case 6:
                print("")
            case 7:
                salir7()
                break
            case _:
                print("Error de seleccion, reintente")
    except Exception as e:
        print("Seleccion invalida, reintente",e )






