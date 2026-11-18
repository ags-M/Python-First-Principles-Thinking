"""
==========================================================================
Ejercicio 08: Contar vocales
==========================================================================

ENUNCIADO
---------
Pedile al usuario un string. Decí cuántas vocales (minúsculas o mayúsculas) tiene, usando for.

PISTA (leela solo si te trabás)
-------------------------------
`c.lower() in 'aeiou'`.

"""
s = input("Ingresá un string: ").lower()
contador = 0
for c in s:
    if c in "aeiou":
        contador = contador +1 
print(f"la cantidad de vocales que hay en {s} es igual a {contador}") 


