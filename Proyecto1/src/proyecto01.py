import random
import collections

#Clase carta como especifica los requerimientos del proyecto y que utilizaremos para generar todas las cartas de la baraja.
class Carta:
    def __init__(self,valor,palo,color):
        self.valor = valor  
        self.palo = palo
        self.color = color

    def setValor(valor):
        self.valor = valor
    
    def setPalo(palo):
        self.palo = palo
    
    def setColor(color):
        self.color = color

    def getValor(self):
        return self.valor
        
    def getPalo(self):
        return self.palo

    def getColor(self):
        return self.color
        
    def toString(self):
        return ("Valor: " + str(self.valor) + " Palo: " + self.palo + " Color: " + self.color)
        
        
def verificaGanador(cartasjugadorA,cartasjugadorB):
#Verificamos el ganador comparando dos listas en las cuales veremos cual tiene un True mas al inicio de la lista. Cada True representa si cumple una condicion de jugada y en caso de desempate revisamos los valores que le siguen elemento a elemento. Regresamos i para saber con que jugada ganó cualsea de los dos jugadores.
    lista1 = [cartaAlta(cartasjugadorA), pares(cartasjugadorA), dospares(cartasjugadorA), tercia(cartasjugadorA), escalera(cartasjugadorA), mismoColor(cartasjugadorA), fullHouse(cartasjugadorA), cuarta(cartasjugadorA), escaleraColor(cartasjugadorA), florImperial(cartasjugadorA)]
    lista2 = [cartaAlta(cartasjugadorB), pares(cartasjugadorB), dospares(cartasjugadorB), tercia(cartasjugadorB), escalera(cartasjugadorB), mismoColor(cartasjugadorB) , fullHouse(cartasjugadorB), cuarta(cartasjugadorB), escaleraColor(cartasjugadorB), florImperial(cartasjugadorB)]
    lista1 = lista1[::-1]
    lista2 = lista2[::-1]
#    print(lista1)
#    print(lista2)
    for i in range(0,len(lista1)):
        if(lista1[i][0] == False and lista2[i][0] == False):
            pass
        elif (lista1[i][0] == True and lista2[i][0] == False):
            return (0,i)
        elif (lista1[i][0] == False and lista2[i][0] == True):
            return (2,i)
        else:
            if(i == 0):
                return (1,i)
            elif (i == 9):
                for k in range(0,5):
                    if(lista1[i][k] == lista2[i][k]):
                        pass
                    elif(lista1[i][k] < lista2[i][k]):
                        return (2,i)
                    else:
                        return (0,i)
                
            else:
                for j in range(1, len(lista1[i])+1):
                    if(lista1[i][j] == lista2[i][j]):
                        pass
                    elif(lista1[i][j] < lista2[i][j]):
                        return (2,i)
                    else:
                        return (0,i)
                return (1,i)
            

def determinaJugada(numero):
#Para imprimir en pantalla con que jugada gano el jugador.
    if(numero == 0): 
        print("Jugada: Royal Flush")
    elif (numero == 1):
        print("Jugada: Straight Flush")
    elif (numero == 2):
        print("Jugada: Four of a kind")
    elif (numero == 3):
        print("Jugada: Full house")
    elif (numero == 4):
        print("Jugada: Flush")
    elif (numero == 5):
        print("Jugada: Straight")
    elif (numero == 6):
        print("Jugada: Three of a kind")
    elif (numero == 7):
        print("Jugada: Two pair")
    elif (numero == 8):
        print("Jugada: One pair")
    else:#(numero == 9):
        print("Jugada: Carta Alta")
        
        
def cartaAlta(cartasjugadorC):
#Regresa el valor de la carta mas alta de la mano del jugador. 
    lista = []
    for i in range(0,5):        
        lista.append(Carta.getValor(cartasjugadorC[i]))
    lista = cambiarLetrasNum(lista)        
    lista = insertionSort(lista) 
    lista = lista[::-1]
    #return(lista[4])
    return(lista)


def pares(cartasjugadorC):
# Vemos si hay un par igual en las cartas de los jugadores y regresamos un True en caso de ser cierto junto a su lista de pares ordena en caso de querer desempatar.
    lista, lista1 = [], []
    for i in range(0,5):
        lista.append(Carta.getValor(cartasjugadorC[i]))
    lista1 = [x for x, y in collections.Counter(lista).items() if y > 1]
    lista1 = cambiarLetrasNum(lista1)
    lista1 = insertionSort(lista1)
    if(len(lista1) >= 1):
        lista = cambiarLetrasNum(lista)
        lista = insertionSort(lista)
        lista = lista[::-1]
        for i in range(0,len(lista)):
            if(lista[i] in lista1):
                pass
            else:
                lista1.append(lista[i])
        lista1.insert(0,True)
        return lista1
    else:
        lista = cambiarLetrasNum(lista)
        lista = insertionSort(lista)
        lista.insert(0,False)
        return lista
 
 
