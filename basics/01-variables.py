# Python3 - Variables 📦
# Las variables en Python son contenedores donde se almacenan valores de datos.
# Una variable es creada en el momento que le asignas un valor.
# Python no es de tipado estricto, asi que no necesita declara algun tipo en particular.
# Además, el tipo puede cambiar incluso despues de que fueron creadas.

# Nombres de variables.
# Reglas.
# 1. Debe empezar con una letra o un _ (underscore)
# 2. No puede empezar con un número.
# 3. Solo deben contener caracteres alphanumericos y underscores (A-z, 0-9, _)
# 4. Son case-sensitive esto age, no es lo mismo que Age o AGE.
# 5. No puedes usar ningunas de las palabras reservadas de Python.

first_name = "Cristhian" # ✅
_first_name = "_cristhian" # ✅
FirstName = "Cristhian" # ✅
firstName = "cristhian" # ✅
firstName10 = "cristhian10" # ✅

10Cristhian = "10cristhian" # ❌
cristhian-com = "cristhian-com" # ❌
cristhian space = "cristhian space" # ❌

# Python te permite asignar varios valores a varias variables en una linea.
a, b, c = "A", "B", "C"
