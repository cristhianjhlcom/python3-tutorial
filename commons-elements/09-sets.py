# Sets 📦
# Permite almacenar multiples elementos en una simple variable.
# Son uno de los 4 tipos de datos incorporados para almacenar colección de datos.
# Son desordenado, no se pueden cambiar, y no tienen indexes.
# Son unchangeable, pero se puede agregar y eliminar elementos.
# Se crean encerrando los elementos con llaves.
# No permite datos duplicados.
others = ['Tecnologias', 'Joyas', 'Correas']
categories = {'Camisas', 'Zapatos', 'Correas'}
# categories = set(('Camisas', 'Correas', 'Zapatos', 'Correas'))
# categories.add('Sombreros')
# categories.update(others)
# categories.remove('Camisa')
# categories.discard('Camisa')
# categories.pop()
# categories.clear()
print(type(categories))

# if 'Camisas' in categories:
#     print('Si hay camisas')

# for category in categories:
#     print(f"La categoria es {category}")