def dospares(cartasjugadorC):
#Vemos si hay dos pares de cartas que se repiten y regresamos un True junto a la lista ordenada de sus pares para desempatar
    lista, lista1 = [], []
    for i in range(0,5):
        lista.append(Carta.getValor(cartasjugadorC[i]))
    lista1 = [x for x, y in collections.Counter(lista).items() if y > 1] 
    lista1 = cambiarLetrasNum(lista1)
    lista1 = insertionSort(lista1)
    lista1 = lista1[::1]
    if(len(lista1) == 2):
        lista = cambiarLetrasNum(lista)
        lista = insertionSort(lista)
        lista = lista[::-1]
        for i in range(0,len(lista)):
            if(lista[i] in lista1):
                pass
            else:
                lista1.append(lista[i])
        lista1.insert(0,True)
        return lista1
    else:
        lista = cambiarLetrasNum(lista)
        lista = insertionSort(lista)
        lista.insert(0,False)
        return lista

      
def tercia(cartasjugadorC):
#Vemos si hay una tercia contando cuantas veces aparecen en la lista de valores, si una rebasa los tres regresa True y el valor que se repite.  
    lista = []
    veces = 0
    for i in range(0,5):
        lista.append(Carta.getValor(cartasjugadorC[i]))   
    for i in (0,5):
        veces = 0
        for y in lista:
            if(lista[i] == y):
                veces+=1
                if(veces == 3):                
                    lista1 = [x for x, y in collections.Counter(lista).items() if y > 1]                                                            
                    lista1.insert(0,True)
                    return lista1
                else:
                    lista = cambiarLetrasNum(lista)
                    lista = insertionSort(lista)
                    lista.insert(0,False)
                    return lista


def insertionSort(lista):
#Para cada elemento de la lista la rrecoremos hasta encontrar su posición donde es mayor que (i-1) y menor que (i+1) y regresamos una lista ordenada.
   for i in range(1,len(lista)):

     lugar = i
     valor = lista[i]

     while lugar>0 and lista[lugar-1]>valor:
         lista[lugar]=lista[lugar-1]
         lugar = lugar-1

     lista[lugar] = valor
   return(lista)


def cambiarLetrasNum(lista):
#Cambiamos cada letra por un 14(as), 11 ,12 o 13 segun sea el caso.
    listaTemp = []
    for i in lista:
        if(i == "As"):
            listaTemp.append(14)
        elif (i == "J"):
            listaTemp.append(11)            
        elif(i == "Q"):
            listaTemp.append(12)       
        elif (i == "K"):
            listaTemp.append(13)            
        else:
            listaTemp.append(i)
    return listaTemp
    
        
def escalera(cartasjugadorC):
#Cambiamos las letras por numeros y con ayuda de insertionSort vemos si la lista esta en forma de escalera.    
    lista, listaTemp, index = [], [], 0
    for i in range(0,5):        
        lista.append(Carta.getValor(cartasjugadorC[i]))
    lista = cambiarLetrasNum(lista)        
    lista = insertionSort(lista)
    listaTemp = lista[::-1]        
    while(len(lista)>1):
        if(lista[index+1] == lista[index] + 1):
            del(lista[index])
        else:
            listaTemp.insert(0,False)
            return listaTemp
    listaTemp.insert(0,True)
    return listaTemp

   
def mismoColor(cartasjugadorC):
#Vemos si las cartas tienen el mismo Palo y en caso de desempatar regresamos los valores ordenados con insertionSort.  
    lista,lista2, index = [],[],0
    for i in range(0,5):
        lista.append(Carta.getPalo(cartasjugadorC[i])) 
        lista2.append(Carta.getValor(cartasjugadorC[i]))
    lista2 = cambiarLetrasNum(lista2)        
    lista2 = insertionSort(lista2)
    lista2 = lista2[::-1]           
    while (len(lista) > 1 ):
        if(lista[index] == lista[index+1]):
            del(lista[index])
        else:
            lista2.insert(0,False)
            return lista2
    lista2.insert(0,True)
    return lista2


