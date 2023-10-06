## Magic Ball Game 🎱
## Nivel Fácil
## Que hacer
# Crea las siguientes variables 📦
# Asigna el valor que corresponde.
# Tu nombre.
# Pregunta que quieres hacer.
# Respuesta. (Iniciar como un string vacio)
# Número aleatorio.
# Para generar un número aleatorio del 1 al 9 puedes usar el modulo random de python.
# Puedes encontrar más información aquí.
# https://www.w3schools.com/python/ref_random_randint.asp
# Para este paso debe usar tus conocimientos en estructuras de control.
# Dependiendo el valor almacenado en la variable "respuesta".
# Va a depender del número generado aleatoriamente.
# Si el número es 1 almacena "Si - Definitivamente"
# Si el número es 2 almacena "Es decididamente así"
# Si el número es 3 almacena "Sin ninguna duda"
# Si el número es 4 almacena "Respuesta confusa, intenta otra vez"
# Si el número es 5 almacena "Pregunta de nuevo más tarde"
# Si el número es 6 almacena "Mejor no decirte ahora"
# Si el número es 7 almacena "Mis fuentes dicen que no"
# Si el número es 8 almacena "No es una vista muy prometedora"
# Si el número es 9 almacena "Muy cuestionable"
# Si no es ninguno almacena "Error"
# Imprime algo con este formato "[nombre] asks: [pregunta]"
# Imprime algo con este formato "La bola mágica 8 🎱 responde: [respuesta]"
import random

user_name = input("Cuál es tu nombre? ")
user_question = input("Que te gustaria preguntarle a la bola mágica? ")
asnwer = ""
random_number = random.randint(1, 9)

if random_number == 1:
    answer = "Si - Definitivamente"
elif random_number == 2:
    answer = "Es decididamente así"
elif random_number == 3:
    answer = "Sin ninguna duda"
elif random_number == 4:
    answer = "Respuesta confusa, intenta otra vez"
elif random_number == 5:
    answer = "Pregunta de nuevo más tarde"
elif random_number == 6:
    answer = "Mejor no decirte ahora"
elif random_number == 7:
    answer = "Mis fuentes dicen que no"
elif random_number == 8:
    answer = "No es una vista muy prometedora"
elif random_number == 9:
    answer = "Muy cuestionable"
else:
    answer = "Error: número aleatorio incorrecto"

print(f"{user_name} asks: {user_question}")
print(f"La bola mágica 8 🎱 responde: {answer}")
