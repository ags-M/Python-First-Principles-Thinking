# ============================================================
# Ejercicio 12: Nota válida
# Categoría: 03_validacion
# ============================================================
#
# ENUNCIADO:
# Pedile al usuario una nota entre 0 y 10. Si se equivoca, volvé a pedirla.

num = int(input("ingresa un numero (0/10): "))
while num < 0 or num > 10:
    print(f"El numero ingresado {num} no es válido")
    num = int(input("ingresa un numero (0/10): "))
print(f"El numero {num} es correcto")

"""
📊 Traceo manual 

Paso        opcion ingresada   ¿mum < 0 o num> 3?                 Acción del programa
___________________________________________________________________________________________________
 
1                11           Sí ( 11 > 10) es TRUE              Imprime NO es valido, pide de nuevo
---------------------------------------------------------------------------------------------------

2                -1           SI -1 < 0 ES TRUE                  Imprime NO es valido, pide de nuevo         

----------------------------------------------------------------------------------------------------   
3                 1         No (está en rango) es FALSE            SALE del while
---------------------------------------------------------------------------------------------------
4                                                               Imprime "✅ numero correcto ..."
___________________________________________________________________________________________________

"""
