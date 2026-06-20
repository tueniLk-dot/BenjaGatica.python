'''poner en  lista el nombres ,
 edad y hobbie de cada integrantes de la familia 
 y extras mostrar todls lls elementos concatenados 
 con nombre edas y hobbie'''
family=[
    {"nombre": "Pilar", "edad" : 59, 
    "hobbie" : "Ver tele", "quien es?" : "mamá"},   
    {"nombre": "Victor", "edad" : 61, 
    "hobbie" : "Ver realitis", "quien es?" : "papá"},   
    {"nombre": "Valentina", "edad" : 29, 
    "hobbie" : "Ver peliculas", "quien es?" : "hermana"},    
    {"nombre": "Cristian", "edad" : 34, 
    "hobbie" : "Andar en moto", "quien es?" : "hermano"},
    {"nombre": "Benjamin", "edad" : 23, 
    "hobbie" : "Los gatos", "quien es?" : "yo"}   
]
print(family[0])
print(family[1]["nombre"])
print(family[1]["edad"])
print(family[2]["edad"],family[3]["edad"])
print(family[4]["edad"], family[4]["nombre"])

total=0
for edades in family:
    total+=edades["edad"]
print("La suma de las edades es : ", total)
nombres=[]
for names in family:
    nombres.append(names["nombre"])
print(nombres)



# nuevoNombre=                               [input("Ingresa su nombre: " )]
# nuevaEdad=[int(input("ingresa su edad: " ))]
# hobbieExtra=[input("Ingresa su hobbie: ")]
# nuevoQuienEs=[input("Quien es?: ")]
# añadirCompleto={"nombre": nuevoNombre , "edad" : nuevaEdad,
#     "hobbie" : hobbieExtra, "quien es?" : nuevoQuienEs}
# print(añadirCompleto)
# print("nombre: ", nombres[2]["nombre"], "edad: ",nombres[3] )