#Pide al usuario un número y lo regresa.
def obtenerValorAConvertir():
    numero = input("Escribe el numero a convertir: ")
    return numero
    
#__________________________Ejercicio: Decimal a Octal______________________

#Pasa un número de decimal a octal
def decimalOctal(a): 

	numero,residuo = 0, 0
	lista = []
	numero = int(input("Escribe un numero (DecimalaOctal): "))
	#Tomamos los residuos y los elevamos a base 10 para poder mostrarlos en pantalla como enteros.
	while(numero!=0):
		residuo = numero%8
		lista.append(residuo)
		numero = int(numero/8)
	for i in range(0,len(lista)):
		numero = numero+ (lista[i]*10**i)
	print(numero)
	return numero
#_________________________Ejercicio: Octal a Decimal_______________________

#Pasa un número de octal a decimal
def octalDecimal(a):

    #Tomamos el número dado, si es None, mandamos a llamar a la funcion
    #obtenerValorAConvertir() para pedir al usuario dicho número. 
    if(a==None):
        print("\nOctal a decimal")
        numero = float(obtenerValorAConvertir())
    else:
        numero = a 
          
    #Sacamos la parte entera y fraccionaria del número. 
    numeroint = int(numero)
    numeroresiduo = numero - numeroint

    #Variable la cual tendrá el valor final del número en base diez.
    numeroDecimal = 0

    #Aquí guardaremos los valores de la parte entera y fraccionaria.
    lista = []

    #Para conocer si el usuario registro un numero fuera de rango.
    x = 0 
    
    #Caso donde el número es igual a cero.
    if(numero == 0 or 0.0):
        print("Decimal: "+str(numero))

    #Sacamos los valores obtenidos de la parte entera y los guardamos en lista.  
    while(numeroint!=0):
        residuo = int(numeroint/10)
        numeroint = (numeroint/10)-int(numeroint/10)
        
        #Para conocer si el número está fuera de rango.
        if((numeroint*10)>=8):
            print("Ingresa un numero valido")
            numeroint= 0
            x = 1
            break
        
        lista.append(round(numeroint*10))
        if(residuo>=1):
             numeroint = residuo 
        else:
            numeroint = 0  
    
    #Para conocer la potencia más alta y poder después pasar la lista a un número.            
    longitudEntera = len(lista)
    
    #Sacamos los valores obtenidos de la parte fraccionaria y los guardamos en lista.  
    while(numeroresiduo!=0):
        numeroresiduo*=10
        numeroint = int(numeroresiduo)
        lista.insert(0,numeroint) 
        if(numeroresiduo==0):
            numeroresiduo = 0
        else:
            numeroresiduo-=numeroint 
    
    #Para mostrar el valor como un número y no como una lista.   
    for i in range(0,len(lista)):
         numeroDecimal = numeroDecimal + int(lista[i])*(8**(longitudEntera-(len(lista)-i)))
    
    #Esto en caso de requerir que nos regrese el valor pero no lo imprima.         
    if(x==1):
        print("Fuera de rango")
        return False
    if(a==None):
        print("El numero en decimal es: " + str(numeroDecimal))
    else:    
        return(numeroDecimal)

        




#___________________________Ejercicio: Octal a Hexadecimal_________________

#Pasa un número de octal a hexadecimal
def octalHexadecimal(a):
    numero = input("Escribe el numero a convertir(Octal a Hexadecimal): ")
    
#_______________________Ejercicio: Hexadecimal a Octal_____________________

#Pasa un numero de base 16 a base 8.
def hexadecimalOctal(a):
     #Pedimos el numero al usuario y lo leemos como una cadena.
    print("\nHexadecimal a Octal")  
    numero = input("Escribe el número a convertir(hexadecimalOctal): ") 
     
    #Variable la cual mandaremos a la funcion decimalOctal().
    numeroDecimal = 0  
     
    #Creamos una cadena separando los caracteres del numero pedido.
    lista = list(numero)


    for i in range(0,len(lista)):
        #Cambiamos los valores por numeros.
        if(lista[i] == "A"):
            lista[i] = 10
        elif(lista[i] == "B"):
            lista[i] = 11
        elif(lista[i] == "C"):
            lista[i] = 12
        elif(lista[i] == "D"):
            lista[i] = 13
        elif(lista[i] == "E"):
            lista[i] = 14
        elif(lista[i] == "F"):
            lista[i] = 15
        else:
            lista[i] = int(lista[i])
    lista.reverse() 
    #Pasamos la lista a base diez.
    for i in range(0,len(lista)):
        numeroDecimal = numeroDecimal + (lista[i]*(16**i))
    listas = []
    while(numeroDecimal!=0):
        residuo = numeroDecimal%8
        listas.append(residuo)
        numeroDecimal = int(numeroDecimal/8)
    for i in range(0,len(lista)):
        numeroDecimal = numeroDecimal+ (listas[i]*10**i)
    print(numeroDecimal)

#Aqui podemos elegir cual funcion probar      
decimalOctal(None)  
octalDecimal(None) 
octalHexadecimal(None)      
hexadecimalOctal(None)








