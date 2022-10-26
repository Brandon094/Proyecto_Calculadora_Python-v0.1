from math import*

def adi(num1, num2):
    res = num1 + num2
    print(int(res))


def res(num1, num2):
    res = num1 - num2
    print(int(res))


def multi(num1, num2):
    res = num1 * num2
    print(int(res))


def div(num1, num2):
    res = num1 / num2
    print(round(res, 2))


def divE(num1, num2):
    res = num1 // num2
    print(int(res))


def modu(num1, num2):
    res = num1 % num2
    print(int(res))


def expo1(num1):
    n = int(input(f"Digite el valor al que desea exponenciar {int(num1)}: "))

    res = num1**n
    print(int(res))


def expo2(num2):
    n = int(input(f"Digite el valor al que desea exponenciar {int(num2)}: "))

    res = num2**n
    print(int(res))


def expo(num1, num2):
    n = int(
        input(f"Digite el valor al que desea exponenciar {int(num1)} y {int(num2)}: "))

    res1 = num1**n
    res2 = num2**n
    print(int(res1), int(res2))


def raiz1(num1):
    res = sqrt(num1)
    print(int(res))


def raiz2(num2):
    res = sqrt(num2)
    print(int(res))


def raizT(num1, num2):
    res1 = sqrt(num1)
    res2 = sqrt(num2)
    
    print(int(res1), int(res2))


def todas(num1, num2):
    adi(num1, num2)
    res(num1, num2)
    multi(num1, num2)
    div(num1, num2)
    divE(num1, num2)
    modu(num1, num2)
    expo(num1, num2)
    expo1(num1)
    expo2(num2)
    raiz1(num1)
    raiz2(num2)
    raizT(num1,num2)
