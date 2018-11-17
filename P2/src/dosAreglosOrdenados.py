def insertionSort(lista):
	#Para cada elemento de la lista la rrecoremos hasta encontrar su posición donde es mayor que (i-1) y menor que (i+1)
   for i in range(1,len(lista)):

     lugar = i
     valor = lista[i]

     while lugar>0 and lista[lugar-1]>valor:
         lista[lugar]=lista[lugar-1]
         lugar = lugar-1

     lista[lugar] = valor
   #Regresamos la lista por que la vamos a utilizar en otras funciones
   return(lista)

def dosArreglosOrdenados(array1,array2):
    arrayFinalOrdenado = []
    longitudArray1 = len(array1)
    longitudArray2 = len(array2)
	#Concatenamos las dos listas.
    for i in array1: 
        arrayFinalOrdenado.append(i)
    for i in array2:
        arrayFinalOrdenado.append(i)

	#Ordenamos la lista con insertionSort y la mostramos en pantalla
    return(insertionSort(arrayFinalOrdenado))
    
    
#Verificamos que esten ordenadas las listas
def verificaSiestaOrdenado(lista):
	for i in range (0,len(lista)-1):
		if (lista[i]>lista[i+1]):
			return 0
	return 1	
    
    
    
    
lista, lista2 = [],[]
x = 0
#Tomamos los valores de las listas
while(exit != "s"):
	x = input("Escribe los numeros para el arreglo 1 o presiona s para salir: ")
	if(x == "s"):
		break
	else:
		lista.append(int(x))

while(exit != "s"):
	y = input("Escribe un numero para el arreglo 2 o presiona s para salir: ")
	if(y == "s"):
		break	
	else:
		lista2.append(int(y))

#Verificamos que ambas listas esten ordenadas	
if(verificaSiestaOrdenado(lista)==0 or verificaSiestaOrdenado(lista2)==0):
	print("\nVerifica que los arreglos esten ordenados")
else:
	#Juntamos las dos listas y las ordenamos con insertionSort
	print(dosArreglosOrdenados(lista,lista2))		
