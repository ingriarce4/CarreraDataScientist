# Se pide crear el programa juego.py , el usuario pasará como argumento piedra, papel o tijera, el programa
# escogerá una opción al azar jugará con número al azar


# Para que el computador pueda jugar escoger un número al azar entre 1 y 3, si es 1 entonces en piedra, si es
# 2 entonces papel y 3 tijera.
# python juego.py piedra
# Computador juega tijera
# Ganaste


# 1 == piedra
# 2== papel
# 3== tijera
import random

jugador = str(input())



if jugador != "piedra" and jugador != "papel" and jugador != "tijera":
	print ("Argumento inválido: Debe ser piedra, papel o tijera.")

else: 
	computador = random.randint(1, 3)

	if computador == 1:
		elige = "piedra"

	elif computador == 2:
		elige = "papel"

	else:
		elige = "tijera"

	if jugador == elige:
		print("Computador juega {}\nEmpataste". format(elige))

	elif (jugador == "tijera" and elige == "piedra") or (elige == "tijera" and jugador== "papel") or (jugador == "piedra" and elige == "papel"):
		print ("Computador juega {}\nPerdiste". format(elige))

	else: 
		print("Computador juega {}\nGanaste".format(elige))