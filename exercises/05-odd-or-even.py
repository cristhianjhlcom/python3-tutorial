## Es par o impar 🤔
## Nivel Fácil
# Escribe un programa que determine si un número dado es par o impar.
## TODOS
# Si el numero del usuario es par:
#   Imprimir "El número entregado es PAR"
# Si no:
#   Imprimir "El número entregado es IMPAR"
## Tips
# 1. Un número es PAR si es divisible por 2 sin dejar residuo.
# 2. Un número es IMPAR si no es divisible por 2 sin dejar un residuo.
# 3. Puedes usar el operador modulo para realizar esto.
def is_odd_or_even(number):
    if number % 2 == 0:
        print("El número entregado es PAR")
    else:
        print("El número entregado es IMPAR")


user_number = int(input("Cuál número quieres verificar? "))
is_odd_or_even(user_number)