def fullHouse(cartasjugadorC):
#Contamos si las cartas tienen una tercia y que los valores de cartas tiene dos valores que se repiten dentro de ella, con esto sabemos que hay una tercia y un par.
    lista = []
    veces = 0
    for i in range(0,5):
        lista.append(Carta.getValor(cartasjugadorC[i]))      
    for i in (0,5):
        veces = 0
        for y in lista:
            if(lista[i] == y):
                veces+=1
                if(veces == 3):                
                    lista1 = [x for x, y in collections.Counter(lista).items() if y > 1] # En esta linea se crea una lista con los valores que se repiten en la mano de los jugadores                                                           
                    lista1 = insertionSort(lista1)
                    if (len(lista1)==2):
                        lista1.insert(0,True)
                        return lista1
                    else:
                        lista = cambiarLetrasNum(lista)
                        lista = insertionSort(lista)
                        lista.insert(0,False)
                        return lista
                else:
                    lista = cambiarLetrasNum(lista)
                    lista = insertionSort(lista)
                    lista.insert(0,False)
                    return lista


def cuarta(cartasjugadorC):
#Verificamos que exista un valor cuatro veces en la lista de valores y regresamos un True junto a este valor para desempatar.
    lista = []
    veces = 0
    for i in range(0,5):
        lista.append(Carta.getValor(cartasjugadorC[i]))
    for i in (0,5):
        for y in lista:
            if(lista[i] == y):
                veces+=1
                if(veces == 4):
                    lista1 = [x for x, y in collections.Counter(lista).items() if y > 1] 
                    lista1.insert(0,True)
                    return lista1
                else:
                    lista = cambiarLetrasNum(lista)
                    lista = insertionSort(lista)
                    lista.insert(0,False)
                    return lista

def escaleraColor(cartasjugadorC):
#Verificamos que las cartas cumplan estar en escalera y tener el mismo palo y regresamos los valores junto a un True en caso de desempatar.
    lista, listaTemp, index, index1 , lista1 = [], [], 0,0,[]
    for i in range(0,5):        
        lista.append(Carta.getValor(cartasjugadorC[i]))
    lista = cambiarLetrasNum(lista)        
    lista = insertionSort(lista)
    listaTemp = lista[::-1]        
    while(len(lista)>1):
        if(lista[index+1] == lista[index] + 1):
            del(lista[index])
        else:
            listaTemp.insert(0,False)
            return listaTemp
            
    for i in range(0,5):
        lista1.append(Carta.getPalo(cartasjugadorC[i]))
    while (len(lista1) > 1 ):
        if(lista1[index1] == lista1[index1+1]):
            del(lista[index1])
        else:
            listaTemp.insert(0,False)
            return listaTemp
    listaTemp.insert(0,True)
    return listaTemp
        

def florImperial(cartasjugadorC):
#Verificamos que tengan el mismo palo las cartas y que la lista de valores sea igual a: [10,11,12,13] donde 14 es el valor de As, cuando cambiamos las letras por numeros y la ordenamos con insertionSort.
    lista, listaTemp, index, index1 , lista1 = [], [], 0,0,[]
    for i in range(0,5):        
        lista.append(Carta.getValor(cartasjugadorC[i]))
    lista = cambiarLetrasNum(lista)        
    lista = insertionSort(lista)
    listaTemp = lista[::-1]        
    while(len(lista)>1):
        if(lista[index+1] == lista[index] + 1):
            del(lista[index])
        else:
            listaTemp.insert(0,False)
            return listaTemp
            
    for i in range(0,5):
        lista1.append(Carta.getPalo(cartasjugadorC[i]))
    while (len(lista1) > 1 ):
        if(lista1[index1] == lista1[index1+1]):
            del(lista[index1])
        else:
            listaTemp.insert(0,False)
            return listaTemp
    for i in range(0,len(listaTemp)):
        if(listaTemp[i] == flor[i]):
            pass
        else:
            listaTemp.insert(0,False)
            return listaTemp
    listaTemp.insert(0,True)
    return listaTemp

                             
def cambiarCarta(cartaACambiar,lugares):
#Guardamos el valor de la carta y regresamos otra verificando que sea distinta a la que el jugador quiere cambiar. 
    carta = lugares[cartaACambiar]
    del(lugares[cartaACambiar])
    while(len(lugares) != 10):
        x = random.randint(0,51)
        if(x in lugares):
            pass
        elif(x == carta):
            pass
        else:
            lugares.insert(cartaACambiar,x)
    return (lugares)

       
def menu():
#Menu de inicio donde preguntamos de que manera se va a jugar     
    print('''       
            ***Poker***
            
            Elige una opcion
            1. Jugar como A y B
            2. Ingresar nombres de jugadores
            3. Salir(Enter)''')
            
    opcion = input('=>')
    return opcion



