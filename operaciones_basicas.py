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


def matriz(num1, num2):
    fun = adi(num1, num2), res(num1, num2), multi(num1, num2), div(num1, num2), divE(num1, num2), modu(
        num1, num2), expo1(num1), expo2(num2), expo(num1, num2), raiz1(num1), raiz2(num2), raizT(num1, num2)

    matriz = []
    tam_fun = len(fun)
    print("\nMostrando matriz de resultados\n")
    for i in range(0, tam_fun):
        maTemp = []

        for j in range(0, 2):
            maTemp.append(fun[i])
        matriz.append(maTemp)

    # mostrar Matriz
    c = 0
    cc = 1
    for i in range(0, tam_fun):
        for j in range(1):
            print(f"{i+1}:Resultado = {matriz[i][j]}", end="\t")
            c += 1
            cc += 1
        print("\t")


# Funcion para Mostrar todas las operacionnes


def todas(num1, num2):
    matriz(num1, num2)
