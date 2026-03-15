def practica_1():
    # 2.1.5: Trabajando con la funcion print()
    print("¡Hola, mundo!\n\n")

def practica_2():
    # 2.1.12: La funcion print() y sus argumentos
    print(" Programming","Essencials","in",sep="***",end="...")
    print("Python\n\n")

def practica_3():
    # 2.1.13: Dando formato a la salida
    print("COn los menos print que se puedan")
    print("     *\n","   * *\n","  *   *\n"," *     *\n","***   ***\n","  *   *\n","  *   *\n","  *****\n")

    print("El doble de grande pero manteniendo las proporciones")
    print("        *")
    print("       * *")
    print("      *   *")
    print("     *     *")
    print("    *       *")
    print("   *         *")
    print("  *           *")
    print(" *             *")
    print("******     ******")
    print("     *     *")
    print("     *     *")
    print("     *     *")
    print("     *     *")
    print("     *     *")
    print("     *     *")
    print("     *******\n")

    print("Doble flecha")
    print("        *         "*2)
    print("       * *        "*2)
    print("      *   *       "*2)
    print("     *     *      "*2)
    print("    *       *     "*2)
    print("   *         *    "*2)
    print("  *           *   "*2)
    print(" *             *  "*2)
    print("******     ****** "*2)
    print("     *     *      "*2)
    print("     *     *      "*2)
    print("     *     *      "*2)
    print("     *     *      "*2)
    print("     *     *      "*2)
    print("     *     *      "*2)
    print("     *******      "*2,("\n"))

def practica_4():
    # 2.1.15 Cuestionario de seccion
    print("Pregunta 1: Cual es la salida del siguiente programa?")

    print('print("Mi\\nnombre\\nes\\nBond.",end=" ")')
    print("James Bond\n")

    print("La salida es:")
    print("Mi")
    print("nombre")
    print("es")
    print("Bond. James Bond\n")

    print("Pregunta 2: Cual es la salida del siguiente programa?")
    print('print(sep="&", "fish", "chips")\n')
    print("La salida es: &fish&chips")
    print("""La verdadera respuesta: File "main.py", line 1
    print(sep="&", "fish", "chips")
                  ^
SyntaxError: positional argument follows keyword argument\n""")

    print("Pregunta 3: ¿Cuál de las siguientes print() invocaciones de función generarán un SyntaxError?")
    print("""print('Greg\'s book.')
print("'Greg's book.'")
print('"Greg\'s book."')
print("Greg\'s book.")
print('"Greg's book."')""")
    print("El ultimo")

while True:
    print("\n===== 2.1 Uso de print() =====")
    print("1. Hola mundo")
    print("2. Argumentos de print()")
    print("3. Dando formato a la salida")
    print("4. Cuestionario de seccion")
    print("0. Salir")

    opcion = input("\nElige una opcion: ")

    if opcion == "1":
        practica_1()
    elif opcion == "2":
        practica_2()
    elif opcion == "3":
        practica_3()
    elif opcion == "4":
        practica_4()
    elif opcion == "0":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