#Creamos las 52 cartas que utilizaremos en el juego y las clasificamos para obtener los cuatro simbolos de la baraja.               
cartas = []
for i in range (0,52):
    x = i % 13
    if(i <=12):
        if (x == 0):
            cartas.append( Carta('As', chr(27)+"[0;31m"+u'\u2665'+chr(27)+"[0m",'R'))            
        elif(x == 10):
            cartas.append( Carta('J', chr(27)+"[0;31m"+u'\u2665'+chr(27)+"[0m",'R'))
        elif(x == 11):
            cartas.append( Carta('Q', chr(27)+"[0;31m"+u'\u2665'+chr(27)+"[0m",'R'))    
        elif (x == 12 and i != 0):
            cartas.append( Carta('K', chr(27)+"[0;31m"+u'\u2665'+chr(27)+"[0m",'R'))
        else:    
            cartas.append( Carta(x+1, chr(27)+"[0;31m"+u'\u2665'+chr(27)+"[0m",'R'))
    elif (i<=25):
        if (x == 0):
            cartas.append( Carta('As',chr(27)+"[0;30m"+u'\u2660'+chr(27)+"[0m",'N'))        
            
        elif(x == 10):
            cartas.append( Carta('J',chr(27)+"[0;30m"+u'\u2660'+chr(27)+"[0m",'N')) 
        elif (x == 11):
            cartas.append( Carta('Q',chr(27)+"[0;30m"+u'\u2660'+chr(27)+"[0m",'N'))
        elif (x == 12 and i != 0):
            cartas.append( Carta('K',chr(27)+"[0;30m"+u'\u2660'+chr(27)+"[0m",'N'))
        else:
            cartas.append( Carta(x+1,chr(27)+"[0;30m"+u'\u2660'+chr(27)+"[0m",'N'))
    elif(i<=38):
        if(x == 0):
            cartas.append( Carta('As', chr(27)+"[0;30m"+u'\u2663'+chr(27)+"[0m",'N'))            
        elif(x ==10):
            cartas.append( Carta('J', chr(27)+"[0;30m"+u'\u2663'+chr(27)+"[0m",'N'))
        elif(x == 11):
            cartas.append( Carta('Q', chr(27)+"[0;30m"+u'\u2663'+chr(27)+"[0m",'N'))
        elif(x == 12 and i != 0):
            cartas.append( Carta('K', chr(27)+"[0;30m"+u'\u2663'+chr(27)+"[0m",'N'))
        else:
            cartas.append( Carta(x+1, chr(27)+"[0;30m"+u'\u2663'+chr(27)+"[0m",'N'))
    elif(i<=51):
        if(x == 0):
            cartas.append( Carta('As',chr(27)+"[0;31m"+u'\u2666'+chr(27)+"[0m",'R'))        
        elif (x == 10):
                    cartas.append( Carta('J',chr(27)+"[0;31m"+u'\u2666'+chr(27)+"[0m",'R'))
        elif (x == 11):
            cartas.append( Carta('Q',chr(27)+"[0;31m"+u'\u2666'+chr(27)+"[0m",'R'))
        elif (x == 12 and i != 0):
            cartas.append( Carta('K',chr(27)+"[0;31m"+u'\u2666'+chr(27)+"[0m",'R'))
        else:
            cartas.append( Carta(x+1,chr(27)+"[0;31m"+u'\u2666'+chr(27)+"[0m",'R'))

#for i in range(0,52):
#    print(Carta.toString(cartas[i]))        

print("\n")
cartasjugadorA, cartasjugadorB,lugares = [], [], []
#Elegimos 10 numeros aleatorios para "barajar" y obtener las cartas.
while (len(lugares) != 10):
    x = random.randint(0,51)
    if (x in lugares):
        pass
    else:
        lugares.append(x)

#Asignamos las primeras 5 cartas de la lista a el jugador 1 y las restantes al jugador 2.
for i in range(0,len(lugares)):
    if(i<=4):
        cartasjugadorA.append(cartas[lugares[i]])
    else:
        cartasjugadorB.append(cartas[lugares[i]])
         
    
