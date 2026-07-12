# Diccionario 1: Datos fijos del libro [Título, Autor, Año, Copias Disponibles]
libros = {
    'L001': ['Cien años de soledad', 'Gabriel García Márquez', 1967, 3],
    'L002': ['Don Quijote', 'Miguel de Cervantes', 1605, 1],
    'L003': ['1984', 'George Orwell', 1949, 0],
    'L004': ['El Principito', 'Antoine de Saint-Exupéry', 1943, 5]
}

# Diccionario 2: Operaciones [Fecha de Salida, Estado de Devolución]
prestamos = {
    'L001': ['10-05-2026', 'Devuelto'],
    'L002': ['14-06-2026', 'Pendiente'],
    'L003': ['01-07-2026', 'Pendiente'],
    'L004': ['20-06-2026', 'Devuelto']
}
def mostrarTitulos(libros):
    for id , book in libros.items():
        print(f"{id} : {book} ")
# mostrarTitulos(libros)
print("-"*63)
def presYDev(libros):
    for prestado, devuelto in libros.items():
        print(f"{prestado} : {devuelto}")
# presYDev(prestamos)

def librosPrestados(Tittles):
    prestados=0
    for id, prest in prestamos.items():
        if prest [0].lower()== Tittles.lower():
            if prestamos [id] [-1]!= "Pendiente":
                prestados+=1
    print(f"la cantidad de titulos prestados son {prestados} bajo el titulo de {Tittles}")
# librosPrestados("don quijote")
def actualizarFecuasDev(id, fechaNueva):
    if id in prestamos:
        prestamos [id][-1]==fechaNueva
        return True
    else: return False
    # Verificando libros 
def verifFechaLanzamien(VFL):
    if VFL<1900:
        return False
    else: True
    # este tipo de funciones se relaciones en la formula,
def validaranking(r):
    if r>=1 and r<= 5:
        return False
    else: return True
    # la cual es "sensilla" por lo pedido
def validaString(h):
    if h=="" or h==" ":
        return True
    else: return False