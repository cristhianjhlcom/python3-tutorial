from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, hp, mp):
        self.name = name
        self.hp = hp
        self.mp = mp

    @abstractmethod
    def use_skill(self):
        pass

class Warrior(Character):
    def use_skill(self):
        print(f"{self.name} use sword attack.")

class Mage(Character):
    def use_skill(self):
        print(f"{self.name} use fire ball.")

character_1 = Warrior("Milo", 100, 20)
character_2 = Mage("Dr. Strange", 40, 120)

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass

class CreditCard(PaymentMethod):
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner

    def process_payment(self, amount):
        print(f"Procesando pago de {amount} con tarjeta de crédito nro. {self.number} a nombre de {self.owner}")

class WireTransfer(PaymentMethod):
    def __init__(self, account, bank):
        self.account = account
        self.bank = bank

    def process_payment(self, amount):
        print(f"Realizando transferencia de {amount} desde la cuenta {self.account} a travéz del banco {self.bank}")

card = CreditCard(number="1234-5678-9012-1234", owner="John Doe")
transfer = WireTransfer("88-0923-123-233", "Devank")

def process_payment_with_method(method, amount):
    method.process_payment(amount)

process_payment_with_method(card, 1000)
process_payment_with_method(transfer, 20000)
