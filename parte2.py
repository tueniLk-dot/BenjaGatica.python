ximport random


r2=3
num=random.randint(1,5)   
print("Tiene 3 oportunudades")

n1=int(input(f"ingresa un numero random, es 1 numeros en juego, entre el 1 y el 5 " ))


 
for r2 in range(3):
    while num:
        
                
            if num!= n1:
                print("Reintenta")
                n1=int(input("ingresa un numero menor: "))
                print(f"Tiene {r2-1} oportunudades")
            else:
                print("Adivinaste! ")
                
    break
            
        