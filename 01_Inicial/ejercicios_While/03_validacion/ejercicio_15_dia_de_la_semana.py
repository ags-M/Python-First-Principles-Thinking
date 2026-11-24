# ============================================================
# Ejercicio 15: Día de la semana
# Categoría: 03_validacion
# ============================================================
#ENUNCIADO: "Una empresa solo atiende de lunes a viernes. 
# Pedile al usuario un día de la semana y rechazá los fines de semana (sábado y domingo)."
#

dias_aceptados = ["lunes", "martes", "miercoles", "jueves", "viernes"]
seleccion_dia = input("ingresa un dia de la semana: ").lower()

while seleccion_dia not in dias_aceptados:
    print("'No ingresaste el dia de semana aceptado'")
    seleccion_dia = input("ingresa un dia de la semana aceptado: ").lower()
print(f"'Ingresaste el dia de semana aceptado': {seleccion_dia}")

#📊 Traceo manual
#____________________________________________________________________________________________

# iteracion          dia que ingreso        cumple con la lista          que imprime
                                           
#____________________________________________________________________________________________
#     1                  domingo                     no             no ingresaste el dia aceptado
#----------------------------------------------------------------------------------------------
#     2                    lunes                     si                   sale del bucle
#-----------------------------------------------------------------------------------------------
                                                               # imprime ingresaste dia aceptado
#-----------------------------------------------------------------------------------------------