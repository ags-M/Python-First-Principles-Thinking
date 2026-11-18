# =====================================================================
# EJERCICIO #24  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí monto (float), horario raro (s/n), país riesgo (s/n),
# cliente conocido (s/n). 'sospechosa' True si monto>10000 y
# (horario_raro o pais_riesgo) y no conocido.
#
# QUE SE BUSCA ENTRENAR:
# Detección de fraude con float.
#
# REGLAS (solo lecciones 2 y 3):
#   - Podés usar: input(), print(), int(), float(), str(), bool()
#   - Operadores aritméticos: +  -  *  /  //  %  **
#   - Operadores de comparación: ==  !=  <  >  <=  >=
#   - Operadores lógicos: and  or  not
#   - f-strings
#   - len() para medir strings
#   - NO uses if/elif/else, ni for, ni while, ni listas, ni funciones
#
# =====================================================================


# ---------------- TU SOLUCIÓN ACÁ ----------------






# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# monto = float(input('Monto: '))
# horario_raro = input('¿Horario raro? (s/n): ').lower() == 's'
# pais_riesgo = input('¿País riesgo? (s/n): ').lower() == 's'
# conocido = input('¿Cliente conocido? (s/n): ').lower() == 's'
# sospechosa = (monto > 10000) and (horario_raro or pais_riesgo) and (not conocido)
# print(f'¿Sospechosa?: {sospechosa}')
#
# =====================================================================
