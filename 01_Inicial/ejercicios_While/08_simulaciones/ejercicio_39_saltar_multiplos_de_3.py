# ============================================================
# Ejercicio 39: Saltar múltiplos de 3
# Categoría: 08_simulaciones
# ============================================================
#
# ENUNCIADO:
# Contá del 1 al 20, pero saltate los múltiplos de 3 usando 'continue'.

"""
# PLAN DE LOGICA DE PROGRAMACION - NO ES CODIGO FINAL
# 1. Recorrer del 1 al 20
# 2. En cada vuelta:
#    - Calcular el resto de dividir el numero por 3
#    - Preguntar si ese resto es igual a 0
#    - Si es igual a 0: usar continue ANTES del print
#    - Si no es igual a 0: mostrar el numero

# Chequeo mental:
# ¿El continue esta antes del print? ...
# ¿La condicion compara el resto con 0? ...
# ¿El print muestra solo los que NO son multiplos de 3? ...

"""
n = 1                          # arrancamos en 1 porque el ejercicio pide del 1 al 20

while n <= 20:                 # mientras n sea menor o igual a 20, seguimos
    if n % 3 == 0:             # preguntamos: ¿el resto de dividir n por 3 es 0?
        n += 1                 # si es múltiplo de 3, avanzamos PRIMERO
        continue               # y salteamos el resto de esta vuelta (no mostramos n)

    print(n)                   # si NO era múltiplo de 3, lo mostramos
    n += 1                     # y después avanzamos al siguiente número
#--------------------------------------------------------------------------------

print("---"*30)

#--------------------------------------------------------------------------------
"""
# SI n += 1 ESTA DESPUES DEL continue:
# - n es multiplo de 3 -> entra al if
# - ejecuta continue
# - se saltea n += 1
# - n no cambia
# - vuelve al while con el mismo n
# - BUCLE INFINITO (no se detiene, se cuelga)

# SI n += 1 ESTA ANTES DEL continue:
# - n es multiplo de 3 -> entra al if
# - ejecuta n += 1
# - ejecuta continue
# - saltea el print
# - vuelve al while con n actualizado
# - SIGUE CON EL SIGUIENTE NUMERO

# PREGUNTAS PARA DISTINGUIR si While se Detiene o se Cuelga:
# ¿La condicion del while en algun momento se vuelve falsa?
#   SI -> el bucle se detiene (termina)
#   NO -> el bucle se cuelga (bucle infinito)
#
# ¿La variable de control cambia en TODAS las vueltas?
#   SI -> en algun momento va a salir
#   NO -> se cuelga
#
# ¿El codigo despues del while se ejecuta?
#   SI -> el bucle se detuvo bien
#   NO -> probablemente se colgo
__________________________________________________________________________________________________________________

variable de control en este ejercicio es n
Hay dos cosas que definen a una variable de control de un while:
1ro.- aparece en la condicional del bucle ----> while n <= 20:
2do.- Cambia dentro del bucle para que la condición algún día sea falsa: n += 1
resultante de todo esto es : 
Sin n cambiando, el while nunca termina. Por eso n es la que “controla” si el bucle sigue o se detiene.

# VARIABLE DE CONTROL
# Es la variable que aparece en la condicion del while
# y que cambia dentro del bucle.
#
# En este ejercicio:
# - Variable de control: n
# - Condicion: n <= 20
# - Avance: n += 1
#
# NO es variable de control:
# - print(n): solo muestra
# - continue: solo salta una vuelta
# - if n % 3 == 0: solo pregunta
"""
# versiones progresivas de este mismo código para que veas cómo piensa un principiante, un intermedio y un ingeniero.


#--------------------------------------------------------------------------------

print("---"*30)

#--------------------------------------------------------------------------------
print("VERSION 1.- PRINCIPIANTE (la que vimos anteriormente)")
n = 1
while n <= 20:
    if n % 3 == 0:
        n += 1
        continue
    print(n)
    n += 1
#--------------------------------------------------------------------------------

print("---"*30)

#--------------------------------------------------------------------------------    
   
print("Versión 2: Intermedia (sin continue)")

n = 1
while n <= 20:
    if n % 3 != 0:      # Si NO es múltiplo de 3
        print(n)        # Lo mostramos
    n += 1              # Avanzamos SIEMPRE
#--------------------------------------------------------------------------------

print("---"*30)

#--------------------------------------------------------------------------------
    
print("Versión 3: Ingeniero/a (la forma 'Pythonic')")  

for n in range(1, 21):  # range(1, 21) genera del 1 al 20
    if n % 3 == 0:
        continue        # Salta el print
    print(n)
#--------------------------------------------------------------------------------

print("---"*30)

#--------------------------------------------------------------------------------

