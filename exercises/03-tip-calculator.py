## Calculador de Propina 📲
## Nivel Facil
# 1. Obten el total del consumo.
# 2. Calcula el % de la propina.
# 3. Obten el monto de la propina.
# 4. Suma ambos montos.
# 5. Muestraselo al usuario en pantalla.
## Formula
# propina %: propina / 100
# monto propina: pago * propina %
# total a pagar: propina + monto propina
## Recomendaciones
# Obten la cantidad de propina del usuario.
# Redondea los valores flotantes.

payment_list = [
    {"food": "Burger", "price": 12.50},
    {"food": "Pizza", "price": 15.75},
    {"food": "Salad", "price": 8.20},
    {"food": "Pasta", "price": 10.95},
    {"food": "Soda", "price": 2.50}
]

def get_total_amount(items, key = "price"):
    total = 0
    for item in items:
        total += item[key]
    return round(total, 2)


def get_tip_amount(total, tip = 10):
    tip_as_percentage = tip / 100
    tip_amount = total * tip_as_percentage
    return round(tip_amount, 2)


def show_final_payment():
    print("Bienvenidos a Dev Foods")
    for item in payment_list:
        print("{} - Costo ${}".format(item['food'], item['price']))
    user_tip = int(input("Desea dejar propina? 0/10/15/20 "))
    items_total = get_total_amount(payment_list)
    tip = get_tip_amount(items_total, user_tip)
    total = round(items_total + tip, 2)
    print(f"El total a pagar es de ${total} con ${tip} en propina.")


show_final_payment()
