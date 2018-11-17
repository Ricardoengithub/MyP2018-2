m,n,field = 1,1,0
while(m!= 0 and n!=0): #Salida del programa
    tamaño = input("")
    tamaño = tamaño.split()
    m = int(tamaño[0]) #Obtenemos los datos del tamaño del buscaminas
    n = int(tamaño[1])
    
    if(n<0 or m>100): #Verificacion de dimensiones
        print("dimensiones incorrectas")
        m = 0 
        n = 0
        break    
    
    lista = []
    for i in range(0,m): #Obtenemos los datos del buscaminas y los añadimos a una lista.
        renglon = input("")
        if(len(renglon)> n):
            print("Faltan o sobran datos")
            break
        else:
            lista.append(renglon)
    
    matriz1 = []
    for i in range(0,m): #Creamos la lista de listas que se puede ver como un arreglo bidimensional.
        matriz1.append(list(lista[i]))

    matriz2 = []    
    for i in range(0,m): #Utilizamos un contador para saber cuantas veces aparece un '*' y lo añadimos a una listas
        for j in range(0,n):
            counter = 0
            if (matriz1[i][j]=="*"): #Si el elemento es un '*' lo añade.
                counter = "*"            
            elif(i == 0): #Hacemos todas las verificaciones de los 8 lugares adyacentes dependiendo del lugar donde se encuentre la matriz1[i][j].
                if(j == 0):
                    if(matriz1[1][0]== "*"): #Abajo
                        counter+=1
                    if(matriz1[1][1] == "*"): #Diagonal Derecha Abajo
                        counter+=1
                    if(matriz1[0][1] == "*"): #Derecha
                        counter+=1
                elif(j == n-1):
                    if(matriz1[1][n-1]=="*"): #Abajo
                        counter+=1
                    if (matriz1[1][n-2]=="*"): # Diagonal Izquierda Abajo
                        counter+=1
                    if (matriz1[0][n-2]=="*"): # Izquierda
                        counter+=1
                else:
                    if(matriz1[0][j-1]=="*"): # Izquierda
                        counter+=1
                    if(matriz1[1][j]=="*"): # Abajo
                        counter+=1
                    if(matriz1[0][j+1]=="*"): # Derecha
                        counter+=1
                    if(matriz1[1][j-1]=="*"): #Diagonal Izquierda Abajo
                        counter+=1
                    if(matriz1[1][j+1]=="*"): #Diagonal Derecha Abajo
                        counter+=1
            elif(i==m-1):
                if(j == 0):
                    if(matriz1[m-1][1]=="*"): #Derecha
                        counter+=1
                    if(matriz1[m-2][1]=="*"): #Diagonal Derecha Arriba
                        counter+=1
                    if(matriz1[m-2][0]=="*"): #Arriba
                        counter+=1
                elif(j == n-1):
                    if(matriz1[m-1][n-2]== "*"): #Izquierda
                        counter+=1
                    if(matriz1[m-2][n-2]== "*"): #Diagonal Izquierda Arriba    
                        counter+=1
                    if(matriz1[m-2][n-1]=="*"): #Arriba
                        counter+=1
                else:
                    if(matriz1[m-1][j-1] == "*"): #Izquierda
                        counter+=1       
                    if (matriz1[m-2][j-1]=="*"): #Diagonal Izquierda Arriba
                        counter+=1
                    if(matriz1[m-2][j] == "*"): #Arriba
                        counter+=1
                    if(matriz1[m-2][j+1] == "*"): #Diagonal Derecha Arriba
                        counter+=1
                    if(matriz1[m-1][j+1] == "*"): # Derecha
                        counter+=1
            else:
                if(j == 0):
                    if(matriz1[i-1][0] == "*"): # Arriba
                        counter+=1
                    if(matriz1[i-1][1] =="*"): #Diagonal Derecha Arriba
                        counter+=1
                    if(matriz1[i][1] == "*"): #Derecha
                        counter+=1
                    if(matriz1[i+1][1]=="*"): #Diagonal Derecha Abajo
                        counter+=1
                    if (matriz1[i+1][0] == "*"): #Abajo
                        counter+=1
                elif(j == n-1):
                    if(matriz1[i-1][n-1]=="*"): #Arriba
                        counter+=1
                    if(matriz1[i-1][n-2]=="*"): #Diagonal Izquierda Arriba
                        counter+=1
                    if(matriz1[i][n-2] =="*"): #Izquierda
                        counter+=1
                    if(matriz1[i+1][n-2] == "*"): #Diagonal Izquierda Abajo
                        counter+=1
                    if(matriz1[i+1][n-1] == "*"): #Abajo
                        counter+=1
                else:
                    if(matriz1[i][j+1] == "*"): #Derecha
                        counter+=1
                    if (matriz1[i+1][j+1] == "*"): #Diagonal Derecha Abajo
                        counter+=1
                    if(matriz1[i+1][j]=="*"):#Abajo
                        counter+=1
                    if(matriz1[i+1][j-1]=="*"): # Diagonal Izquierda Abajo
                        counter+=1
                    if(matriz1[i][j-1]=="*"): #Izquierda
                        counter+=1
                    if(matriz1[i-1][j-1]=="*"): #Diagonal Izquierda Arriba
                        counter+=1
                    if(matriz1[i-1][j]=="*"): #Arriba
                        counter+=1
                    if(matriz1[i-1][j+1]=="*"): # Diagonal Arriba Derecha
                        counter+=1
            matriz2.append(str(counter))
            
    field+=1 #Contador de campos.
    s = "".join(matriz2)
    if(n == 0 and m==0):
        break
    else:
        print("\nField #"+str(field)+":")
        while(len(s)!=0): #Para mostrar los valores obtenidos a partir de los datos ingresados por el usuario.
            print(s[0:n])
            s=s[n::]
        print("\n")

