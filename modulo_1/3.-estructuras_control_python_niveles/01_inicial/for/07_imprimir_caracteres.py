"""
==========================================================================
Ejercicio 07: Imprimir caracteres
==========================================================================

ENUNCIADO
---------
Pedile al usuario un string. Imprimí cada carácter en una línea usando for.

PISTA (leela solo si te trabás)
-------------------------------
`for c in s`.

"""
s = input("Ingresá un string: ")
for c in s:
    print(c)

#-------------------------------
print("-"* 12)
#-------------------------------

texto = input("Ingresá un string: ")
for caracter in reversed(texto):
    print(caracter)

#-------------------------------
print("-"* 12)
#-------------------------------

texto = input("Ingresá un string: ")
for i in range(len(texto) - 1, -1, -1):
    print(texto[i])