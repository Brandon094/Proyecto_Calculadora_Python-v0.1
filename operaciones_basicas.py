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
    print(res)


def modu(num1, num2):
    res = num1 % num2
    print(int(res))


def expo1(num1):
    n = int(input(f"Digite el valor al que desea exponenciar {int(num1)}: "))

    num1 = num1**n
    print(int(num1))


def expo2(num2):
    n = int(input(f"Digite el valor al que desea exponenciar {int(num2)}: "))

    num2 = num2**n
    print(int(num2))


def expo(num1, num2):
    n = int(input(f"Digite el valor al que desea exponenciar {int(num1)} y {int(num2)}: "))

    num1 = num1**n
    num2 = num2**n
    print(int(num1), int(num2))


def raiz1(num1):
    pass


def raiz2(num2):
    pass


def raiz(num1, num2):
    pass


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
