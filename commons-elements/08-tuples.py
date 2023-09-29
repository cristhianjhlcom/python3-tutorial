# Tuples 📦

# Son casi lo mismo que las lista solo que.
# No se pueden cambiar.
# # No se puede agregar elementos
# # No se pueden actualizar los elementos
# # No se puede eliminar elementos
# Se crean encerrando los datos entre parentesis.
# Son más seguros al ser inmutables.
# Son más eficientes.

# my_tuple = ('Cristhian', 29, 'Cristhian', True)
# print(my_tuple)
# name, age, is_developer = my_tuple
# print(name, age, is_developer)
# print(my_tuple[1])
# for item in my_tuple:
#     print(item)
# my_tuple[0] = 'Eric'
# print(len(my_tuple))
# user = tuple(('Cristhian', 29, True))
# print(user)
# users = [
#     ('Edith', 20, False),
#     ('Victor', 45, True),
#     ('Katherin', 24, False)
# ]

# for user in users:
#     print(f"Mi nombre es {user[0]} y tengo {user[1]} años.")
user = ('Edith', 20, False)
print(type(user))
