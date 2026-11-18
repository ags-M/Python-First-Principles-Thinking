# =====================================================================
# EJERCICIO #07  -  NIVEL: MEDIANA
# =====================================================================
# Categoria:       Composicion de condiciones (logica booleana)
# Nivel cognitivo: Aplicar
# Lecciones:       2 (variables, tipos, input, print) y 3 (operadores)
# Dificultad:      MEDIANA
# =====================================================================
#
# CONSIGNA:
# Pedí una nota (0-10) y guardá en 'aprobo' True si es 6 o más.
#
# QUE SE BUSCA ENTRENAR:
# Comparación >= aplicada a un caso de estudio.
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
n_examen = int(input("Cual fue tu calificacion: "))
aprobado = n_examen >= 6 
print(f"tu nota de examen {n_examen} esta aprobada es: {aprobado} ")

# ---------------- TU SOLUCIÓN ACÁ ----------------
# =====================================================================
# SOLUCIÓN (no mires hasta intentarlo al menos 10 minutos)
# =====================================================================
# nota = int(input('Ingresá tu nota: '))
# aprobo = nota >= 6
# print(f'¿Aprobaste?: {aprobo}')
#
# =====================================================================
