class ProgramLanguage:
    def __init__(self, name):
        self.name = name
        self.__age = 20

    def __private_method(self):
        print("Private method")

    def say_age(self):
        print(f"the age is {self.__age}")
        self.__private_method()

class Python(ProgramLanguage):
    pass

y = Python("Python")
# print(y.name)
# print(y.__age)
# print(y._ProgramLanguage__age)
# y.say_age()
# y.__private_method()

class Person:
    @staticmethod
    def greeting(name):
        print(f"Hello {name}")

Person.greeting("Cristhian")
