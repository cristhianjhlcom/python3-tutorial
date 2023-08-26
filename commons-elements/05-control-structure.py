# Python3 - Estructura de Control. ⚠️

# Estructura de Control Selectivas.
# Se usan para crear bifurcaciones en el código para que se vaya por un camino u otro.
# Python soporta las condiciones logicas usual en las matematicas.
# 1. Igualdad a == b
# 2. No igual a != b
# 3. Menos que a < b
# 4. Menos o igual que a <= b
# 5. Mayor que a > b
# 6. Mayor o igual que a >= b

# Se puede almacenar la comparación en una variable para usarlo en una condición.
is_greater_than = 5 > 10 and 1 == 1

# Declaración if más común
if is_greater_than:
    print('Si, es mayor')
else:
    print('No, no es mayor')


# Declarción if con elif para agregar mas condiciones.
if is_greater_than:
    print('Si, es mayor')
elif 3 < 2:
    print('elif si es mayor')
elif 5 == 5:
    print('segundo elif si es mayor')
elif 3 == 3:
    print('tercer elif si es mayor')
else:
    print('No, no es mayor')

# Declaraciones if anidadas.
day = 3
hour = 13

if day == 3:
    if hour < 12:
        print('Es hora de trabajar')
    else:
        print('Es hora de almorzar')
else:
    print('Es fin de semana')

print('Finalizando el código')

# Forma corta de escribir if
# Si solo tienes que ejecutar una declaracion, lo puedes escribir en una linea.
a = 20
b = 10

if a > b: print("a is greater than b")

# Y la forma corta de usar else se puede hacer casi de la misma forma.
# Con la diferencia que el resultado del if se escribe al principio.
print("a is greater") if a > b else print("b is greater")

# Estructuras de Control Repetitivas.
# Las estructuras de control repetitivas permiten automatizar tareas que necesitan ejecutarse varias veces.

# For Loops
# se utiliza para iterar sobre una secuencia (como una lista, tupla o rango)
# y ejecutar un bloque de código para cada elemento en la secuencia.

# Si quieres declara un for si que haga nada puedes usar el pass.
# Si dejas el for vacio te dara error.
for i in "hola":
    pass


for i in range(11):
    if i % 2 != 0:
        print('Es impar')
    else:
        print('Es par')
else:
    print('Termino el bucle foor')


for i in range(1, 11):
    if i == 3:
        break
    print(i)


for i in range(1, 11):
    if i == 3:
        continue
    print(i)


for i in range(1, 11):
    print(f"Valor de la i {i}")
    for j in range(1, 6):
        print(f"Valor de la j {j}")


# Estructuras repetitivas While.
# permite ejecutar un bloque de código mientras una condición sea verdadera.

# While común con else, cuando termina el while.
# count = 0
# while count <= 5:
#     print(count)
#     count += 1
# else:
#     print('fin del bucle while')


# También se puede agregar condiciones if.
# count = 0
# while count <= 10:
#     if count == 3:
#         print('El número es 3')
#     print(count)
#     count = count + 1


# Se puede usar break para detener un while.
# count = 0
# while count <= 10:
#     print(count)
#     if count == 4:
#         break
#     count += 1


# Se puede usar el continue también
count = 0
while count <= 10:
    count += 1
    if count == 5:
        continue
    print(count)
