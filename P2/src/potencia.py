def potencia(x,y):
	if (y == 0):
		return 1
	elif (y == 1):
		return x
	else:
		return x * potencia(x,y-1)

def main():

	x = int(input("Escribe x: "))
	y = int(input("Escribe la potencia a la que quieres elevar x: "))

	print(f"La potencida de {x} elevado a {y} es: {potencia(x,y)}")


if __name__ == "__main__":
    main()