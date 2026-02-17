import random

name_person= input("Hola, ¿cómo estás? El sistema quiere verificar tu archivos para saber si eres pato, Indica tu nombre : ")

num= random.randint(0,1)

if num>0.5:
    print(f"Felicidades {name_person}, tus archivos dicen que no eres pato 🦆")

elif name_person == "victor" or name_person == "Victor":
    
    print("Acceso especial concedido, eres el creador del sistema 🦆.CLARAMENTE ERES EL HOMBRE MAS HETERO ")

else:
    print(f"Felicidades {name_person}, tus archivos dicen PAAATOOOOO 🦆")

