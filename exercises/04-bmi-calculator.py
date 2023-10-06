# Calcular el Indice de Masa Corporal (IMC)
# Nivel Fácil
## Crea un programa que calcule el IMC,
## Según el peso y la altura del usuario.
## El IMC es una medida del peso de una persona teniendo en cuenta su altura.
## Si una persona alta y una baja pesan lo mismo,
## la persona baja suele tener más sobrepeso.
## El IMC se calcula dividiendo el peso de una persona (en kg)
## por el cuadrado de su altura (en m).
# 1. Preguntale el peso y la altura
# 2. Luego has el calculo
# 3. Imprime el resultado con un formato agradable en la terminal.
# weight / (height * height) = IMC
def get_current_imc():
    weight = float(input("Cuál es tu peso actual? (kg) "))
    height = float(input("Cuál es tu altura actual? (m) "))
    imc = round(weight / (height * height), 2)
    print(f"Tu indice de masa corporal es {imc}%")
    # Si el % es < 18.5 = Estas por debajo de tu peso ideal.
    if imc < 18.7:
        return "Estas por debajo de tu peso ideal."
    # Si el % es entre 18.5 y 24.9 = Estas en tu peso ideal.
    elif imc >= 18.5 and imc <= 24.9:
        return "Estas en tu peso ideal."
    # Si el % es entre 25 y 29.9 = Estas con Sobrepeso.
    elif imc >= 25.0 and imc <= 29.9:
        return "Estas con Sobrepeso."
    # Si el % es entre 30 y 34.9 = Estas con Obesidad I.
    elif imc >= 30.0 and imc <= 34.9:
        return "Estas con Obesidad I."
    # Si el % es entre 35 y 39.9 = Estas con Obesidad II.
    elif imc >= 35.0 and imc <= 39.9:
        return "Estas con Obesidad II."
    else:
        # Si el % es > 40 = Estas con Obesidad III.
        return "Estas con Obesidad III."

message = get_current_imc()
print(message)
