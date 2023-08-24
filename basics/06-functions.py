# Python3 - Funciones 🤖
# 1. Una función es un bloque de código que solo se ejecuta cuando se llama.
# 2. Le puedes pasar datos, también conocido como parametros, y ser usada adentro de la función.
# 3. Una función puede retornar data como resultado.

# Se crea una función usando la palabra reservada def para definirla.
def greeting(name = "John", age = 0):
    if age < 18:
        return f"Hello {name}, You are so young!\n"

    return f"Hello buddy how is going?\n"

# Se llama la función por el nombre y con parentesis.
# Si es necesario se le pasa los parametros adentro de los parentesis.
cristhian = greeting(name = "Cristhian", age = 29)
shir0shir0 = greeting("shir0shir0", 30)
lelele = greeting(name = "lelele", age = 16)


# Ejemplo de una función para retirar dinero.
def get_authentication(username, password):
    return username == 'admin' and password == '1234'

def withdrawal(amount, is_authenticated = False):
    money = 100
    if not is_authenticated:
        return f"You are not authorized"

    if amount <= money:
        money -= amount
        print(f"You have {money}$ left")
        return f"Here we go your {amount}$"
    else:
        return f"You cannot withdraw {amount}$"

is_authenticated = get_authentication(username = 'admin', password = '1235')
result = withdrawal(amount=100, is_authenticated=is_authenticated)
print(result)
