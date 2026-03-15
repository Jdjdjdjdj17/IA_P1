def practica_1():
    print("=== 2.5.3: Comentarios ===\n")

    #este programa calcula los segundos en cierto número de horas determinadas

    a = 2 # número de horas
    seconds = 3600 # número de segundos en una hora

    print("Horas: ", a) #imprime el numero de horas
    print("Segundos en", a, "horas: ", a * seconds) # se imprime el numero de segundos en a horas

    #este el es fin del programa que calcula el numero de segundos en 2 horas

while True:
    print("\n===== 2.5 Comentarios =====")
    print("1. 2.5.3 - Calculo de segundos en horas")
    print("0. Salir")

    opcion = input("\nElige una opcion: ")

    if opcion == "1":
        practica_1()
    elif opcion == "0":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
