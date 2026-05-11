'''Fabrica de enlatados
Se necesita hacer el algoritomo de productos enlatados
Se debe consultar el peso del producto( en gramos) (solo valores positivos)
El porcentaje de sodio en él 
(solo valores entre 1 y 100) y si se va a vender nacional o internacionalmente
Considerar los criterios en la siguiente tabla

menos de 500 grs, lata normal 501g hasta 1500 g, lata mediana
1501 y mas, lata grande si el sodio es menos de 5%, lata queda
igual si es entre 5% y 8% lata especial si tiene 9% o mas, 
lata acorazada a las latas internacionales, se le debbe pegar un sticker 
de validacion sanitaria

Ej:800, 7%, 2==> Jata mediana espacial con sticker sanitario
'''
enlatados=0
sodio=0

print("-------------ENLATADOS TUENI-------------")
print('''
      1- Lata menor a 500g 
      2- Lata normal entre 501g a 1500g 
      3- Lata mediana 1501 y mas 
      4- Lata grande si el sodio es menor de 5%, esta lata queda igual si es entre 5% a 8% 
      5- Lata especial es si tiene 9% o mas 
      6- Lata acorazada 
      7- Latas internacionales con sticker sanitario
      8- Salir
      ''')
tipos=int(input("Seleccione su producto "))




while True:
    try:
        match tipos:
                    
                case 1:
                    # print("Lata normal = $40")
                    # porcent=int(input("Ingresa pocentaje de sodio: "))
                    # if sodio < 5:
                    #     print("Lata chica = $40")
                    #     if enlatados < 5:
                    #         print("Al ser una lata con menos de 500g y menos de 5% en sodio")
                    # else: print("No puede ser lata chica por impueso ndeaa")
                    selG=int(input("Ingrese el gramaje deseado: "))
                    if selG <= 500:
                        print(f"{selG}g puedes llevarlo por $40")
                        # enlatados=int(input(f"{selG}g = $40"))
                    else :
                        print(f"No podras adquirir este producto con este gramaje {selG}g ya que supera el gramaje permitido 500g")            
                
                case 2:
                    # print("Lata normal = $55")
                    selG=int(input("Ingrese el gramaje deseado: "))
                    if selG >= 501 and selG <=1500:
                        print(f"{selG}g puedes llevarlos por $55")
                    else: print(f"No podras adquirir este producto con este gramaje {selG}g, se admiten desde >= 501g hasta <= 1500g")
                
                case 3:
                    # print("Lata mediana = $64")
                    selG=int(input("Ingrese el gramaje deseado: "))
                    if selG >=1501:
                        print(f"{selG}g puedes llevarlo por $35g")
                case 4:
                    
                    # print("Lata grande = 75")
                    selS=int(input("Ingrese el porcentaje de sodio: "))
                    if selS <5 or selS >=5 and selS <= 8:
                        print(f"{selS}% de sodio es permitido para la venta")
                    else: print(f"{selS}% de sodio no es permitido en este producto")
                case 5:
                    
                    # print("Lata especial = 80")
                    selS=int(input("Ingrese el porcentaje de sodio: "))
                case 6:
                    print("")
                    # print("Lata acorazada = 100")
                    selS=int(input("Ingrese el porcentaje de sodio: "))
                case 7:
                    # print("Latas internacionales con sticker sanitario = 100")
                    selS=int(input("Ingrese el porcentaje de sodio: "))
                case 0:
                    print("Cerrando programa")
    except:
        print("Opcion no valida, por favor ingrese una opcion del menu")
            
                
   
# try:
#     if selG <500:
#         print(f"Lata chica de {selG}g")
# except ValueError:
#     print(f"Lata chica con {selS}% de sodio no puede ser vendida.")
# else:     print(f"Lata chica con <5% de sodio no puede ser vendida.")


# while True:
#     try:
#         enlatados=int(input("Ingrese el peso del producto en gramos: "))
#         if enlatados < 0:
#             print("El peso del producto debe ser un valor positivo.")
#         break
#     except ValueError:
#         print("Entrada no válida. Por favor, ingrese un número entero positivo para el peso del producto.")
# print("Todo listo")







































