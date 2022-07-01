
# MAYOR ENTRE TRES NÚMEROS

firt_number = int(input())
second_number = int(input())
thri_number= int(input())

if (firt_number > second_number and second_number > thri_number):
	print( "El mayor de tres numeros {}".format(firt_number))
elif (second_number > thri_number):
	print ( "El mayor de tres numeros {}".format(second_number))
else:
	print ( "El mayor de tres numeros {}".format(thri_number))