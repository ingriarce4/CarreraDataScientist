# Crear el programa emprendedor2.py donde el usuario ingrese el precio, el número de
# usuarios totales(incluyendo a usuarios premium y gratuitos), el número de usuarios
# premium(pagan el doble), el número de usuarios gratuitos(no pagan) y los gastos. El programa
# debe calcular las utilidades.


import sys

p=float(sys.argv[1])
n=int(sys.argv[2])
g=float(sys.argv[3])
ua=0

if len(sys.argv)<5:
    ua=1000  
else:
    ua=float(sys.argv[4])

u=p*n-g
ufinal=u*0.65
uff=ufinal+ua
uf=u+ua
if(u>0):
    print("La utilidad actual mas anterior {}".format(uff))
else:
    i=0
    print("La utilidad actual mas anterior {}".format(uf))


