import time

def practica_1():
    print("=== 3.2.4: Adivina el numero secreto ===\n")
    print("""Escenario
 
Un mago junior ha elegido un número secreto. Lo ha escondido en una variable llamada secret_number. Quiere que todos los que ejecutan su programa jueguen el juego Adivina el número secreto, y adivina qué número ha elegido para ellos. ¡Quiénes no adivinen el número quedarán atrapados en un bucle sin fin para siempre! Desafortunadamente, él no sabe cómo completar el código.

Tu tarea es ayudar al mago a completar el código en el editor de tal manera que el código:

    pedirá al usuario que ingrese un número entero;
    utilizará un bucle while;
    comprobará si el número ingresado por el usuario es el mismo que el número escogido por el mago. Si el número elegido por el usuario es diferente al número secreto del mago, el usuario debería ver el mensaje "¡Ja, ja! ¡Estás atrapado en mi bucle!" y se le solicitará que ingrese un número nuevamente. Si el número ingresado por el usuario coincide con el número escogido por el mago, el número debe imprimirse en la pantalla, y el mago debe decir las siguientes palabras: "¡Bien hecho, muggle! Eres libre ahora."

¡El mago está contando contigo! No lo decepciones.""")

    print("""
+================================+
| ¡Bienvenido a mi juego, muggle!|
| Introduce un número entero     |
| y adivina qué número he        |
| elegido para ti.               |
|¿Cuál es el número secreto?     |
+================================+
""")

    secret_number = 76
    n = int(input("Dame un numero entero: "))

    while n :
        if n == secret_number :
            print("¡Bien hecho, muggle! Eres libre ahora")
            n = 0
        else :
            print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
            n = int(input("Dame un numero entero: "))

def practica_2():
    print("=== 3.2.7: Fundamentos del bucle for ===\n")
    print("""Escenario

¿Sabes lo que es Mississippi? Bueno, es el nombre de uno de los estados y ríos en los Estados Unidos. El río Mississippi tiene aproximadamente 2,340 millas de largo, lo que lo convierte en el segundo río más largo de los Estados Unidos (el más largo es el río Missouri). ¡Es tan largo que una sola gota de agua necesita 90 días para recorrer toda su longitud!

La palabra Mississippi también se usa para un propósito ligeramente diferente: para contar mississippily (mississippimente).

Si no estás familiarizado con la frase, estamos aquí para explicarte lo que significa: se utiliza para contar segundos.

La idea detrás de esto es que agregar la palabra Mississippi a un número al contar los segundos en voz alta hace que suene más cercano al reloj, y por lo tanto "un Mississippi, dos Mississippi, tres Mississippi" tomará aproximadamente unos tres segundos reales de tiempo. A menudo lo usan los niños que juegan al escondite para asegurarse de que el buscador haga un conteo honesto.

Tu tarea es muy simple aquí: escribe un programa que use un bucle for para "contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa debería imprimir en la pantalla el mensaje final ¡Listos o no, ahí voy!\n""")

    for i in range(1, 6):
        print(i, "MIssissippi")
        time.sleep(1)
    print("Lista o no, aqui vengo!")

def practica_3():
    print("=== 3.2.9: La sentencia break - atrapado en un bucle ===\n")
    print("""Escenario

La instrucción break se implementa para salir/terminar un bucle.

Diseña un programa que use un bucle while y le pida continuamente al usuario que ingrese una palabra a menos que ingrese "chupacabra" como la palabra de output secreta, en cuyo caso el mensaje "Has dejado el bucle con éxito." debe imprimirse en la pantalla y el bucle debe terminar.

No imprimas ninguna de las palabras ingresadas por el usuario. Utiliza el concepto de ejecución condicional y la sentencia break.""")

    while True:
        str = input(":")
        if str == "chupacabra":
            print("Has dejado el bucle con éxito.")
            break

def practica_4():
    print("=== 3.2.10: La sentencia continue - el Feo devorador de vocales ===\n")
    print("""Escenario

La sentencia continue se usa para omitir el bloque actual y avanzar a la siguiente iteración, sin ejecutar las sentencias dentro del bucle.

Se puede usar tanto con bucles while y for.

Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales! Escribe un programa que use:

    un bucle for;
    el concepto de ejecución condicional (if-elif-else).
    la sentencia continue.

Tu programa debe:

    pedir al usuario que ingrese una palabra.
    utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario a mayúsculas; hablaremos sobre los llamados métodos de cadena y el método upper() muy pronto, no te preocupes
    utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes vocales A, E, I, O, U de la palabra ingresada.
    imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada""")

    user_word = input(":")
    user_word = user_word.upper()

    for letter in user_word:
        if letter == "A":
            continue
        elif letter == "E":
            continue
        elif letter == "I":
            continue
        if letter == "O":
            continue
        elif letter == "U":
            continue
        else: print(letter)

def practica_5():
    print("=== 3.2.14: Fundamentos del bucle while - La piramide ===\n")
    print("""Escenario

Escucha esta historia: Un niño y su padre, un programador de computadoras, juegan con bloques de madera. Están construyendo una pirámide.

Su pirámide es un poco rara, ya que en realidad es una pared en forma de pirámide - es plana. La pirámide se apila de acuerdo con un principio simple: cada capa inferior contiene un bloque más que la capa superior.

Tu tarea es escribir un programa que lea la cantidad de bloques que tienen los constructores, y generar la altura de la pirámide que se puede construir utilizando estos bloques.

Nota: La altura se mide por el número de capas completas - si los constructores no tienen la cantidad suficiente de bloques y no pueden completar la siguiente capa, terminan su trabajo inmediatamente.""")

    bloques = int(input("Cuantos bloques tienes?: "))
    capa = 1
    altura = 0

    while bloques >= capa:
        bloques -= capa
        capa += 1
        altura += 1

    print("La altura de la piramide es: ", altura)

def practica_6():
    print("=== 3.2.15: LAB - La hipotesis de Collatz ===\n")
    print("""Escenario

En 1937, un matemático alemán llamado Lothar Collatz formuló una hipótesis intrigante (aún no se ha comprobado) que se puede describir de la siguiente manera:

1. toma cualquier número entero que no sea negativo y que no sea cero y asígnale el nombre c0;
2. si es par, evalúa un nuevo c0 como c0 / 2;
3. de lo contrario, si es impar, evalúe un nuevo c0 como 3 x c0 + 1;
4. si c0 != 1, salta al punto 2.

La hipótesis dice que, independientemente del valor inicial de c0, el valor siempre tiende a 1.

Tu código también debe mostrar todos los valores intermedios de c0.\n""")

    c0 = int(input("Dame un numero entero: "))
    pasos = 0
    while c0 != 1:
        if c0 % 2 == 0: c0 = c0 // 2
        else: c0 = 3 * c0 + 1
        pasos += 1
        print(c0)
    print("\nPasos: ", pasos)

while True:
    print("\n===== 3.2 Bucles en Python =====")
    print("1. 3.2.4  - Adivina el numero secreto")
    print("2. 3.2.7  - Fundamentos del bucle for (Mississippi)")
    print("3. 3.2.9  - La sentencia break - atrapado en un bucle")
    print("4. 3.2.10 - La sentencia continue - el Feo devorador de vocales")
    print("5. 3.2.14 - Fundamentos del bucle while - La piramide")
    print("6. 3.2.15 - LAB - La hipotesis de Collatz")
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
    elif opcion == "5":
        practica_5()
    elif opcion == "6":
        practica_6()
    elif opcion == "0":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
