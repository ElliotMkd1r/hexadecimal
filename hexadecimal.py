#! usr/bin/env python
# -*- coding: utf-8 -*-

"""

Libreria : Hexadecimal.py
Autor : MKD1R(mkdir)

Libreria hecha para todos los programadores de Python, 
pero en especial para los debugger's.

"""

#Funcion para convertir a string los hexadecimales

def convtStr(string):
    nuevoStr = ""
    for i in range(0, len(string), 2):
        temp = hexToInt(string[i:i+2])
        nuevoStr += chr(temp)

    return nuevoStr


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
    
    if num < 0:
        num = -num
        temp = hexToInt((2 ** 4) * 'f')
        hexa = intToHex((num ^ temp) + 1)
        
        return hexa
        
	
    while num >= 16:
        resd=num % 16
        num //= 16
        
        if resd >= 10:
            resd = simb[resd-10]
        hexa += str(resd)

    if num != 0:
        if num > 10:
            num = simb[num-10]
        hexa += str(num)
    
    hexa = invPalabras(hexa, 1)

    return hexa


# Funcion que convierte un decimal a sistema binario

def intToBin(num):
    num = int(num)
    binario = ""
    negativo = 0
    
    if num < 0:
        num = -num
        num = (num ^ binToInt('1' * 32)) + 1
     
    while num >= 2:
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
    negativo = 0
    
    if len(bin) == 32 and bin[0] == '1':
        for i in range(0, 32, 4):
            if '0' in bin[i:i+4]:
                negativo = 1
                break
    
    for i in range(0, tam):
        tam -= 1
		
        decimal += int(bin[i])*(2**tam)

    if negativo:
        decimal = (decimal ^ binToInt('1' * 32)) + 1
        decimal = int('-' + str(decimal))

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
    negativo = 0

    if len(hexa) == 16 and hexa[0] == 'f':
        for i in range(0, 16):
            if hexa[i] != 'f':
                negativo = 1
                break

    
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

    if negativo:
        decimal = (decimal ^ hexToInt('f' * 16)) + 1
        decimal = int('-' + str(decimal))

    return decimal


#Funcion que convierte un hexadecimal a sistema binario

def hexToBin(hexa):
    binario = ""

    binario = hexToInt(hexa)
    binario = intToBin(binario)

    return binario


#Comprobacion de las funciones


if __name__ == "__main__":
    num = input("Introduce un numero : ")
    #print(intToHex(num))
    #print("HEXADECIMAL: {}\nBINARIO: {}".format(intToHex(num), intToBin(num)))
    #print("DECIMAL: {}\nHEXADECIMAL: {}".format(binToInt(num), binToHex(num)))
    print("DECIMAL: {}\nBINARIO: {}".format(hexToInt(num), hexToBin(num)))
    #print("Palabra Invertida: {}\n".format(invPalabras(num, 2)))
    input("\nContinuar?? ....")
