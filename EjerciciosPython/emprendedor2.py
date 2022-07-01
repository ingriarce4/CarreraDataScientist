# Crear el programa emprendedor2.py donde el usuario ingrese el precio, el número de
# usuarios totales(incluyendo a usuarios premium y gratuitos), el número de usuarios
# premium(pagan el doble), el número de usuarios gratuitos(no pagan) y los gastos. El programa
# debe calcular las utilidades.

import sys

p=float(sys.argv[1])
total=int(sys.argv[2])
premium=int(sys.argv[3])
gratuito=int(sys.argv[4])
g=float(sys.argv[5])
u=(p*(2*premium+(total-premium-gratuito)))-g

if u>0:
    u=u*0.65
    print("La utilidad menos impuestos {}".format(u))
else:
    
    print("La utilidad menos impuestos {}".format(u))

    