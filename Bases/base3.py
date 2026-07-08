familia={
    "a1":["Mario", "Padre", 61, 934219791],
    "a2":["Valentina", "Hermana", 28, 934219724],
    "a3":["Benjamin", "Hermano", 23,934219722],
    "a4":["Pilar", "Madre", 60, 934219764 ],
}
cumpleanioYFiesta={
    "a1":["02-10-1964", "fiesta de cumpleaños el dia sabado 05-10-2026"],
    "a2":["19-09-1997", "fiesta de cumpleaños el dia sabado 23-09-2026"],
    "a3":["28-12-2002", "fiesta de cumpleaños el dia sabado 30-12-2026"],
    "a4":["10-07-1966", "fiesta de cumpleaños el dia sabado 10-07-2026"],
}


 # dentro del diccionario debe ir el id "key" del nuevo usario
def mostrarFamily(famili):
    for fam,nam in famili:
        print(f"{fam} : {nam}")
mostrarFamily(cumpleanioYFiesta)