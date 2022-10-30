from operaciones_basicas import adi, res, multi, div, divE, modu, expo, expo1, expo2, raiz1, raiz2, raizT, todas, listas, lP, lN

# Funcion para capturar los numeros


def datos():
    numeros = float(input("Ingrese 1er numero: ")), float(
        input("Ingrese 2do numero: "))

    return numeros

# Funcion de menu


def menu():
    print("\n")

    # llamado a la funcion datos
    num = datos()
    # llamado a la funcion listas
    print("\nselecione la operacion deseada:\n")
    listas(lP)

    # condicionales para validar la operacion a realizar
    operacion = input("\nSelecione: ").lower()

    if operacion == "1" or operacion == "+":
        r = adi(num[0], num[1])
        print(
            f"\nEl resultado de la {lP[0:1:1]} de {num[0]} y {num[1]} es: {r}")

    elif operacion == "2" or operacion == "-":
        r = res(num[0], num[1])
        print(
            f"\nEl resultado de la {lP[1:2:1]} de {num[0]} y {num[1]} es: {r}")

    elif operacion == "3" or operacion == "*":
        r = multi(num[0], num[1])
        print(
            f"\nEl resultado de la {lP[2:3:1]} de {num[0]} y {num[1]} es: {r}")

    elif operacion == "4" or operacion == "/":
        r = div(num[0], num[1])
        print(
            f"\nEl resultado de la {lP[3:4:1]} de {num[0]} y {num[1]} es: {r}")

    elif operacion == "5" or operacion == "//":
        r = divE(num[0], num[1])
        print(
            f"\nEl resultado de la {lP[4:5:1]} de {num[0]} y {num[1]} es: {r}")

    elif operacion == "6" or operacion == "%":
        r = modu(num[0], num[1])
        print(
            f"\nEl resultado de la {lP[5:6:1]} de {num[0]} y {num[1]} es: {r}")

    elif operacion == "7" or operacion == "**":
        listas(lN)
        elevar = input("\nSelecione numero a elevar: ")
        # Condicionales anidados para la selecion de el dato a operar
        if elevar == "1":
            r = expo1(num[0])
            print(
                f"\nEl resultado de la {lP[6:7:1]} de {num[0]} y {num[1]} es: {r}")

        elif elevar == "2":
            r = expo2(num[1])
            print(
                f"\nEl resultado de la {lP[6:7:1]} de {num[0]} y {num[1]} es: {r}")

        elif elevar == "3":
            r = expo(num[0], num[1])
            print(
                f"\nEl resultado de la {lP[6:7:1]} de {num[0]} y {num[1]} es: {r}")

        else:
            print("\n¡¡Error!! seleccion invalida")

    elif operacion == "8" or operacion == "√":
        listas(lN)
        raiz = input("\nSelecione numero para hallar la raiz cuadrada: ")
        # Condicionales anidados para la selecion de el dato a operar
        if raiz == "1":
            r = raiz1(num[0])
            print(
                f"\nEl resultado de la {lP[7:8:1]} de {num[0]} y {num[1]} es: {r}")

        elif raiz == "2":
            r = raiz2(num[1])
            print(
                f"\nEl resultado de la {lP[7:8:1]} de {num[0]} y {num[1]} es: {r}")

        elif raiz == "3":
            r = raizT(num[0], num[1])
            print(
                f"\nEl resultado de la {lP[7:8:1]} de {num[0]} y {num[1]} es: {r}")

        else:
            print("\n¡¡Error!! seleccion invalida")

    elif operacion == "9" or operacion == "t":
        todas(num[0], num[1])

    elif operacion == "10" or operacion == "s":
        print("Hasta la proxima")
        quit()

    else:
        print("¡¡Error!! opcion invalida")
