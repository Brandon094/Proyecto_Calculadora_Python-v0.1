from Menu import menu

while True:
    salir = input(
        "\n--Bienvenido--\nSi desea continuar digite 1 o Y, Para salir digite cualquier otra tecla: ").lower()
    if salir == "1" or salir == "y":
        menu()
    else:
        break
