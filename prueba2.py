# print("Hola Luis")

# # creando variables

# titulo="clima del dia de hoy" #srting
# diaDelMes=13#int 
# mes=4 #int

# temperatura=22.3 #float

# llueve= False #boolean

# print(titulo)
# print("temperatura actual ", temperatura, "grados")
# print(diaDelMes," - ", mes)

# if llueve :
#     print("Tiene que llevar paragua")
# else:
#      print("puede llevar polera sin mangas")

# pedir password y pin
# pedir al usuario password en palabras que deben ser "TEMU"
# ademas pida el pin que debe ser 3435
# los dos deben star correctos para acceder al sstema 

 

# password= "temu"
# pin=3435

# palabra=input("ingrese clave palabra")
# code=int(input("ingresa la clave de numeros"))


# if pin==code and password== palabra:
#     print("correct")
# else: 
#     if password==pin:
#         print()
#     else: "incorrecto"

# cantidadDeIngresos= 500.000 a 1.000.000 : 300.000
# 1.000.000 await 1.500.000 : 650.000
# 1.500.001 o mas : 1.000.000

# basica :x1 , media ;x1.3, superior:x1.5

# nacionaidad: chileno:+300mil, extranjero= 0

ingreso=int(input("Ingrese su sueldo"))

print("1. basico")
print("2. media")
print("3. superior")
edu=input("nivel educacion: ")

nac=input("nacionalidad: ")

credito=0
if ingreso >= 500000 and ingreso <= 1000000:
    credio=credito + 300000
elif ingreso >= 100001 and ingreso <= 1500000:
    credito=credito+650000
elif ingreso >= 150001 :
    creduto=credito+100000
else:
    print("no tiene sueldo suficiente")

if edu==1:
    print("no hay credito")
elif edu==2:
    credio=credio*1.3
elif edu==3:
    credio=credio*1.5

if nac == "chilena":
    credito=credito+300000

else: 
    print("no tiene bono por nacionalidad")


print("Su puntaje de credito es: ",credito)