#Desplegamos el menu y preguntamos al usuario de que manera va a jugar y le mostramos sus cartas a cada jugador y si quiere cambiar alguna.     
opcion = menu()           
if(opcion == '1'): 

    print("\nCartas del jugador A: ")             
    for i in range(0,5):
        print(Carta.toString(cartasjugadorA[i]))  
         
    print("\nCartas del jugador B: ")
    for i in range(0,5):
        print(Carta.toString(cartasjugadorB[i])) 
                       
    a = input("\nEl jugador A quiere cambiar una carta... Presione 1-Si 0-No: ")
    b = input("El jugador B quiere cambiar una carta... Presione 1-Si 0-No: ")
    
    #Caso si a quiere cambiar una carta
    if(a == '1'):
        cartasjugadorA, cartasjugadorB = [],[]
        card = int(input("\nQue carta quiere cambiar el jugador A, eliga un numero del 1 al 5: "))
        lugares = cambiarCarta(card-1,lugares)
        for i in range(0,len(lugares)):
            if(i<=4):
                cartasjugadorA.append(cartas[lugares[i]])
            else:
                cartasjugadorB.append(cartas[lugares[i]])                
    else:
        pass
    #Caso si b quiere cambiar una carta        
    if(b == '1'):
        cartasjugadorA,cartasjugadorB = [],[]
        card = int(input("Que carta quiere cambiarel jugador B, eliga un numero del 1 al 5: "))
        lugares = cambiarCarta(card+4,lugares)
        for i in range(0,len(lugares)):
            if(i<=4):
                cartasjugadorA.append(cartas[lugares[i]])
            else:
                cartasjugadorB.append(cartas[lugares[i]])        
    else:
        pass

#Volvemos a mostrar las cartas finales a los dos jugadores por si se ha hecho algun cambio.     
    print("\nCartas del jugador A")
    for i in range(0,5):
       print(Carta.toString(cartasjugadorA[i])) 
    print("\nCartas del jugador B")
    for i in range(0,5):
        print(Carta.toString(cartasjugadorB[i]))   
    print("\n")    
    #Vemos cual de los dos jugadores ganó
    (ganador,jugada) = verificaGanador(cartasjugadorA, cartasjugadorB)
    if (ganador == 0):
        print("\nEl ganador es el jugador A")
    elif (ganador == 1):
        print("\nEmpate")
    else:
        print("\nEl ganador es el jugador B")
    #Imprimimos con que jugada gano el jugador A o B y en empate no imprime nada
    if(ganador == 1):
        pass
    else:
        determinaJugada(jugada)



#Caso donde se ingresan los nombres de los usuarios.    
elif(opcion == '2'):
    jugadorA = input("Nombre del jugador 1: ")
    jugadorB = input("Nombre del jugador 2: ")
    print("\nCartas del jugador "+jugadorA)
    for i in range(0,5):
       print(Carta.toString(cartasjugadorA[i])) 
    print("\nCartas del jugador "+jugadorB)
    for i in range(0,5):
        print(Carta.toString(cartasjugadorB[i]))   
    print("\n")
    
    a = input("\nEl jugador "+jugadorA+" quiere cambiar una carta... Presione 1-Si 0-No: ")
    b = input("El jugador "+jugadorB+" quiere cambiar una carta... Presione 1-Si 0-No: ")

    #Caso si a quiere cambiar una carta
    if(a == '1'):
        cartasjugadorA, cartasjugadorB = [],[]
        card = int(input("\nQue carta quiere cambiar el jugador "+ jugadorA+", eliga un numero del 1 al 5: "))
        lugares = cambiarCarta(card-1,lugares)
        for i in range(0,len(lugares)):
            if(i<=4):
                cartasjugadorA.append(cartas[lugares[i]])
            else:
                cartasjugadorB.append(cartas[lugares[i]])                
    else:
        pass
    #Caso si a quiere cambiar una carta   
    if(b == '1'):
        cartasjugadorA,cartasjugadorB = [],[]
        card = int(input("Que carta quiere cambiar el "+jugadorB+ ", eliga un numero del 1 al 5: "))
        lugares = cambiarCarta(card+4,lugares)
        for i in range(0,len(lugares)):
            if(i<=4):
                cartasjugadorA.append(cartas[lugares[i]])
            else:
                cartasjugadorB.append(cartas[lugares[i]])        
    else:
        pass
    
    print("\nCartas del jugador "+ jugadorA)
    for i in range(0,5):
       print(Carta.toString(cartasjugadorA[i])) 
       
    print("\nCartas del jugador "+ jugadorB)
    for i in range(0,5):
        print(Carta.toString(cartasjugadorB[i]))  
     
    print("\n")    
    #Vemos cual de los dos jugadores ganó
    (ganador,jugada) = verificaGanador(cartasjugadorA, cartasjugadorB)
    if (ganador == 0):
        print("\nEl ganador es: "+ jugadorA)
    elif (ganador == 1):
        print("\nEmpate")
    else:
        print("\nEl ganador es: "+ jugadorB)
    #Imprimimos con que jugada gano
    if(ganador == 1):
        pass
    else:
        determinaJugada(jugada)
