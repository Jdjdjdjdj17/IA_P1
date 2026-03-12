# 2.4.7: Variables
print("""Escenario

A continuación una historia:

Érase una vez en la Tierra de las Manzanas, Juan tenía tres manzanas, María tenía cinco manzanas, y Adán tenía seis manzanas. Todos eran muy felices y vivieron por muchísimo tiempo. Fin de la Historia.

Tu tarea es:

    Crear las variables: john, mary, y adam;
    Asignar valores a las variables. El valor debe de ser igual al número de manzanas que cada quien tenía;
    Una vez almacenados los números en las variables, imprimir las variables en una línea, y separar cada una de ellas con una coma;
    Después se debe crear una nueva variable llamada total_apples y se debe igualar a la suma de las tres variables anteriores;
    Imprime el valor almacenado en total_apples en la consola;
    Experimenta con tu código: crea nuevas variables, asigna diferentes valores a ellas, y realiza varias operaciones aritméticas con ellas \(por ejemplo, +, -, *, /, //, etc.\). Intenta poner una cadena con un entero juntos en la misma línea, por ejemplo, \"Número total de manzanas:\" y total_apples.,\n""")

jhon = 3
mary = 5
adam = 6
total_apples = jhon + mary + adam

print(jhon, mary, adam, sep=",")
print(total_apples,"\n")

# 2.4.9: Variables: un convertidor simple
print("""Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, complementa el programa en el editor para que convierta de:

    Millas a kilómetros;
    Kilómetros a millas.

No se debe cambiar el código existente. Escribe tu código en los lugares indicados con ###. Prueba tu programa con los datos que han sido provistos en el código fuente.

Pon mucha atención a lo que esta ocurriendo dentro de la función print(). Analiza como es que se proveen múltiples argumentos para la función, y como es que se muestra el resultado.

Nota que algunos de los argumentos dentro de la función print() son cadenas (por ejemplo, "millas son", y otros son variables (por ejemplo, miles).,\n""")

millas = 7.38
km = 12.25
print(millas, 'millas son', millas*1.61)
print(km, 'kilometros son', km/1.61,"\n")

# 2.4.19: Operadores y expreciones
print("""Escenario

Observa el código en el editor: lee un valor float, lo coloca en una variable llamada x, e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar la siguiente expresión:

3x3 - 2x2 + 3x - 1

El resultado debe ser asignado a y.

Recuerda que la notación algebraica clásica muy seguido omite el operador de multiplicación, aquí se debe de incluir de manera explicita. Nota como se cambia el tipo de dato para asegurarnos de que x es del tipo float.

Mantén tu código limpio y legible, y pruébalo utilizando los datos que han sido proporcionados. No te desanimes por no lograrlo en el primer intento. Se persistente y curioso., \n""")

x = 0
x = float(x)
y = 3* x**3 - 2 * x**2 + 3*x -1
print("y=", y, "\n")

x = 1
x = float(x)
y = 3* x**3 - 2 * x**2 + 3*x -1
print("y=", y, "\n")

x = -1
x = float(x)
y = 3* x**3 - 2 * x**2 + 3*x -1
print("y=", y, "\n")