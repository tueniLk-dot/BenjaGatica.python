# Funcion sin argumento y sin return
def suma():
    n1=("ingresa un numero ")
    n2=("ingresa otro numero ")
    print(n1+n2)
# con argumento y sin return
def suma_arg(n1,n2):
    print(n1+n2)
# sin argumento y con return
def suma_ret():
    n1= int(input("Ingrese un numero"))
    n2= int(input("Ingrese otro numero"))
    return n1+n2
# con argumento con return
def sumass(n1,n2):
    return n1 + n2 

product={
    1:{"nombre" : "agua con gas 500cc", "precio": 1000},
    2:{"nombre" : "CocaCola en lata 374cc", "precio": 1000},
    3:{"nombre" : "Kilogramo de pan", "precio": 1000},
    
}
print(product[3])

# perros de caza

perros= { #Diccionario de diccionario 
    1: {"nombre ": "Doppy", 
        "Raza" : "Doghount",
        "Codigo" : "Dphh06"}
}

while True:
    try:
        print('''
            1.- Resgistrar un perro
            2.- Mostrar perros
            3.- Salir ''')
        op= int(input("seleccione una opcion "))
        match op:
            case 1:
                nombre=input("ingrese un nombre: ")
                raza=input("Ingrese la raza: ")
                code=input("ingrese su codigo: ")
                perros [2]={1: {"nombre ": nombre, 
                                "Raza" : raza,
                                "Codigo" : code}}
            case 2:
                print(perros)
            case 3:
                print("Saliendo")
                break
            case _:
                print("Opcion invalida")
    except Exception as e:
        print("El error es: ",e)