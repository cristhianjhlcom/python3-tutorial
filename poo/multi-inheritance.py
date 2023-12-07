# Multiple Inheritance.
class Father:
    def __init__(self, eyes):
        self.eyes = eyes

class Mother:
    def __init__(self, hair):
        self.hair = hair

class Son(Father, Mother):
    def __init__(self, eyes, hair):
        Father.__init__(self, eyes)
        Mother.__init__(self, hair)

son = Son("Brow", "Light Brown")
# print(f"""I have {son.eyes} eyes because of my father,
# and I have {son.hair} hair because of my mother""")

# Multilevel Inheritance.
class A:
    def __init__(self, name):
        self.name = name

class B(A):
    def __init__(self, name, age):
        A.__init__(self, name)
        self.age = age

class C(B):
    def __init__(self, name, age, is_admin):
        B.__init__(self, name, age)
        self.is_admin = is_admin

c = C("Cristhian", 29, True)
# print(f"name: {c.name} age: {c.age} is admin: {c.is_admin}")

# Hierarchical Inheritance.
class ProgrammeLanguage:
    def __init__(self, name):
        self.name = name

class Python(ProgrammeLanguage):
    pass

class PHP(ProgrammeLanguage):
    pass

python = Python("Python")
php = PHP("PHP")
# print(python.name)
# print(php.name)

# Hybrid Inheritance.
class P:
    def __init__(self, name):
        self.name = name

    def method(self):
        print("The class P")

class X(P):
    def __init__(self, name, age):
        P.__init__(self, name)
        self.age = age

    def method(self):
        print("The class X")

class Y(P):
    def __init__(self, name, is_admin):
        P.__init__(self, name)
        self.is_admin = is_admin

    def method(self):
        print("The class Y")

class Z(X, Y):
    def __init__(self, name, age):
        X.__init__(self, name, age)
        Y.__init__(self, name, is_admin)

    def method(self):
        super().method()
        print("The Class Z")

# obj = Z("Cristhian", 29, True)
# obj.method()

# Class Composition.
products = [
    {"name": "Camisa", "price": 20},
    {"name": "Zapato", "price": 10},
    {"name": "Pantalon", "price": 50},
]

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Customer:
    def __init__(self, name, address):
        self.name = name
        self.address = address

class Purchase:
    def __init__(self, order, customer):
        self.order = order
        self.customer = customer
        self.products = []

    def add_to_cart(self, product):
        self.products.append(product)

    def get_total(self):
        return sum([product.price for product in self.products])

    def print_order(self):
        print(f"Your order is {self.order}")
        print(f"Name {self.customer.name}")
        print(f"Address {self.customer.address}")
        for product in self.products:
            print(f"Product name {product.name} ${product.price}")
        print(f"Total ${self.get_total()}")

customer_1 = Customer(name="Cristhian", address="Lima")
order_1 = Purchase(order=1, customer=customer_1)

for product in products:
    product_obj = Product(name=product["name"], price=product["price"])
    order_1.add_to_cart(product_obj)

order_1.print_order()
