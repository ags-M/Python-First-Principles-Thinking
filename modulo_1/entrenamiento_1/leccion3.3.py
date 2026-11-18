#validador de password

contraseña = input("Inventá una contraseña: ")
contraseña_R = input("Repetila: ")

# Verificación 1: ¿Coinciden?
coinciden = contraseña == contraseña_R

# Verificación 2: ¿Tiene al menos 8 caracteres?
tiene_8_caracteres = len(contraseña) >= 8

# Verificación 3: ¿No es la prohibida "12345678"?
no_es_prohibida = contraseña != "12345678"

# Mostrar cada chequeo
print(f"¿Las contraseñas coinciden? {coinciden}")
print(f"¿Tiene al menos 8 caracteres? {tiene_8_caracteres}")
print(f"¿No es la prohibida? {no_es_prohibida}")

# Contraseña válida solo si TODAS se cumplen (and)
es_valida = coinciden and tiene_8_caracteres and no_es_prohibida
print(f"Contraseña válida: {es_valida}")