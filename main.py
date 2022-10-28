from menu import menu

while True:
    salir = input(
        "Si desea continuar digite 1 o Y\nPara salir digite cualquier otra tecla: ").lower()
    if salir == "1" or salir == "y":
        menu()
    else:
        break

