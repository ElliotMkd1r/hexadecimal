"""

Libreria : Hexadecimal.py
Autor : MKD1R(mkdir)

Libreria hecha para todos los programadores de Python, 
pero en especial para los debugger's.

"""

# Funcion usada por IntToHex()

def invPalabras(str, cifras):
	strInv = ""	

	for i in range(len(str)-1, -1, -cifras):
		strInv += str[i-(cifras-1):i+1]

	return strInv


# Funcion que convierte un decimal a sistema hexadecimal

def intToHex(num):
	num = int(num)
	simb = ['a','b','c','d','e','f']
	hexa = ""
	
	while(num >= 16):
		resd=num % 16
		num //= 16

		if(resd >= 10):
			resd = simb[resd-10]
		hexa += str(resd)

	if(num != 0):
		hexa += str(num)

	hexa = invPalabras(hexa, 1)

	return hexa


# Funcion que convierte un decimal a sistema binario

def intToBin(num):
	num = int(num)
	binario = ""
	
	while(num >= 2):
		binario += str(num % 2)
		num //= 2

	if num == 1:
		binario += '1'

	binario = invPalabras(binario, 1) 

	return binario


# Funcion que convierte un numero binario a sistema decimal

def binToInt(bin):
	bin = str(bin)
	tam = len(bin)
	decimal = 0

	for i in range(0, tam-1):
		tam -= 1
		
		decimal += int(bin[i])*(2**tam)

	return decimal


def binToHex(bin):
	hex = str(bin)

	hex = binToInt(hex)
	hex = intToHex(hex)

	return hex


#Funcion que convierte un hexadecimal a sistema decimal

def hexToInt(hexa):
	decimal = 0
	tam = len(hexa)	
	hexs = ['a', 'b', 'c', 'd', 'e', 'f']
	
	for i in range(0, tam):
		cifra = hexa[i]
		tam -= 1

		try:
			verf = hexs.index(cifra)
		except ValueError:
			verf = -1

		if verf >= 0:
			cifra = 10 + verf

		decimal += int(cifra) * (16**tam)

	return decimal


#Funcion que convierte un hexadecimal a sistema binario

def hexToBin(hexa):
	binario = ""

	binario = hexToInt(hexa)
	binario = intToBin(binario)

	return binario


#Comprobacion de las funciones

"""
if __name__ == "__main__":
	num = input("Introduce un numero binario: ")
	#print("HEXADECIMAL: {}\nBinario: {}".format(intToHex(num), intToBin(num)))
	#print("DECIMAL: {}\nHEXADECIMAL: {}".format(binToInt(num), binToHex(num)))
	#print("DECIMAL: {}\nBinario: {}".format(hexToInt(num), hexToBin(num)))
	#print("Palabra Invertida: {}\n".format(invPalabras(num, 2)))
"""
