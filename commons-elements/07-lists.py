# Lists 📦

# Es común querer trabajar con una colección de datos.
# En Python las listas es una de las estructuras de datos que esta inscrutado en el lenguaje.
# Nos permite trabajar con una colección de datos de una manera secuencial.
# Son ordenadas
# Son mutables
# Heterogéneas
# my_first_list = []
# my_first_list = list()
# fruits = ['Apples', 'Melon', 'Pineapple']
# person = ['Cristhian', 29, True]

# heros = ['Spiderman', 'Batman', 'Superman', 'Wolverine']
#print(heros)
#print(heros[1:])
# print(heros[0]) # Spiderman
# print(heros[1]) # Batman
# print(heros[2]) # Superman
# print(heros[3]) # Wolverine
# print(heros[4]) # Error

# for hero in heros:
#     print(hero)

# if 'Dr. Strange' in heros:
#     print('Si, Dr. Strange existe')
# else:
#     print('No, no existe')
# heros[-1] = 'Thor'
# heros[1:3] = ['Thor', 'Black Panter']
# heros.append('Thor')
# heros.append('Iron Man')
# heros.insert(1, 'Robin')
# heros.insert(0, 'Hulk')
# heros.extend(villians)

# heros = ['Spiderman', 'Batman', 'Superman', 'Batman', 'Wolverine']
# villians = ['Venom', 'Joker', 'Thanos']
# print(heros)
# heros.clear()
# print(heros.pop(9))
# print(heros)

# Copiando una lista
# lista_1 = ['Gato', 'Perro', 'Cristhian']
# lista_2 = lista_1
# print('antes de modificar')
# print(lista_1)
# print('despues de modificar')
# lista_2.append('Hola')
# print(lista_1)
# print(lista_2)
# original_list = ['Gato', 'Perro']
# copied_list = original_list.copy()
# copied_list = list(original_list)
# copied_list.append('Dragon')
# print(original_list)
# print(copied_list)

# Un poco mas sobre las listas python
# name, age, is_developer = ['Cristhian', 29, True]
# one, two, three, *resto = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(one, two, three, resto)
# for user in users:
#     name, age, is_developer = user
#     print(f"Mi nombre es {name}, tengo {age} de edad.")

# users = [
#     ['Cristhian', 29, True],
#     ['Angelo', 16, False],
#     ['Milagros', 33, True],
# ]
# first_user = users[0][0]
# second_user = users[1][0]
# third_user = users[2][0]
# print(first_user, second_user, third_user)

# List Comprehension
# Nos ofrece una manera corta de crear una lista en base a otra lista.
numbers = [1, 2, 3, 4]
# double_numbers = [
#     # expression
#     number * 2
#     # iterable
#     for number in numbers
#     # condition
# ]
double_numbers = [number * 2 for number in numbers]
# for number in numbers:
#     double_numbers.append(number * 2)

# print(numbers)
# print(double_numbers)

# characters = [
#     ['Spiderman', True],
#     ['Superman', True],
#     ['Thanos', False],
#     ['Capitan America', True],
#     ['Joker', False],
# ]

# villians = [
#     character
#     for character in characters
#     if character[1] == False
# ]

# heros = [
#     character
#     for character in characters
#     if character[1]
# ]

# print(heros)
# print(villians)

# fruits = [
#     'manzana',
#     'pera',
#     'banana',
#     'piña',
#     'pera',
# ]

# new_fruits = [
#     fruit
#     if fruit != 'pera' else 'naranja'
#     for fruit in fruits
# ]

# print(fruits)
# print(new_fruits)

fruits = [
    'manzana',
    'pera',
    'banana',
    'piña',
    'pera',
]
print(fruits)
# print(len(fruits))
# print(fruits.count('pera'))
# print(fruits.count('manzana'))
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
