def practica_1():
    print("=== 3.6.6: LAB - Operaciones con listas: conceptos basicos ===\n")
    print("""Escenario

Imagina una lista - no muy larga ni muy complicada, solo una lista simple que contiene algunos números enteros. Algunos de estos números pueden estar repetidos, y esta es la clave. No queremos ninguna repetición. Queremos que sean eliminados.

Tu tarea es escribir un programa que elimine todas las repeticiones de números de la lista. El objetivo es tener una lista en la que todos los números aparezcan no más de una vez.\n""")

    lista = [1, 2, 4, 4, 1, 4, 2, 6, 6, 8]
    print("Lista original:", lista)

    lista_sin_repetidos = []
    for numero in lista:
        if numero not in lista_sin_repetidos:
            lista_sin_repetidos.append(numero)

    print("Lista sin repetidos:", lista_sin_repetidos)

while True:
    print("\n===== 3.6 Operaciones con listas =====")
    print("1. 3.6.6 - LAB - Operaciones con listas: conceptos basicos")
    print("0. Salir")

    opcion = input("\nElige una opcion: ")

    if opcion == "1":
        practica_1()
    elif opcion == "0":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
