class FirstClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greeting(self):
        print(f"Hello {self.name} how are you?")

    def say_something(self):
        print("Something!")

    def __repr__(self):
        return f"FirstClass(name={self.name}, age={self.age})"

# first_class = FirstClass("Cristhian", 29)
# second_class = FirstClass("Victor", 15)
# print(first_class)
users = [
    {"name": "Cristhian", "age": 29, "is_admin": True},
    {"name": "Bob", "age": 30, "is_admin": True},
    {"name": "Charlie", "age": 22, "is_admin": False},
    {"name": "David", "age": 28, "is_admin": False},
]

class User:
    def __init__(self, name, age, is_admin):
        self.name = name
        self.age = age
        self.is_admin = is_admin

    def presentation(self):
        message = "I am administrator" if self.is_admin else "I am not administrator"
        return f"Hello my name is {self.name} I am {self.age} years old and {message}"


for user in users:
    person = User(user["name"], user["age"], user["is_admin"])
    print(person.presentation())
