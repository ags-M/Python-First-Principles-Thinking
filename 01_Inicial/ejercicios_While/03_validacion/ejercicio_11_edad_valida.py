# ============================================================
# Ejercicio 11: Edad válida
# Categoría: 03_validacion
# ============================================================
# ENUNCIADO:
# Pedile al usuario su edad. Si es menor a 0 o mayor a 120, volvé a pedirla. Repetí hasta que sea válida.

# 1. Lectura adelantada: pedimos el dato ANTES del while para tener algo que evaluar.
edad = int(input("Ingresá tu edad (18/70): "))
# 2. Condición de INVALIDEZ: mientras la edad esté FUERA del rango, seguimos pidiendo.
while edad < 18 or edad > 70: #edad menor de cero o edad mayor a 120 esto ES TRUE 
    print("⚠️ Error: Esa edad no es válida. Intentá de nuevo.")
    # 3. Actualización: volvemos a pedir el dato DENTRO del bucle.
    edad = int(input("Ingresá tu edad (18/70): "))

# 4. Si el código llega acá, es porque la condición del while es FALSA (la edad es válida).
print(f"✅ Edad registrada correctamente: {edad} años.")


#__________________________________________________________________________________________________
"""
📊 Traceo manual (Usuario se equivoca 2 veces)
Paso        edad ingresada        ¿edad < 18 o edad > 70?        Acción del programa
___________________________________________________________________________________________________

1                75            Sí ( 75 > 70) es TRUE           Imprime error, pide de nuevo
---------------------------------------------------------------------------------------------------

2                12            Sí ( 12 < 18) es TRUE             Imprime error, pide de nuevo
---------------------------------------------------------------------------------------------------
3                25            No (está en rango) es FALSE            SALE del while
---------------------------------------------------------------------------------------------------
4                                                               Imprime "✅ Edad registrada..."
___________________________________________________________________________________________________

"""