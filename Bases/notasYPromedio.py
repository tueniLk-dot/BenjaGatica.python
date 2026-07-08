Estudiantes={
    "01" : ["Benjamin Gatica", "Programacion","Pruebas:", 3.7, 2.2, 4.0, 4.6, ],
    "02" : ["Stephen Hawking", "Programacion","Pruebas:" ,7, 7, 7, ],
    "03" : ["Steve Jobs", "Programacion","Pruebas:", 6.5 , 6.6 ,6.4 , 5, ],
    "04" : ["Mark Zuckerberg", "Programacion","Pruebas:" ,3.7, 6.3, 4.0, ],
}
fechaPruebas= {
    "01" : ["01-01-2024 ","12-12-2025 (Hecho)"],
    "02" : ["01-01-2024","Inasistente (Pendiente)"],   
    "03" : ["01-01-2024","12-12-2025 (Hecho)"],
    "04" : ["01-01-2024","Inasistente (Pendiente)"],   
}
# def mostrarEst(lista):
#     for info,estudiantes in lista.items():
#         print(f"{info}: {estudiantes}")
# mostrarEst(Estudiantes)

# def mostrarFec(fechas):
#     for info,fecha in fechas.items():
#         print(f"{info}: {fecha}")
# print("-"*50)
# mostrarFec(fechaPruebas)

# def almnos_fecha_pr(fecha ):
#     for info, fecha in fechaPruebas.items():
#         if fecha[1].lower()!="inasistente (pendiente)":
#             print(f"El alumno {Estudiantes[info][0]} asistio a la prueba el {fecha[0]} y la finalizo el {fecha[1]}")
# print("-"*50)
# almnos_fecha_pr("01-01-2024")
def actFechaPru(id_alumno, nueva_fecha):
    
    if id_alumno in fechaPruebas:
        fechaPruebas[id_alumno][-1]==nueva_fecha
        return False
    else: return True
def validarNota(nota):
    if nota>=4 and nota<=7:
       return True
    else: return False
validarNota(5.5)