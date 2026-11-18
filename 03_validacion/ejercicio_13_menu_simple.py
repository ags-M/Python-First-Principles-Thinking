# ============================================================
# Ejercicio 13: Menú simple
# Categoría: 03_validacion
# ============================================================
#
# ENUNCIADO:
# Mostrá un menú con 3 opciones. El usuario elige una. El programa termina cuando elija '4. Salir'.
#
# No necesitamos declarar las opciones por separado si solo validamos el rango
menu = int(input("Ingresa una opción (1, 2 o 3): "))

while menu < 1 or menu > 3:
    print("⚠️ Error: Opción no válida. Debe ser 1, 2 o 3.")
    menu = int(input("Ingresa una opción (1, 2 o 3): "))

print(f"✅ Opción {menu} registrada. Serás atendido.")

"""
📊 Traceo manual (Usuario se equivoca pone numero 4 )

Paso        opcion ingresada   RANGO < 1 o menu > 3?                 Acción del programa
___________________________________________________________________________________________________
 
1                4                  4 > 3 es TRUE              Imprime error, pide de nuevo
---------------------------------------------------------------------------------------------------

2                1                  1 < 1   FALSE                  Imprime menu valido          
                               No (está en rango) es FALSE            SALE del while
---------------------------------------------------------------------------------------------------
4                                                               Imprime "✅ opcion  registrado..."
___________________________________________________________________________________________________

"""