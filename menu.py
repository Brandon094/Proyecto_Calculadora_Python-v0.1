from operaciones_basicas import adi, res, multi, div, divE, modu, expo, expo1, expo2, raiz1, raiz2, raizT, todas

listOperaciones = ["1-Suma: + ", "2-Resta: -", "3-Multiplicacion: * ",
                   "4-Divicion: /", "5-Division Entera: //", "6-Modulo(residuo): %", "7-Elevar(exponenciar): **", "8-Raiz cuadrada: √", "9-Todas: T", "10-Salir: S"]

listSelecionarNum = ["1:1er numero", "2:2do numero", "3:Ambos"]


def listas(lista):
    for i in lista:
        print(i)


def menu(num1, num2):
    print("\nselecione la operacion deseada:\n")

    for i in listOperaciones:
        print(i)

    operacion = input("\nselecione: ").lower()
    if operacion == "1" or operacion == "+":
        adi(num1, num2)

    elif operacion == "2" or operacion == "-":
        res(num1, num2)

    elif operacion == "3" or operacion == "*":
        multi(num1, num2)

    elif operacion == "4" or operacion == "/":
        div(num1, num2)

    elif operacion == "5" or operacion == "//":
        divE(num1, num2)

    elif operacion == "6" or operacion == "%":
        modu(num1, num2)

    elif operacion == "7" or operacion == "**":
        listas(listSelecionarNum)
        elevar = input("\nSelecione numero a elevar: ")

        if elevar == "1":
            expo1(num1)
        elif elevar == "2":
            expo2(num2)
        elif elevar == "3":
            expo(num1, num2)
        else:
            print("¡¡Error!! seleccion invalida")

    elif operacion == "8" or operacion == "√":
        listas(listSelecionarNum)
        raiz = input("\nSelecione numero para hallar la raiz cuadrada: ")

        if raiz == "1":
            raiz1(num1)
        elif raiz == "2":
            raiz2(num2)
        elif raiz == "3":
            raizT(num1, num2)
        else:
            print("¡¡Error!! seleccion invalida")

    elif operacion == "9" or operacion == "t":
        todas(num1, num2)

    elif operacion == "10" or operacion == "s":
        print("Hasta la proxima")
        quit()

    else:
        print("¡¡Error!! opcion invalida")
