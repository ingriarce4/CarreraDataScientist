

# Un emprendedor quiere crear una aplicación y necesita saber si es rentable, para eso tiene que:
# El producto planea venderse en 50 dólares.
# Se espera tener 1000 usuarios en el año.
# Los gastos del año son 20000 dólares
# Las utilidades se calculan como 
# Los impuestos aplicados a las utilidades son el 35% y solo aplican si es positivo.

# 1. Crear el progama emprendedor1.py donde el usuario ingrese el precio, el número de
# usuarios, los gastos y el programa calcula las utilidades.

import sys
p=float(sys.argv[1])
n=int(sys.argv[2])
g=float(sys.argv[3])
u=p*n-g
ufinal=u*0.65
i=u*0.35
if(u>0):
    print("La utilidad menos impuestos {} \n".format(ufinal))
else:
    i=0
    print("La utilidad menos impuestos {} \n".format(u))
