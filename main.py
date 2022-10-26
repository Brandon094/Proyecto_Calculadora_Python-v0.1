from menu import menu

while True:
    salir = input(
        "Si desea continuar digite 1 o Y\nPara salir digite cualquier otra tecla: ").lower()
    if salir == "1" or salir == "y":
        n1 = float(input("\nIngrese 1er numero: "))
        n2 = float(input("Ingrese 2do numero: "))
    else:
        break

    menu(n1, n2)
