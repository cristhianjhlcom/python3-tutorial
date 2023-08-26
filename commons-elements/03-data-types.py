# Python3 - Tipos de Datos 🔡
# En la programación los tipos de datos son un concepto importante.
# Las variables pueden definir diferentes tipos de datos.
# Los primeros tipos de datos que vamos a ver:
# 1. Cadena de caracteres (str)
# 2. Númericos (int, float)
# 3. Booleanos (bool)


# Cadena de Caracteres (strings)
first_name = 'lelele'
last_name = 'Hernandez'
full_name = first_name + " " + last_name

# Algunos Metodos de Cadena de Caracteres.
upper_first_name = first_name.upper() # Transforma todo en mayuscula.
lower_first_name = first_name.lower() # Transforma todo a minuscula.
capitalice_first_name = capitalice(first_name) # Convierte la primera letra en mayuscula.
title_first_name = title(first_name) # Convierte la primera de cada palabra en mayusculas.

# Tipo de Dato Numericos en Python
first_integer = 10 # Número entero
second_integer = 20 # Número entero
negative_integer = -10 # Número entero negativo
first_float = 19.99 # Número flotante positivo
second_float = -19.99 # Número flotante negativo

# los tipos de datos numéricos son fundamentales para realizar cálculos matemáticos y operaciones numéricas.
a = 5
b = 3
suma = a + b
resta = a - b
multiplicacion = a * b
division = a / b

#  los tipos de datos booleanos son True y False,
# que representan los valores de verdadero y falso, respectivamente.
# Los tipos de datos booleanos son fundamentales para controlar el flujo de ejecución en
# programas mediante estructuras de control condicionales.
has_money = False
is_admin = True

# Obteniendo el tipo de dato.
# Se puede obtener el dato de cualquier objecto usando la funcion incorporada type()
type("Cristhian") # Cadena de Caracteres (str)
type(10) # Número Entero (int)
type(10.99) # Número Flotante (float)
type(False) # Booleanos (bool)

# Especificando el tipo de dato de manera manual.
# Si lo deseas puedes especificar el tipo de dato de algún valor usando la función correspondiente.
name = str("Cristhian")
age = int(10)
price = float(10.99)
is_student = bool(True)


# Si intentas sumar un string de "10" + 10 te dara un error de tipo.
# Pero le puedes decir a python a travez de la función int() que es un número.
add = int("20") + 10
int("asdas") # Esto dara un error.
