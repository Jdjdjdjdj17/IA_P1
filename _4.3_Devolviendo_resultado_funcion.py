def practica_1():
    print("=== 4.3.4: LAB - Un año bisiesto: escribiendo tus propias funciones ===\n")
    print("""Escenario

Tu tarea es escribir y probar una función que toma un argumento (un año) y devuelve True si el año es un año bisiesto, o False si no lo es.\n""")

    def is_year_leap(year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    test_data = [1900, 2000, 2016, 1987]
    test_results = [False, True, True, False]
    for i in range(len(test_data)):
        yr = test_data[i]
        print(yr, "->", end="")
        result = is_year_leap(yr)
        if result == test_results[i]:
            print("OK")
        else:
            print("Fallido")

def practica_2():
    print("=== 4.3.5: LAB - Cuantos dias: escribiendo y usando tus propias funciones ===\n")
    print("""Escenario

Tu tarea es escribir y probar una función que toma dos argumentos (un año y un mes) y devuelve el número de días del mes/año dado.

La función debería devolver None si los argumentos no tienen sentido.\n""")

    def is_year_leap(year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    def days_in_month(year, month):
        if year < 1 or month < 1 or month > 12:
            return None
        dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and is_year_leap(year):
            return 29
        return dias[month - 1]

    test_years = [1900, 2000, 2016, 1987]
    test_months = [2, 2, 1, 11]
    test_results = [28, 29, 31, 30]
    for i in range(len(test_years)):
        yr = test_years[i]
        mo = test_months[i]
        print(yr, mo, "->", end="")
        result = days_in_month(yr, mo)
        if result == test_results[i]:
            print("OK")
        else:
            print("Fallido")

def practica_3():
    print("=== 4.3.6: LAB - Dia del año: escribiendo y usando tus propias funciones ===\n")
    print("""Escenario

Tu tarea es escribir y probar una función que toma tres argumentos (un año, un mes y un día del mes) y devuelve el día correspondiente del año, o devuelve None si cualquiera de los argumentos no es válido.\n""")

    def is_year_leap(year):
        if year % 4 != 0:
            return False
        elif year % 100 != 0:
            return True
        elif year % 400 != 0:
            return False
        else:
            return True

    def days_in_month(year, month):
        if year < 1 or month < 1 or month > 12:
            return None
        dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and is_year_leap(year):
            return 29
        return dias[month - 1]

    def day_of_year(year, month, day):
        if year < 1 or month < 1 or month > 12 or day < 1:
            return None
        dias_en_mes = days_in_month(year, month)
        if day > dias_en_mes:
            return None
        dia_del_año = 0
        for m in range(1, month):
            dia_del_año += days_in_month(year, m)
        dia_del_año += day
        return dia_del_año

    print(2000, 12, 31, "->", day_of_year(2000, 12, 31))
    print(2000, 1, 1, "->", day_of_year(2000, 1, 1))
    print(2016, 2, 29, "->", day_of_year(2016, 2, 29))
    print(1900, 2, 29, "->", day_of_year(1900, 2, 29))

def practica_4():
    print("=== 4.3.7: LAB - Numeros primos: como encontrarlos ===\n")
    print("""Escenario

Un número natural es primo si es mayor que 1 y no tiene divisores más que 1 y si mismo.

Tu tarea es escribir una función que verifique si un número es primo o no.

La función:
    * se llama is_prime
    * toma un argumento (el valor a verificar)
    * devuelve True si el argumento es un número primo, y False de lo contrario.\n""")

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    for i in range(1, 20):
        if is_prime(i + 1):
            print(i + 1, end=" ")
    print()

def practica_5():
    print("=== 4.3.8: LAB - Conversion del consumo de combustible ===\n")
    print("""Escenario

El consumo de combustible de un automóvil se puede expresar de muchas maneras diferentes. En Europa se muestra como la cantidad de combustible consumido por cada 100 kilómetros. En los EE. UU., se muestra como la cantidad de millas recorridas por un automóvil con un galón de combustible.

Tu tarea es escribir un par de funciones que conviertan l/100km a mpg y viceversa.

Datos utiles:
    * 1 milla = 1609.344 metros
    * 1 galon = 3.785411784 litros\n""")

    def liters_100km_to_miles_gallon(liters):
        miles_per_km = 1 / 1.609344
        gallons_per_liter = 1 / 3.785411784
        return (100 * miles_per_km) / (liters * gallons_per_liter)

    def miles_gallon_to_liters_100km(miles):
        km_per_mile = 1.609344
        liters_per_gallon = 3.785411784
        return (100 * liters_per_gallon) / (miles * km_per_mile)

    print(liters_100km_to_miles_gallon(3.9))
    print(liters_100km_to_miles_gallon(7.5))
    print(liters_100km_to_miles_gallon(10.))
    print(miles_gallon_to_liters_100km(60.3))
    print(miles_gallon_to_liters_100km(31.4))
    print(miles_gallon_to_liters_100km(23.5))

while True:
    print("\n===== 4.3 Funciones =====")
    print("1. 4.3.4 - LAB - Un año bisiesto")
    print("2. 4.3.5 - LAB - Cuantos dias en el mes")
    print("3. 4.3.6 - LAB - Dia del año")
    print("4. 4.3.7 - LAB - Numeros primos")
    print("5. 4.3.8 - LAB - Conversion del consumo de combustible")
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
    elif opcion == "0":
        print("Hasta luego!")
        break
    else:
        print("Opcion no valida, intenta de nuevo.")
