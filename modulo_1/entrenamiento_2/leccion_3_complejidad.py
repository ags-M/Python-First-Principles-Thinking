# -*- coding: utf-8 -*-
"""
Curso de Python - De cero a experto
MÓDULO 1 - LECCIÓN 3: OPERADORES
Batería de entrenamiento complementaria - 40 ejercicios

Distribución de dificultad:
  Ejercicios  1 - 15  →  FÁCIL
  Ejercicios 16 - 28  →  MEDIO
  Ejercicios 29 - 40  →  DIFÍCIL

Modalidades de ejercicio (novedad de esta batería):
  - PREDICCIÓN: leé el código y decidí qué imprime, SIN ejecutarlo.
  - DEBUGGING:  encontrá el error en el código dado y corregilo.
  - FILL-IN:    completá los huecos (_____) del código.
  - V/F:        afirmación teórica, respondé Verdadero o Falso y justificá.
  - TIPO:       decí qué tipo de dato devuelve la expresión.
  - REFACTOR:   reescribí el código de forma más prolija o más corta.
  - CASO LÍMITE: analizá qué pasa con un caso raro o trampa.
  - TABLA DE VERDAD: completá combinaciones de and/or/not.
  - SIMPLIFICACIÓN: reducí una expresión booleana compleja a una más simple.
  - TEST DE MESA: trazá el código con varios inputs.
  - PROYECTO:   programa integrador usando todo lo de la lección.

Cómo usar este archivo en VS Code:
  1. Abrí este archivo .py en VS Code.
  2. Leé el enunciado de cada ejercicio (en los comentarios).
  3. Escribí tu solución en el espacio debajo de "Tu solución:".
  4. Para PREDICCIÓN, V/F o TIPO: escribí tu respuesta como comentario.
  5. Para DEBUGGING, FILL-IN o REFACTOR: escribí el código corregido.
  6. Para PROYECTO: escribí el programa completo.
  7. Verificá ejecutando cuando corresponda.

Temas que cubre esta batería:
  - Aritméticos:  +  -  *  /  //  %  **
  - Comparación:  ==  !=  <  >  <=  >=
  - Lógicos:      and   or   not
  - Precedencia y asociatividad
  - Cortocircuito (short-circuit)
  - Casos límite (división por cero, negativos con %, ** fraccionario)
  - Tablas de verdad y simplificación

Tips antes de empezar:
  - La división / SIEMPRE devuelve float, aunque sean enteros.
  - // es división entera (sin decimales).
  - % es módulo (el resto de la división).
  - ** es potencia: 2**3 = 8.
  - Las comparaciones devuelven True o False (bool).
  - and / or / not combinan condiciones.
  - Precedencia: ** > unarios > * / % // > + - > comparaciones > not > and > or.
  - and y or usan CORTOCIRCUITO: si ya saben el resultado, no evalúan el resto.
  - En Python, a % b tiene el MISMO SIGNO que b (el divisor).
"""


