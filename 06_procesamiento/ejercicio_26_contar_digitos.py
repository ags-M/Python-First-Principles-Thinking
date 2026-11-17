# ============================================================
# Ejercicio 26: Contar dígitos
# Categoría: 06_procesamiento
# ============================================================
#
# ENUNCIADO:
# Pedile un número entero y mostrá cuántos dígitos tiene usando while (sin convertir a string).
#
# -----------------------------------------------------------
# PISTA para principiantes:
# Recordá la estructura básica del while:
#
#   variable = valor_inicial
#   while condicion:
#       # acciones
#       variable = variable + 1   (o lo que corresponda)
#
# Escribí tu solución debajo de esta línea.
# Cuando termines, probá el programa con varios casos.
# -----------------------------------------------------------
n = int(input("Ingrese un numero entero: "))
digitos = 0
contador_digitos= 0
lista_digitos = [""]

while n > 0:
    digito = n % 10       # 1. EXTRAER (Cortar): Obtiene el último dígito (ej: de 123 obtiene 3)
    contador_digitos += 1         # 2. CONTAR: Suma 1 al contador por cada dígito que encuentra
    n = n // 10           # 3. ELIMINAR (Cortar): Elimina el último dígito del número (ej: 123 pasa a ser 12)
print(f"primer ejercicio = La cantidad de digitos es: {contador_digitos}")
#__________________________________________________________________________________________________________
#--------------------------------------------
print("-" * 30)
#--------------------------------------------
#___________________________________________________________________________________________________________
"""
💡 Un atajo muy usado en Python:
Aunque la fórmula matemática con while es excelente para aprender lógica de programación, 
en Python la forma más rápida y común de contar dígitos es convertir el número a texto y usar len():

"""
n = int(input("Ingrese un numero entero: "))

contador_digitos = len(str(n)) # Convierte n a "n" es decir un string y cuenta sus caracteres
                       # recordar que len solo cuenta del 0 al 10 solo de 1 digito nada mas
print(f"segundo ejercicio: la cantidad de digitos es: {contador_digitos}")
#-----------------------------------------------------------------------------------------------------------
#--------------------------------------------
print("-" * 30)
#--------------------------------------------

# otra simplificacion 

def contardor_digitos_rapido(n):
    return len(str(abs(n)))
print("tercer ejercicio: la cantidad de digitos es de: ", contardor_digitos_rapido(12345))
"""
¿Cómo funciona este atajo?
abs(n) lo vuelve positivo (ej: -85 → 85).
str(...) lo convierte en texto (ej: 85 → "85").
len(...) cuenta los caracteres de ese texto (ej: "85" tiene longitud 2).

"""

#--------------------------------------------
print("-" * 30)
#--------------------------------------------
"""
PATRON del ciclo while para que funcione correctamente en todos los casos:
números positivos, números negativos y el cero.

"""
# 🎯 Este ejercicio es contar digitos de un numero NEGATIVO:
# n = int(input("Ingrese un numero entero: "))
n = -1234      # Prueba cambiando este valor a 0 
contador = 0

# 1. CASO ESPECIAL, el usuario esribe 0 : El cero tiene exactamente 1 dígito
# Si n = 0: El ciclo while n > 0: nunca se ejecutaría, y el contador se quedaría en 0. 
# Pero matemáticamente, el número 0 tiene 1 dígito. 
# Por eso lo atrapamos primero con un if.
if n == 0:
    contador = 1
# 2. CASO NEGATIVO: Si es menor a 0, lo volvemos positivo
else:
    if n < 0:
        n = -n   # También se puede escribir como:🎯 n = abs(n)
#Si el usuario escribe un n y es negativo (ej. -4567): Si no hacemos nada, el ciclo while n > 0 esto con n negativo: 
# tampoco se ejecutaría. Al hacer n = -n (o n = abs(n)), convertimos -4567 en 4567. 
# Así el ciclo funciona normal y "**no contamos el signo menos como si fuera un dígito**"".
    # 3. CASO GENERAL: Ahora sí aplicamos la fórmula de corte y conteo
    while n > 0:
#El ciclo while: Hace el trabajo pesado de ir "cortando" con el resto o modulo y 
# luedo el número de derecha a izquierda (n // 10) y sumando 1 al contador por cada vez que logra cortar un pedazo.
        digito = n % 10      # (Opcional) Aquí "ves" o extraes el dígito
        contador += 1        # Sumamos 1 al contador
        n = n // 10          # "Cortamos" o eliminamos el último dígito
        #ingresa al ciclo while hasta agotar los digitos cuando n= 0 entonces 0 > 0 cierra el bucle y print
print("cuarto ejercicio: Cantidad de dígitos:", contador)
