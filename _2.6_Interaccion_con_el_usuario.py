def practica_1():
    print("=== 2.6.9: Entradas y salidas simples ===\n")
    print("""Escenario

Tu tarea es completar el código para evaluar los resultados de cuatro operaciones aritméticas básicas.

Los resultados deben imprimirse en la consola.

Es posible que no puedas proteger el código de un usuario que quiera dividir entre cero. Está bien, no te preocupes por eso por ahora.

Prueba tu código - ¿produce los resultados esperados?

No te mostraremos ningún dato de prueba - eso sería demasiado simple.,\n""")

    a = float(input("Dame un mumero ..."))# ingresa un valor flotante para la variable a aquí
    b = float(input("Dame otro mumero ..."))# ingresa un valor flotante para la variable b aquí

    print(a,"+", b, "=", a+b)# mostrar el resultado de la suma aquí
    print(a,"-", b, "=", a-b)# mostrar el resultado de la resta aquí
    print(a,"x", b, "=", a*b)# mostrar el resultado de la multiplicación aquí
    print(a,"/", b, "=", a/b)# mostrar el resultado de la división aquí

    print("\n¡Eso es todo, amigos!")

def practica_2():
    print("=== 2.6.10: Operadores y expresiones ===\n")
    print("""Escenario

Tu tarea es completar el código para poder evaluar la siguiente expresión: 1/(x+1/(x+1/(x+(1/x))))""")
    x = float(input("Dame un valor para x: "))
    print("y = ", 1/(x+1/(x+1/(x+(1/x)))))

def practica_3():
    print("=== 2.6.11: Operadores y expresiones 2 ===\n")
    print("""Escenario

La tarea es preparar un código simple para evaluar o encontrar el tiempo final de un periodo de tiempo dado, expresándolo en horas y minutos. La hora de inicio se da como un par de horas (0..23) y minutos (0..59). El resultado debe ser mostrado en la consola.

Por ejemplo, si el evento comienza a las 12:17 y dura 59 minutos, terminará a las 13:16.

No te preocupes si tu código no es perfecto - está bien si acepta una hora invalida - lo más importante es que el código produzca una salida correcta acorde a la entrada dada.

Prueba el código cuidadosamente. Pista: utilizar el operador % puede ser clave para el éxito., \n""")

    hora_i = int(input("Hora de inicio del evento(0..23): "))
    min_i = int(input("Minuto de inicio del evento(0..59): "))

    min_d = int(input("Duracion del evento(0..59): "))

    min_total = ((hora_i * 60) + min_i) + min_d

    print("Inicio del evento: ",hora_i, ":", min_i, ". Terminacion del evento: ", min_total//60, ":", (min_total % 60),".")

while True:
    print("\n===== 2.6 Interaccion con el usuario =====")
    print("1. 2.6.9  - Entradas y salidas simples")
    print("2. 2.6.10 - Operadores y expresiones")
    print("3. 2.6.11 - Operadores y expresiones 2")
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