# ##################################################################
# #                                                                #
# #           NIVEL FÁCIL  (Ejercicios 1 a 15)                     #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.1  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(10 + 5 * 2)
#
# Pista: la multiplicación tiene MAYOR precedencia que la suma.
#        Se evalúa como 10 + (5 * 2).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.2  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(2 ** 3 ** 2)
#
# Pista: ** es asociativo por la DERECHA.
#        Se evalúa como 2 ** (3 ** 2).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.3  [FÁCIL]  (FILL-IN)
# ------------------------------------------------------------------
# Completá el hueco para calcular el doble de x:
#
#   x = 7
#   doble = x _____ 2
#
# Pista: el operador de multiplicación es *.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.4  [FÁCIL]  (V/F)
# ------------------------------------------------------------------
# Afirmación: "El operador / SIEMPRE devuelve float, aunque ambos
# operandos sean int."
#
# Respondé V o F y justificá con un ejemplo.
#
# Pista: probá  4 / 2  y mirá si lleva punto decimal.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.5  [FÁCIL]  (TIPO)
# ------------------------------------------------------------------
# ¿Qué tipo devuelve?
#
#   10 / 2
#
# Pista: / siempre da float, sin importar los operandos.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.6  [FÁCIL]  (DEBUGGING)
# ------------------------------------------------------------------
# Este código tiene un error sutil. Encontrálo y corregilo.
#
#   edad = 25
#   es_mayor = edad = 18
#   print(es_mayor)
#
# Pista: = es ASIGNACIÓN, == es COMPARACIÓN.
#        edad = 18 asigna 18 a edad (y devuelve 18, no un bool).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.7  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(10 // 3)
#
# Pista: // es división ENTERA, descarta los decimales.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.8  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(10 % 3)
#
# Pista: % es módulo, devuelve el RESTO de la división.
#        10 // 3 = 3 con resto 1.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.9  [FÁCIL]  (V/F)
# ------------------------------------------------------------------
# Afirmación: "0 ** 0 da error porque es una indeterminación matemática."
#
# Respondé V o F y justificá.
#
# Pista: probá en Python  print(0 ** 0). Python decide un valor
#        por convención (no necesariamente el matemático).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.10  [FÁCIL]  (TIPO)
# ------------------------------------------------------------------
# ¿Qué tipo devuelve?
#
#   5 // 2
#
# Pista: // con dos int devuelve int (no float como /).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.11  [FÁCIL]  (FILL-IN)
# ------------------------------------------------------------------
# Completá el hueco para verificar si edad es mayor o igual a 18:
#
#   edad = 20
#   es_mayor = edad _____ 18
#
# Pista: el operador "mayor o igual" es >=.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.12  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(5 > 3 and 2 < 1)
#
# Pista: and da True solo si AMBAS condiciones son True.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.13  [FÁCIL]  (DEBUGGING)
# ------------------------------------------------------------------
# Este código rompe. Encontrá el error y corregilo.
#
#   x = 5
#   y = "3"
#   print(x + y)
#
# Pista: NO podés sumar int + str. Hay que convertir y a int primero.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.14  [FÁCIL]  (CASO LÍMITE)
# ------------------------------------------------------------------
# ¿Qué pasa al ejecutar esto?
#
#   print(7 % 0)
#
# Pista: módulo por cero es como dividir por cero.
#        Python lanza un error específico, ¿cuál?
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.15  [FÁCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(not True or False and True)
#
# Pista: precedencia: not > and > or.
#        Evaluá primero not, después and, después or.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL MEDIO  (Ejercicios 16 a 28)                    #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.16  [MEDIO]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(2 + 3 * 4 ** 2)
#
# Pista: orden de precedencia: ** primero, después *, después +.
#        Es: 2 + (3 * (4 ** 2)).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.17  [MEDIO]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print(10 - 3 - 2)
#
# Pista: - es asociativo por la IZQUIERDA.
#        Se evalúa como (10 - 3) - 2.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.18  [MEDIO]  (V/F)
# ------------------------------------------------------------------
# Afirmación: "and equivale a multiplicación lógica (1*1=1) y
# or equivale a suma lógica (1+1=1)."
#
# Respondé V o F y justificá con las tablas de verdad de and y or.
#
# Pista: True = 1, False = 0. and → multiplicación, or → suma
#        truncada a 1. ¿Coincide?
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.19  [MEDIO]  (TIPO)
# ------------------------------------------------------------------
# ¿Qué tipo devuelve cada una? (3 respuestas)
#
#   7 / 2
#   7 // 2
#   7 % 2
#
# Pista: / siempre da float. // y % con dos int dan int.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.20  [MEDIO]  (DEBUGGING)
# ------------------------------------------------------------------
# Este código no funciona. Encontrá el error y corregilo.
#
#   precio = 1000
#   descuento = precio * 0.10
#   total = precio - descuent
#   print(total)
#
# Pista: revisá bien los nombres de las variables (typo).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.21  [MEDIO]  (FILL-IN)
# ------------------------------------------------------------------
# Completá el hueco para verificar si n es par:
#
#   n = 8
#   es_par = (n _____ 2 == 0)
#
# Pista: el módulo % da el RESTO de dividir n por 2.
#        Si ese resto es 0, el número es par.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.22  [MEDIO]  (TABLA DE VERDAD)
# ------------------------------------------------------------------
# Completá esta tabla para  a and b:
#
#   a     | b     | a and b
#   ----- | ----- | -------
#   True  | True  | _____
#   True  | False | _____
#   False | True  | _____
#   False | False | _____
#
# Pista: and solo da True si AMBAS son True.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.23  [MEDIO]  (CASO LÍMITE - CORTOCIRCUITO)
# ------------------------------------------------------------------
# ¿Qué pasa al ejecutar esto? ¿Imprime algo? ¿Rompe?
#
#   print(False and (10 / 0 == 0))
#
# Pista: and usa CORTOCIRCUITO. Si el primer operando es False,
#        ya sabe que el resultado es False y NO evalúa el segundo.
#        (10 / 0) nunca llega a ejecutarse.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.24  [MEDIO]  (REFACTOR)
# ------------------------------------------------------------------
# Este código usa if anidados innecesariamente. Reescribilo usando
# UNA SOLA expresión con and:
#
#   edad = 20
#   tiene_dni = True
#   if edad >= 18:
#       if tiene_dni:
#           print(True)
#       else:
#           print(False)
#   else:
#       print(False)
#
# Pista: print((edad >= 18) and tiene_dni). Una sola línea.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.25  [MEDIO]  (CASO LÍMITE)
# ------------------------------------------------------------------
# ¿Qué devuelven estos casos con negativos?
#
#   print(-5 % 3)
#   print(5 % -3)
#
# Pista: en Python, el resultado de % tiene el MISMO SIGNO que
#        el DIVISOR (el segundo operando). No el de matemáticas clásicas.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.26  [MEDIO]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   x = 5
#   print(f"{x + 3 * 2}")
#
# Pista: dentro de {} se evalúa la EXPRESIÓN completa, respetando
#        precedencia normal.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.27  [MEDIO]  (V/F)
# ------------------------------------------------------------------
# Afirmación: "10 // 3 da exactamente lo mismo que int(10 / 3)."
#
# Respondé V o F y justificá. Probá también con NEGATIVOS.
#
# Pista: para positivos sí coinciden. Probá con  -10 // 3  y con
#        int(-10 / 3)  ¿dan lo mismo?
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.28  [MEDIO]  (SIMPLIFICACIÓN)
# ------------------------------------------------------------------
# Simplificá esta expresión booleana a una más corta:
#
#   not (not a or not b)
#
# Pista: esto se conoce como LEY DE MORGAN.
#        "no (no a o no b)" equivale a "a y b".
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL DIFÍCIL  (Ejercicios 29 a 40)                  #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.29  [DIFÍCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime?
#
#   print((2 + 3) * (4 - 1) ** 2)
#
# Pista: los PARÉNTESIS se evalúan primero.
#        Después **, después *.
#        Es: (5) * (3) ** 2 = 5 * 9 = 45.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.30  [DIFÍCIL]  (DEBUGGING)
# ------------------------------------------------------------------
# Este mini-programa tiene 3 bugs. Encontrá los 3 y corregilos.
#
#   precio = input("Precio: ")
#   cantidad = input("Cantidad: ")
#   total = precio * cantidad
#   descuento = total * 0,10
#   print(f"Total: {total - descuento")
#
# Pista 1: input() devuelve str. Para multiplicar como números,
#          hay que convertir (float o int).
# Pista 2: en Python los DECIMALES usan PUNTO, no coma.
#          0,10 no es un float válido (en realidad es una tupla).
# Pista 3: revisá los paréntesis y llaves del último print.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.31  [DIFÍCIL]  (TABLA DE VERDAD)
# ------------------------------------------------------------------
# Completá esta tabla para la expresión:  a and (b or not c)
#
#   a     | b     | c     | not c | b or not c | a and (b or not c)
#   ----- | ----- | ----- | ----- | ---------- | ------------------
#   True  | True  | True  | _____ | _____      | _____
#   True  | True  | False | _____ | _____      | _____
#   True  | False | True  | _____ | _____      | _____
#   True  | False | False | _____ | _____      | _____
#   False | True  | True  | _____ | _____      | _____
#   False | False | False | _____ | _____      | _____
#
# Pista: evaluá de ADENTRO hacia afuera.
#        Primero not c, después b or not c, después a and (eso).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.32  [DIFÍCIL]  (CASO LÍMITE - CORTOCIRCUITO)
# ------------------------------------------------------------------
# Para cada caso, decidí si el código se ejecuta sin error o si
# ROMPE con ZeroDivisionError. Justificá cada uno.
#
#   a) print(True or (10 / 0))
#   b) print(False and (10 / 0))
#   c) print(False or (10 / 0))
#   d) print(True and (10 / 0))
#
# Pista: or cortocircuita si el primer operando es True.
#        and cortocircuita si el primer operando es False.
#        Si no cortocircuita, evalúa el segundo operando y ROMPE.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.33  [DIFÍCIL]  (REFACTOR)
# ------------------------------------------------------------------
# Este código clasifica el IMC usando if/elif/else.
# Reescribilo SIN usar if, usando el truco de MULTIPLICAR strings
# por bools ("Texto" * True = "Texto", "Texto" * False = ""):
#
#   imc = 23.5
#   if imc < 18.5:
#       cat = "Bajo peso"
#   elif 18.5 <= imc < 25:
#       cat = "Normal"
#   elif 25 <= imc < 30:
#       cat = "Sobrepeso"
#   else:
#       cat = "Obesidad"
#   print(cat)
#
# Pista:
#   cat = "Bajo peso" * (imc < 18.5) + "Normal" * (18.5 <= imc < 25) + ...
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.34  [DIFÍCIL]  (CASO LÍMITE)
# ------------------------------------------------------------------
# ¿Qué imprimen estas líneas?
#
#   print(2 ** 0.5)
#   print(9 ** 0.5)
#   print(8 ** (1/3))
#   print((-1) ** 0.5)
#
# Pista: ** con exponente FRACCIONARIO funciona como RAÍZ.
#        2 ** 0.5 = raíz cuadrada de 2.
#        9 ** 0.5 = raíz cuadrada de 9.
#        8 ** (1/3) = raíz cúbica de 8.
#        (-1) ** 0.5 = ? Python hace algo curioso, mirá bien.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.35  [DIFÍCIL]  (PREDICCIÓN)
# ------------------------------------------------------------------
# ¿Qué imprime? (El truco de multiplicar strings por bools)
#
#   imc = 22.0
#   categoria = "Bajo" * (imc < 18.5) + "Normal" * (18.5 <= imc < 25) + "Alto" * (imc >= 25)
#   print(categoria)
#
# Pista: "Texto" * True = "Texto". "Texto" * False = "" (vacío).
#        Solo UNA de las 3 condiciones va a ser True.
#        El resultado es la suma de los 3 strings (uno será el real,
#        los otros dos serán "").
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.36  [DIFÍCIL]  (SIMPLIFICACIÓN)
# ------------------------------------------------------------------
# Simplificá esta expresión al MÍNIMO:
#
#   (a and b) or (a and not b)
#
# Pista: factorizá como en álgebra.
#        (a and b) or (a and not b) = a and (b or not b)
#        ¿Cuánto vale (b or not b)? Siempre es True.
#        Entonces a and True = ...
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.37  [DIFÍCIL]  (TEST DE MESA)
# ------------------------------------------------------------------
# Para cada caso, ¿qué imprime este programa? (True o False)
#
#   n = int(input("n: "))
#   es_par = (n % 2 == 0)
#   es_positivo = (n > 0)
#   resultado = es_par and es_positivo
#   print(resultado)
#
# Casos:
#   a) n = 4
#   b) n = -3
#   c) n = -2
#   d) n = 7
#
# Pista: recordá que en Python, (-3) % 2 da 1 (no -1).
#        El signo del módulo sigue al DIVISOR.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.38  [DIFÍCIL]  (DEBUGGING)
# ------------------------------------------------------------------
# Este programa calcula un descuento escalonado pero tiene un BUG
# importante. Si el monto es 15000 (descuento del 20%), el total
# debería ser 12000, pero da 18000. Encontrá el bug y corregilo.
#
#   monto = float(input("Monto: "))
#   if monto >= 10000:
#       desc = monto * 0.20
#   elif monto >= 5000:
#       desc = monto * 0.10
#   else:
#       desc = 0
#   total = monto + desc
#   print(f"Total: ${total}")
#
# Pista: el descuento se debe RESTAR del monto, no sumar.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.39  [DIFÍCIL]  (REFACTOR)
# ------------------------------------------------------------------
# Este código verifica si una persona puede jubilarse usando if
# anidados. Reescribilo usando UNA SOLA expresión con and y or:
#
#   edad = 62
#   sexo = "mujer"
#   if sexo == "mujer":
#       if edad >= 60:
#           print(True)
#       else:
#           print(False)
#   else:
#       if edad >= 65:
#           print(True)
#       else:
#           print(False)
#
# Pista: print((sexo == "mujer" and edad >= 60) or (sexo == "hombre" and edad >= 65))
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.40  [DIFÍCIL]  (PROYECTO INTEGRADOR)
# ------------------------------------------------------------------
# Escribí un programa completo que:
#   1) Pida al usuario: nombre, edad, promedio y si hace deporte (sí/no).
#   2) Convierta cada uno al tipo correcto (str, int, float, bool).
#      Para el bool: True si escribió "sí", False si no.
#   3) Verifique si accede a una BECA DEPORTIVA con esta regla:
#        (edad < 25 AND promedio >= 7) AND hace_deporte
#   4) Muestre una ficha con todos los datos + el resultado True/False
#      de la beca.
#   5) Calcule y muestre también:
#        - el doble de la edad (operador *)
#        - si la edad es par (operador % y ==)
#        - el promedio al cuadrado (operador **)
#
# Requisitos: usar TODOS los tipos de operadores vistos
# (aritméticos, comparación, lógicos).
#
# Pista: 4 input() + conversiones + f-string + varias expresiones
#        booleanas y aritméticas.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #  ¡Fin de los 40 ejercicios de complejidad - Lección 3!         #
# #                                                                #
# #  Cuando termines, mandame este archivo .py con tus soluciones  #
# #  y te lo devuelvo corregido ejercicio por ejercicio.           #
# #                                                                #
# ##################################################################
