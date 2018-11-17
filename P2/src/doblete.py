contador,salida = 0,0
lista = []
exit = 0
while (exit == 0):
	x = input("Escribe la palabra o escribe 1 para saber si es doblete: ")
	if(x == "1"):
	 	exit = 1
	 	break
	else:
		lista.append(x)
		
while (len(lista)!= 1):
	
	y = list(lista[0])
	z = list(lista[1])
	if (len(y) != len(z)):
		print("No es doblete")
	else:
		for i in range(0,len(y)):
			if(y[i] != z[i]):
				contador+=1
				if(contador==2):
					salida = 1
					print("No es doblete")
			else:
				contador = contador
		contador = 0
		del(lista[0])
		
if ((contador == 0) and (salida != 1)):
	 print("Es doblete")		
		
