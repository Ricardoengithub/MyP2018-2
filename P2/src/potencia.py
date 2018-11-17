def potencia(x,y):
	if (y == 0):	
		return 1
	elif (y == 1):
		return x
	else:
		return x * potencia(x,y-1)
		
x = int(input("Escribe x: "))
y = int(input("Escribe la potencia a la que quieres elevar x: "))

print(potencia(x,y))		
