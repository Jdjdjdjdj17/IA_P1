def practica_1():
    print("=== 2.3.4: Potencia negativa ===\n")
    print(-2**3,"\n")

def practica_2():
    print("=== 2.3.5: Cuestionario de seccion ===\n")
    print("Pregunta 1: ¿Cuál es la salida del siguiente fragmento de código?")
    print('print((2 ** 4), (2 * 4.), (2 * 4)) ')
    print(16, 8.0, 4,"\n")

    print("Pregunta 2: ¿Cuál es la salida del siguiente fragmento de código?")
    print('print((-2 / 4), (2 / 4), (2 // 4), (-2 // 4))')
    print(-0.5, 0.5, 0, -1,"\n")

    print("Pregunta 3: ¿Cuál es la salida del siguiente fragmento de código?")
    print('print((2 % -4), (2 % 4), (2 ** 3 ** 2))')
    print(-2, 2, 512)

while True:
    print("\n===== 2.3 Operadores de Python =====")
    print("1. 2.3.4 - Potencia negativa")
    print("2. 2.3.5 - Cuestionario de seccion")
    print("0. Salir")

    opcion = input("\nElige una opcion: ")

    if opcion == "1":
        practica_1()
    elif opcion == "2":
        practica_2()
    elif opcion == "0":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
