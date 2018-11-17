def insertionSort(lista):
	#Para cada elemento de la lista la rrecoremos hasta encontrar su posición donde es mayor que (i-1) y menor que (i+1)
   for i in range(1,len(lista)):

     lugar = i
     valor = lista[i]

     while lugar>0 and lista[lugar-1]>valor:
         lista[lugar]=lista[lugar-1]
         lugar = lugar-1

     lista[lugar] = valor
   #Imprime la lista en pantalla.
   print(lista)
   #Regresamos la lista por que la vamos a utilizar en otras funciones
   return(lista)
   
#Tomamos los valores de los numeros del arreglo y los ordenamos con insertionSort  
def insertionSorts(n):
	lista = []
	x = 1
	while (x!=-1):
		x = int(input("Escribe un número: "))
		if(x==-1):
			break
		else:
			lista.append(x)
	return(insertionSort(lista))
    
insertionSorts(2)    

