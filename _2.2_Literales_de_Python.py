def practica_1():
    print("=== 2.2.6: Literales de Python ===\n")
    print("Escriba un fragmento de código de una línea, utilizando la función print(), así como los caracteres de nuevalínea y de escape, para que coincida con el resultado esperado que se muestra en la salida.")
    print("\"Estoy\"\n\"\"aprendiendo\"\"\n\"\"\"Python\"\"\"\n")

def practica_2():
    print("=== 2.2.8: Cuestionario de seccion ===\n")
    print("Pregunta 1: ¿Qué tipos de literales son los siguientes dos ejemplos?")
    print('"Hola ", "007"')
    print("Son cadenas\n")

    print("Pregunta 2: ¿Qué tipos de literales son los siguientes cuatro ejemplos?")
    print('"1.5", 2.0, 528, False')
    print("El prmero es cadena, el segundo es flotante, el tercero es entero y el cuarto es booleano\n")

    print("Pregunta 3: ¿Cuál es el valor decimal del siguiente número binario?")
    print(1011)
    print("Es 11 ;)\n")

while True:
    print("\n===== 2.2 Literales de Python =====")
    print("1. 2.2.6 - Literales de Python (ejercicio)")
    print("2. 2.2.8 - Cuestionario de seccion")
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
