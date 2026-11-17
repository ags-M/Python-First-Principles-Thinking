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
print(f"La cantidad de digitos es: {contador_digitos}")

#--------------------------------------------
print("-" * 30)
#--------------------------------------------

"""
💡 Un atajo muy usado en Python:
Aunque la fórmula matemática con while es excelente para aprender lógica de programación, 
en Python la forma más rápida y común de contar dígitos es convertir el número a texto y usar len():

"""
n = int(input("Ingrese un numero entero: "))

contador = len(str(n)) # Convierte n a "n" es decir un string y cuenta sus caracteres
                       # recordar que len solo cuenta del 0 al 10 solo de 1 digito nada mas
#--------------------------------------------
print("-" * 30)
#--------------------------------------------


n = -1234      # Prueba cambiando este valor a 0 
contador = 0

# 1. CASO ESPECIAL: El cero tiene exactamente 1 dígito
if n == 0:
    contador = 1

# 2. CASO NEGATIVO: Si es menor a 0, lo volvemos positivo
else:
    if n < 0:
        n = -n   # También se puede escribir como: n = abs(n)
    
    # 3. CASO GENERAL: Ahora sí aplicamos la fórmula de corte y conteo
    while n > 0:
        digito = n % 10      # (Opcional) Aquí "ves" o extraes el dígito
        contador += 1        # Sumamos 1 al contador
        n = n // 10          # "Cortamos" o eliminamos el último dígito

print("Cantidad de dígitos:", contador)
