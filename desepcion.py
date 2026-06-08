usr1= None
psswd1=None
usr2= None
psswe2=None
usr3= None
psswd3=None
print("Bienvenido al menú Gatica. ")
while True:
    try:
        print("selecciona una opcion")
        menu=int(input('''
            1- Inicar sesion
            2- Regustrar usuario
            3- Salir
             '''))
        match menu:
            case 1:
                while True:
                    try:
                        print("Iniciar sesion, selecciona una opcion ")
                        menu2=int(input('''
                                    1- Realizar llamada
                                    2- enviar correo electronico
                                    3- Cerrar sesion 
                                        '''))
                        match menu2:
                            case 1: 
                                print("Realizar llamada")
                            case 2:
                                print("Enviar correo electronico")
                                
                            case 3:
                                print("Cerrando sesion")
                                break
                            case _:
                                print("Opcion no valida, reintente")    
                    except ValueError:
                        print("Error, debe ingresar solo numeros disponibles.")
                
                        
            case 2: 
                print("Registro nuevo usuario")
            case 3:
                print("Cerrando programa. ")
                break
            case _:
                print("Opcion no valida, reintente")
    except ValueError:
        print("Error, debe ingresar solo numeros disponibles.")