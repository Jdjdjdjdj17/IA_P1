def practica_1():
    print("=== 3.4.6: Los fundamentos de las listas ===\n")
    print("""Escenario

Había una vez un sombrero. El sombrero no contenía conejo, sino una lista de cinco números: 1, 2, 3, 4, y 5.

Tu tarea es:

    escribir una línea de código que solicite al usuario que reemplace el número central en la lista con un número entero ingresado por el usuario (Paso 1)
    escribir una línea de código que elimine el último elemento de la lista (Paso 2)
    escribir una línea de código que imprima la longitud de la lista existente (Paso 3).""")

    lista = [1,2,3,4,5]
    print(lista)
    lista[2] = int(input("Se rempaza el elemento central con: "))
    print(lista)
    del lista[-1]
    print(lista, "se elimina el ultimo elemento de la lista")
    print(lista)
    print("Longitud de la lista: ",len(lista))

def practica_2():
    print("=== 3.4.11: Fundamentos de las listas - Los Beatles ===\n")
    print("""Escenario

Los Beatles fueron uno de los grupos de música más populares de la década de 1960 y la banda más vendida en la historia. Algunas personas los consideran el acto más influyente de la era del rock. De hecho, se incluyeron en la compilación de la revista Time de las 100 personas más influyentes del siglo XX.

La banda sufrió muchos cambios de formación, que culminaron en 1962 con la formación de John Lennon, Paul McCartney, George Harrison y Richard Starkey (mejor conocido como Ringo Starr).

Escribe un programa que refleje estos cambios y le permita practicar con el concepto de listas. Tu tarea es:

    paso 1: crea una lista vacía llamada beatles;
    paso 2: emplea el método append() para agregar los siguientes miembros de la banda a la lista: John Lennon, Paul McCartney y George Harrison;
    paso 3: emplea el bucle for y el append() para pedirle al usuario que agregue los siguientes miembros de la banda a la lista: Stu Sutcliffe, y Pete Best;
    paso 4: usa la instrucción del para eliminar a Stu Sutcliffe y Pete Best de la lista;
    paso 5: usa el método insert() para agregar a Ringo Starr al principio de la lista.\n""")

    # paso 1
    beatles = []
    print("Paso 1:", beatles)

    # paso 2
    beatles.append("Jhon Lennon")
    beatles.append("Paul McCartney")
    beatles.append("George Harrison")
    print("Paso 2:", beatles)

    # paso 3
    i = 0
    for i in range(2):
        str = input("Introduce los miembros que faltan: ")
        beatles.append(str)
    print("Paso 3:", beatles)

    # paso 4
    del beatles[-1]
    del beatles[-1]
    print("Paso 4:", beatles)

    # paso 5
    beatles.insert(0, "Ringo Starr")
    print("Paso 5:", beatles)

    print("Los Fav", len(beatles))

while True:
    print("\n===== 3.4 Listas =====")
    print("1. 3.4.6  - Los fundamentos de las listas")
    print("2. 3.4.11 - Fundamentos de las listas - Los Beatles")
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
