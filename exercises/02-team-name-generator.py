## Generador del nombre de tu equipo. 🎳
## TODOS
# 1. Crea e imprime un soludo para el programa.
# 2. Preguntale al usuario la ciudad donde nacio.
# 3. Preguntale el nombre de su animal favorito.
# 4. Combina las variables e imprime un mensaje e.g.:
# "Los {animal} de {city}"
## Tips
# Usar el builtin function de python 'input'
# La respuesta del usuario almacenalo en variables.
# Utiliza los formatos de strings para imprimir tu mensaje.
def team_name_generator():
    print("Welcome to The Team Name Generator 🎳")
    city = input("En que ciudad naciste? ")
    animal = input("Cuál es tu animal favorito? ")
    return f"Los {animal} de {city}"


team_name = team_name_generator()
print(team_name)
