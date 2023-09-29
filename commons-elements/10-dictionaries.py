# Dictionaries 📦
# Son usados para almacenar valores en pares de key:value
# Son ordenados, cambiables, y no permiten duplicados.
# Los diccionarios son creando entre llevas y tiene key:values como valores.

# product = {
#     'name': 'Camisa',
#     'price': 19.99,
#     'available': True,
#     'stock': 24,
#     'sizes': ['S', 'M', 'L', 'XL']
# }

# print(product.get('namee'))
# print(product.keys())
# print(product.values())
# print(product.items())
# for key, value in product.items():
#     print(f"La llame es {key} y el valor es {value}")

# product = {
#     'name': 'Camisa',
#     'price': 19.99,
#     'available': True,
#     'stock': 24,
#     'sizes': ['S', 'M', 'L', 'XL']
# }
# product['color'] = 'Red'
# product['price'] = 29.99
# product.update({ 'color': 'Blue' })
# product.update({ 'price': 12.90 })
# product.pop('sizes')
# product.clear()
# print(product)

product = {
    'name': 'Camisa',
    'price': 19.99,
    'available': True,
    'stock': 24,
    'sizes': ['S', 'M', 'L', 'XL'],
    'reviews': [
        {
            'message': 'Muy buen product',
            'review': 4.5,
        },
        {
            'message': 'Muy buen product',
            'review': 4.5,
        },
        {
            'message': 'Muy buen product',
            'review': 4.5,
        }
    ]
}

# for review in product['reviews']:
#     print(review['message'])
#     print(review['review'])

# new_product = product.copy()
# new_product = dict(product)
# print(product)
# print(new_product)

users = {
    'cristhianjhl': {
        'name': 'Cristhian',
        'age': 29,
    },
    'victorlol': {
        'name': 'Victor',
        'age': 23,
    }
}

print(users['victorlol']['age'])
