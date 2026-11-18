# =====================================================================
# EJERCICIO #21  -  NIVEL: DIFICIL
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Analizar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      DIFICIL
# =====================================================================
#
# CONSIGNA:
# Pedí paciente inestable (s/n), consentimiento implícito (s/n),
# tutor (s/n), testamento vital (s/n). 'cirugia_urg' True si
# inestable y (implicito o tutor) y no testamento.
#
# QUE SE BUSCA ENTRENAR:
# Caso médico con doble negación implícita.
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
# inestable = input('¿Inestable? (s/n): ').lower() == 's'
# implicito = input('¿Consentimiento implícito? (s/n): ').lower() == 's'
# tutor = input('¿Tutor? (s/n): ').lower() == 's'
# testamento = input('¿Testamento vital? (s/n): ').lower() == 's'
# cirugia_urg = inestable and (implicito or tutor) and (not testamento)
# print(f'¿Cirugía urgente?: {cirugia_urg}')
#
# =====================================================================
