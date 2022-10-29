from math import *

lP = ["1-Suma: +", "2-Resta: -", "3-Multiplicacion: * ",
      "4-Divicion: /", "5-Division Entera: //", "6-Modulo(residuo): %", "7-Elevar(exponenciar): **", "8-Raiz cuadrada: √", "9-Todas: T", "10-Salir: S"]

lN = ["1-1er numero", "2-2do numero", "3-Ambos"]

# Funcion para imprimir el contenido de cada una de las listas


def listas(lista):
    for i in lista:
        print(i)

# Funcion suma


def adi(num1, num2):
    res = num1 + num2
    return int(res)

# Funcion resta


def res(num1, num2):
    res = num1 - num2
    return int(res)

# Funcion multiplicacion


def multi(num1, num2):
    res = num1 * num2
    return int(res)

# Funcion divicion


def div(num1, num2):
    if num1 == 0 or num2 == 0:
        print("No se puede dividir entre cero.\n")
    else:
        res = num1 / num2
        return round(res, 2)

# Funcion divicion entera


def divE(num1, num2):
    if num1 == 0 or num2 == 0:
        print("No se puede dividir entre cero.\n")
    else:
        res = num1 // num2
        return int(res)

# funcion de modulo(residuo)


def modu(num1, num2):
    res = num1 % num2
    return int(res)

# Funcion exponeciar 1er numero


def expo1(num1):
    n = int(input(f"Digite el valor al que desea exponenciar {int(num1)}: "))

    res = num1**n
    return int(res)

# Funcion exponeciar 2do numero


def expo2(num2):
    n = int(input(f"Digite el valor al que desea exponenciar {int(num2)}: "))

    res = num2**n
    return int(res)


# Funcion exponeciar ambos numeros


def expo(num1, num2):
    n = int(
        input(f"Digite el valor al que desea exponenciar {int(num1)} y {int(num2)}: "))

    res1 = num1**n
    res2 = num2**n
    return int(res1), int(res2)

# Funcion raiz 1er numero


def raiz1(num1):
    res = sqrt(num1)

    return int(res)


# Funcion raiz 1er numero


def raiz2(num2):
    res = sqrt(num2)

    return int(res)

# Funcion raiz amnbos numeros


def raizT(num1, num2):
    res1 = sqrt(num1)
    res2 = sqrt(num2)

    return int(res1), int(res2)


# Funcion para Mostrar todas las operacionnes


def todas(num1, num2):
    print(
        f"El resultado de  {lP[0:1:1]} de {int(num1)} y {int(num2)} es: {adi(num1, num2)}")
    print(
        f"El resultado de  {lP[1:2:1]} de {int(num1)} y {int(num2)} es: {res(num1,num2)}")
    print(
        f"El resultado de  {lP[2:3:1]} de {int(num1)} y {int(num2)} es: {multi(num1,num2)}")
    print(
        f"El resultado de  {lP[3:4:1]} de {int(num1)} y {int(num2)} es: {div(num1,num2)}")
    print(
        f"El resultado de  {lP[4:5:1]} de {int(num1)} y {int(num2)} es: {divE(num1,num2)}")
    print(
        f"El resultado de  {lP[5:6:1]} de {int(num1)} y {int(num2)} es: {modu(num1,num2)}")
    print(
        f"El resultado de  {lP[6:7:1]} de {int(num1)} es: {expo1(num1)}")
    print(
        f"El resultado de  {lP[6:7:1]} de {int(num2)} es: {expo1(num2)}")
    print(
        f"El resultado de  {lP[6:7:1]} de {int(num1)} y {int(num2)} es: {expo(num1,num2)}")
    print(
        f"El resultado de  {lP[7:8:1]} de {int(num1)} es: {raiz1(num1)}")
    print(
        f"El resultado de  {lP[7:8:1]} de {int(num2)} es: {raiz2(num2)}")
    print(
        f"El resultado de  {lP[7:8:1]} de {int(num1)} y {int(num2)} es: {raizT(num1,num2)}")
