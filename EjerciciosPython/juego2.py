
# python juego.py tijera
# Computador juega tijera
# Empataste


import sys
import random

opcion=sys.argv[1]

if (opcion !="tijera" and opcion !="piedra" and opcion != "papel"):
    print("Argumento inválido: Debe ser piedra, papel o tijera.")
else:    
    c=random.randint(1,3)
    if (c==1):
        c="piedra"
    elif (c==2):
        c="papel"
    elif (c==3):
        c="tijera"
    maquina=c
    print("Computador juega {}".format(maquina))
    if (opcion == maquina):
        print("Empataste")
    elif (opcion == "piedra" and maquina == "papel" or opcion == "papel" and maquina == "tijera" or opcion == "tijera" and maquina == "piedra"):
        print("Perdiste")
    elif (opcion == "piedra" and maquina == "tijera" or opcion == "papel" and maquina == "piedra" or opcion == "tijera" and maquina == "papel"):
        print("Ganaste")
   