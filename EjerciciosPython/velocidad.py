# Desafío - Velocidad de escape

# Instrucciones
# Resolver el siguiente desafío y subirlo a la plataforma Empieza.
# Contexto
# La velocidad de escape de un planeta (la velocidad mínima necesaria para poder salir de un planeta)
# está dada por la siguiente ecuación.
# Donde:
# g: es la gravedad del planeta
# r: es el radio del planeta (en metros)
# Requerimientos
# Se pide crear el programa escape.py donde el usuario ingrese la gravedad y el radio y como
# resultado obtenga la velocidad de escape (ocupar la formula)
# Desarrollar el diagrama de flujo antes del programa
# Verificar el funcionamiento con los datos de la tierra:
# g = 9.8 mts/seg^2
# r = 6371 kms
# Respuesta: 11174.59 aprox
# Importante: Utilizar argv en lugar de input
# El primer parámetro será g
# El segundo parámetro será r (debe ser entregado en kms)
# El programa debe poder ejecutarse como: python escape.py 9.8 6371

# Consideraciones
# 1. Su respuesta puede ir dentro de una oración, sin embargo, se considerará como respuesta
# valida el último número dentro de la oración. Por ejemplo:
# La velocidad de escape es 6779 m/s (en este caso, la respuesta evaluada seria solo 6779)
# 2. Los argumentos podrían ser de tipo FLOAT o INT



#velocidad 
#g es m/s
# r = km/s
#formula   (raíz cuadrada)v = 2gr
import math

g= float(input())
r = int(input())


ve = math.sqrt(2*g*1000*r)

print("La raiz cuadrada  es {}".format(ve))

