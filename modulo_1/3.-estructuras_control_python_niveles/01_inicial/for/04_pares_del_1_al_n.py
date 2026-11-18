"""
==========================================================================
Ejercicio 04: Pares del 1 al N
==========================================================================

ENUNCIADO
---------
Pedile al usuario N. Mostrá (uno por línea) los pares del 1 al N usando for.

PISTA (leela solo si te trabás)
-------------------------------
`range(2, n+1, 2)` o filtrá con if.

"""
n = int(input("Ingresá un número entero: "))
for i in range(2, n+1, 2):
    print(i)

print("-"* 12)
#------------------------------------------
#Funciona, pero es menos elegante
n = int(input("Ingresá un número entero: "))
for i in range(1, n+1): # arranca de 1 paso 1 a todos
    if i % 2 == 0:        # el if filtra si i es par
        print(i)
    
    



# ============================================================
#  Casos de prueba sugeridos
#  Antes de ejecutar: anotá qué salida esperás de cada uno.
#  Después probá tu código y compará. Si coinciden en todos → OK.
# ============================================================
#   - 10
#   - 7
#   - 1
