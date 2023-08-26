# Python 3 - Operadores 👉🏼
# Los operadores son usado para realizar operaciones en las variables y valores.
# Los operadores que veremos en este nivel son los siguientes:
# 1. Operadores Aritmeticos.
# 2. Operadores de Asignación.
# 3. Operadores de Comparación.
# 4. Operadores Lógicos.

# Operadores Aritmeticos.
# Son usado juntos con los valores numericos para realizar operaciones matematicas comunes.
print(5 + 5) # 10
print(3 - 2) # 1
print(2 * 2) # 4
print(10 / 2) # 5.0
print(10 / 3) # 3.333333
print(10 % 2) # 0
print(10 % 4) # 2
print(2 ** 3) # 2 x 2 x 2 = 8
print(10 // 3) # 3
complex_calculation = (2 + 2) - 3 * 1 / 3
print(complex_calculation)

# Operadores de Asignación.
# Son usados para asignar valores a las variables.
number_1 = 10
number_2 = 20
total = 10
price = 20
total += price
total = total + 40
# total += 40 # Es lo mismo que arriba 🆙
count = 10
count = count - 2
# count -= 2 # Es lo mismo que arriba 🆙

number = 10
number *= 20
number = number * 20

number /= 3
number = number / 3

number **= 2
number //= 10

# Operadores de Comparación.
# Son usado para comparar dos valores.
# Devolviendo un valor booleano.
equal = 10 == 10 # True
equal = 12 == 10 # False
equal = "hola" == "Hola"

not_equal = 12 != 10 # True
not_equal = 10 != 10 # False

is_greater_than = 5 > 4 # True
is_greater_than = 5 > 10 # False
is_lower_than = 5 < 10 # True
is_lower_than = 5 < 3 # False

is_greater_or_equal_than = 5 >= 3 # True
is_greater_or_equal_than = 5 >= 5 # True
is_greater_or_equal_than = 5 >= 10 # False

is_lower_or_equal_than = 5 <= 3 # False
is_lower_or_equal_than = 5 <= 5 # True
is_lower_or_equal_than = 5 <= 10 # True

# Operadores Logicos.
# Son usado para combinar declaraciones condicionales.
age = 29
name = "Cristhian"

is_authorized = age > 18 and name == "Cristhian" # True
is_authorized = age > 40 and name == "Cristhian" # False

has_credit_cart = False
has_money_cash = False

can_pay = has_credit_cart or has_money_cash # False

raining = True
is_raining = not(5 > 3 and 2 == 2) # False
