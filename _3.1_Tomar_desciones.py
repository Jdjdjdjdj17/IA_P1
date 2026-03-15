def practica_1():
    print("=== 3.1.6: Variables - Preguntas y respuestas ===\n")
    print("""Escenario

Usando uno de los operadores de comparación en Python, escribe un programa simple de dos líneas que tome el parámetro n como entrada, que es un entero, e imprime False si n es menor que 100, y True if n es mayor o igual que 100.""")

    n = int(input("Dame un numero y te dire si es mayor que 100: "))

    print("El numero ", n, "es mayor que 100: ", (n>100),"\n")

def practica_2():
    print("=== 3.1.10: Operadores de comparacion y ejecucion condicional ===\n")
    print("""Escenario

Espatifilo, más comúnmente conocida como la planta de Cuna de Moisés o flor de la paz, es una de las plantas para interiores más populares que filtra las toxinas dañinas del aire. Algunas de las toxinas que neutraliza incluyen benceno, formaldehído y amoníaco.

Imagina que tu programa de computadora ama estas plantas. Cada vez que recibe una entrada en forma de la palabra Espatifilo, grite involuntariamente a la consola la siguiente cadena: "¡Espatifilo es la mejor planta de todas!"

Escribe un programa que utilice el concepto de ejecución condicional, tome una cadena como entrada y que:

    imprima el enunciado "Si - ¡El Espatifilo! es la mejor planta de todos los tiempos!" en la pantalla si la cadena ingresada es "ESPATIFILIO" (mayúsculas)
    imprima "No, ¡quiero un gran Espatifilo!" si la cadena ingresada es "espatifilo" (minúsculas)
    imprima "¡Espatifilo!, ¡No [entrada]!" de lo contrario. Nota: [entrada] es la cadena que se toma como entrada.""")

    str = input("Dame el nombre de una flor: ")
    if str == "ESPATIFILIO":
        print("Si, ¡el Espatifilio! es la mejor planta de todos los tiempos!")
    elif str == "espatifilio":
        print("No, ¡quiero un gran Espatifilio!")
    else: print("¡Espatifilio!, ¡No", str + "!\n")

def practica_3():
    print("=== 3.1.11: Fundamentos de la sentencia if-else ===\n")
    print("""Escenario

Érase una vez una tierra de leche y miel - habitada por gente feliz y próspera. La gente pagaba impuestos, por supuesto - su felicidad tenía límites. El impuesto más importante, denominado Impuesto Personal de Ingresos (IPI, para abreviar) tenía que pagarse una vez al año y se evaluó utilizando la siguiente regla:

    si el ingreso del ciudadano no era superior a 85,528 pesos, el impuesto era igual al 18% del ingreso menos 556 pesos y 2 centavos (esta fue la llamada exención fiscal).
    si el ingreso era superior a esta cantidad, el impuesto era igual a 14,839 pesos y 2 centavos, más el 32% del excedente sobre 85,528 pesos.

Tu tarea es escribir una calculadora de impuestos.

    Debe aceptar un valor de punto flotante: el ingreso.
    A continuación, debe imprimir el impuesto calculado, redondeado a pesos totales. Hay una función llamada round() que hará el redondeo por ti - la encontrarás en el código de esqueleto del editor.

Nota: este país feliz nunca devuelve dinero a sus ciudadanos. Si el impuesto calculado es menor que cero, solo significa que no hay impuesto (el impuesto es igual a cero). Ten esto en cuenta durante tus cálculos.""")

    i = float(input("Cuanto es tu ingreso? "))

    if i <= 0 : i = 0
    elif i <= 85528 : i = (i*.18) - 556.2
    else : i = 14859.2 + ((i % 85528) * .32)

    print("El impuesto es de: ", round(i), "\n")

while True:
    print("\n===== 3.1 Tomar decisiones =====")
    print("1. 3.1.6  - Variables - Preguntas y respuestas")
    print("2. 3.1.10 - Operadores de comparacion y ejecucion condicional")
    print("3. 3.1.11 - Fundamentos de la sentencia if-else")
    print("0. Salir")

    opcion = input("\nElige una opcion: ")

    if opcion == "1":
        practica_1()
    elif opcion == "2":
        practica_2()
    elif opcion == "3":
        practica_3()
    elif opcion == "0":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
