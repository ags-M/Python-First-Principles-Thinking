# -*- coding: utf-8 -*-
"""
Curso de Python - De cero a experto
LECCIÓN 3: OPERADORES - 40 ejercicios extra

Distribución de dificultad:
  Ejercicios  1 - 15  →  FÁCIL
  Ejercicios 16 - 28  →  MEDIO
  Ejercicios 29 - 40  →  DIFÍCIL

Cómo usar este archivo en VS Code:
  1. Abrí este archivo .py en VS Code.
  2. Leé el enunciado de cada ejercicio (en los comentarios).
  3. Escribí tu solución en el espacio en blanco debajo de "Tu solución:".
  4. Para probar, comentá con # las soluciones anteriores y dejá solo una.

Temas que cubre esta lección:
  - Aritméticos:  +  -  *  /  //  %  **
  - Comparación:  ==  !=  <  >  <=  >=
  - Lógicos:      and   or   not

Tips antes de empezar:
  - La división / SIEMPRE devuelve float, aunque sean enteros.
  - // es división entera (sin decimales).
  - % es módulo (el resto de la división).
  - ** es potencia: 2**3 = 8.
  - Las comparaciones devuelven True o False (bool).
  - and / or / not combinan condiciones.
"""


# ##################################################################
# #                                                                #
# #           NIVEL FÁCIL  (Ejercicios 1 a 15)                     #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.1  [FÁCIL]
# ------------------------------------------------------------------
# Sumá 25 + 17 usando el operador + y mostrá el resultado.
#
# Pista: print(25 + 17)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.2  [FÁCIL]
# ------------------------------------------------------------------
# Restá 100 - 45 usando el operador - y mostrá el resultado.
#
# Pista: print(100 - 45)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.3  [FÁCIL]
# ------------------------------------------------------------------
# Multiplicá 8 * 7 usando el operador * y mostrá el resultado.
#
# Pista: print(8 * 7)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.4  [FÁCIL]
# ------------------------------------------------------------------
# Dividí 100 / 4 y mostrá el resultado.
# Pregunta extra (en comentario): ¿qué tipo de dato devuelve la
# división con /? ¿int o float?
#
# Pista: print(100 / 4)  →  mirá si sale con punto decimal.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.5  [FÁCIL]
# ------------------------------------------------------------------
# Calculá el doble de un número fijo (por ejemplo 25 * 2) y mostralo.
#
# Pista: doble = 25 * 2 ; print(doble)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.6  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario un número entero y mostrá su triple (usando *).
#
# Pista: n = int(input("...")) ; print(n * 3)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.7  [FÁCIL]
# ------------------------------------------------------------------
# Compará si 10 es mayor que 5 usando el operador >.
# Guardá el resultado en una variable y mostrá: debería dar True.
#
# Pista: resultado = 10 > 5
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.8  [FÁCIL]
# ------------------------------------------------------------------
# Compará si "perro" es igual a "gato" usando ==.
# Mostrá el resultado (debería dar False).
#
# Pista: print("perro" == "gato")
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.9  [FÁCIL]
# ------------------------------------------------------------------
# Verificá si 7 es igual a 7 usando == y mostrá el resultado.
#
# Pista: print(7 == 7)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.10  [FÁCIL]
# ------------------------------------------------------------------
# Calculá el resultado de 20 // 6 (división entera) y mostralo.
# Acordate: // devuelve solo la parte entera, sin decimales.
#
# Pista: print(20 // 6)  →  debería dar 3.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.11  [FÁCIL]
# ------------------------------------------------------------------
# Calculá el resultado de 20 % 6 (módulo o resto) y mostralo.
# Acordate: % devuelve el RESTO de la división.
#
# Pista: print(20 % 6)  →  debería dar 2.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.12  [FÁCIL]
# ------------------------------------------------------------------
# Calculá 2 ** 5 (2 elevado a la 5) usando el operador ** (potencia).
# Mostrá el resultado.
#
# Pista: print(2 ** 5)  →  debería dar 32.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.13  [FÁCIL]
# ------------------------------------------------------------------
# Compará si 15 es distinto de 20 usando el operador !=.
# Mostrá el resultado.
#
# Pista: print(15 != 20)  →  debería dar True.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.14  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su edad (como int) y mostrá True o False indicando
# si es mayor o igual a 18 (usá el operador >=).
# NO uses if.
#
# Pista: print(edad >= 18)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.15  [FÁCIL]
# ------------------------------------------------------------------
# Mostrá el resultado de comparar si 100 es menor que 50 (usá <).
# Debería dar False.
#
# Pista: print(100 < 50)
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL MEDIO  (Ejercicios 16 a 28)                    #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.16  [MEDIO]
# ------------------------------------------------------------------
# Calculá el promedio de 4 números fijos: 6, 7, 8 y 9.
# Usá + para sumar y / para dividir por 4.
# Mostrá el resultado.
#
# Pista: promedio = (6 + 7 + 8 + 9) / 4
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.17  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario dos números (como int) y mostrá las cuatro
# operaciones básicas en mensajes separados:
#   suma, resta, multiplicación y división.
#
# Pista: cuatro print() usando +, -, *, /.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.18  [MEDIO]
# ------------------------------------------------------------------
# Calculá el área de un triángulo con valores fijos:
#   base = 10, altura = 5
# Fórmula: area = (base * altura) / 2
# Mostrá el resultado.
#
# Pista: ojo con los paréntesis, van sí o sí.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.19  [MEDIO]
# ------------------------------------------------------------------
# Calculá el precio con IVA (21%) de un producto.
# Precio fijo: 1000.
# Fórmula: precio_final = precio * 1.21
# Mostrá el resultado con un mensaje claro.
#
# Pista: 1.21 = 1 + 0.21  (100% + 21% de IVA).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.20  [MEDIO]
# ------------------------------------------------------------------
# Convertí kilómetros a millas.
# 1 kilómetro = 0.621371 millas.
# Pedí al usuario los kilómetros (float) y mostrá el equivalente
# en millas.
#
# Pista: millas = km * 0.621371
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.21  [MEDIO]
# ------------------------------------------------------------------
# Verificá si un número es PAR.
# Pedí al usuario un número entero y mostrá True o False.
# Un número es par si el resto de dividirlo por 2 es 0.
# Usá % y ==. NO uses if.
#
# Pista: print((numero % 2) == 0)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.22  [MEDIO]
# ------------------------------------------------------------------
# Calculá el área de un círculo.
# Fórmula: area = pi * radio²
# Usá pi = 3.14159 (como constante).
# Pedí al usuario el radio (float) y mostrá el área.
# Para el cuadrado del radio usá el operador **.
#
# Pista: area = 3.14159 * (radio ** 2)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.23  [MEDIO]
# ------------------------------------------------------------------
# Verificá si la edad ingresada por el usuario está entre 18 y 65
# (ambos incluidos).
# Usá dos comparaciones unidas con and.
# Mostrá True o False.
#
# Pista: 18 <= edad and edad <= 65
#   o más corto: 18 <= edad <= 65
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.24  [MEDIO]
# ------------------------------------------------------------------
# Combiná dos condiciones con and.
# Variables fijas:
#   edad       = 20
#   tiene_dni  = True
# Mostrá el resultado de verificar si puede votar
# (edad >= 18 AND tiene_dni).
#
# Pista: print((edad >= 18) and tiene_dni)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.25  [MEDIO]
# ------------------------------------------------------------------
# Calculá un descuento del 10% si el precio supera 1000.
# Precio fijo: 1500.
# Si precio > 1000, el descuento es precio * 0.10. Sino, 0.
# Mostrá el descuento aplicado.
# (Podés usar el operador condicional: descuento = precio*0.10
#  if precio > 1000 else 0  — o una expresión más simple con bool.)
#
# Pista: una sola línea con if/else "en línea".
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.26  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario un número entero y mostrá su tabla de multiplicar
# del 1 al 5. Sin usar bucles: cinco print() separados.
# Cada línea: "N x 1 = resultado"
#
# Pista: print(f"{n} x 1 = {n * 1}")  ...repetilo hasta x 5.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.27  [MEDIO]
# ------------------------------------------------------------------
# Calculá el tiempo total en minutos.
# Pedí al usuario:
#   - horas (int)
#   - minutos (int)
# Mostrá el total convertido todo a minutos.
#
# Pista: total = (horas * 60) + minutos
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.28  [MEDIO]
# ------------------------------------------------------------------
# Verificá si un año es divisible por 4 (primer paso de la regla
# de bisiesto, sin verificar lo de 100 y 400 todavía).
# Pedí el año al usuario (int) y mostrá True o False.
#
# Pista: print((anio % 4) == 0)
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL DIFÍCIL  (Ejercicios 29 a 40)                  #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.29  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá el sueldo neto de un trabajador.
# Variables fijas:
#   sueldo_bruto = 500000
# Descuentos:
#   - jubilación: 11%
#   - obra social: 3%
# También calculá el aguinaldo (sueldo_bruto / 12).
# Mostrá el desglose de cada descuento, el aguinaldo y el sueldo
# neto final (bruto - jubilación - obra social).
#
# Pista:
#   jubilacion = sueldo_bruto * 0.11
#   obra_social = sueldo_bruto * 0.03
#   aguinaldo = sueldo_bruto / 12
#   neto = sueldo_bruto - jubilacion - obra_social
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.30  [DIFÍCIL]
# ------------------------------------------------------------------
# Verificá si un año es bisiesto aplicando la regla completa:
#   - es divisible por 4  Y
#   - (NO divisible por 100  O  divisible por 400)
# Combiná %, and, or y not.
# Probá con: 2024 (sí), 1900 (no), 2000 (sí).
# Mostrá el resultado para cada uno.
#
# Pista:
#   bisiesto = (anio % 4 == 0) and ((not anio % 100 == 0) or (anio % 400 == 0))
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.31  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculadora de propina.
# Pedí al usuario:
#   - monto_total de la cuenta (float)
#   - porcentaje de propina (int, por ejemplo 10)
#   - cantidad de comensales (int)
# Calculá:
#   - propina total = monto * porcentaje / 100
#   - propina por persona = propina_total / comensales
#   - total por persona = (monto + propina_total) / comensales
# Mostrá los tres resultados.
#
# Pista: tres fórmulas encadenadas, una usa la anterior.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.32  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá un descuento escalonado.
# Pedí al usuario el monto de la compra (float).
# Reglas:
#   - si la compra es >= 10000  →  descuento del 20%
#   - si es >= 5000             →  descuento del 10%
#   - sino                      →  descuento del 0%
# Mostrá el descuento aplicado y el precio final.
#
# Pista: tres condiciones anidadas con if/elif/else, o dos if
# anidados. (Si todavía no querés usar if, podés armar una
# expresión con comparaciones y multiplicación de bool.)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.33  [DIFÍCIL]
# ------------------------------------------------------------------
# Verificá si una persona puede jubilarse.
# Variables:
#   edad     = 62
#   sexo     = "mujer"  (o "hombre")
# Reglas:
#   - mujeres: edad >= 60
#   - hombres: edad >= 65
# Combiná comparaciones con and y or.
# Mostrá True o False.
#
# Pista: (sexo == "mujer" and edad >= 60) or (sexo == "hombre" and edad >= 65)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.34  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá el costo total de un viaje.
# Variables:
#   dias              = 5
#   precio_hotel      = 8000    (por noche)
#   precio_comida     = 3000    (por día)
#   precio_transporte = 15000   (total fijo)
#   cantidad_excursiones = 3
#   precio_excursion  = 4500    (cada una)
# Calculá cada subtotal y el total. Mostrá un desglose claro.
#
# Pista:
#   hotel = dias * precio_hotel
#   comida = dias * precio_comida
#   excursiones = cantidad_excursiones * precio_excursion
#   total = hotel + comida + precio_transporte + excursiones
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.35  [DIFÍCIL]
# ------------------------------------------------------------------
# Convertí una temperatura de Celsius a Fahrenheit y Kelvin en el
# MISMO programa.
# Pedí al usuario la temperatura en Celsius (float).
# Fórmulas:
#   Fahrenheit = (Celsius * 9/5) + 32
#   Kelvin = Celsius + 273.15
# Mostrá los dos resultados con mensajes claros.
#
# Pista: dos operaciones con la misma variable de entrada.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.36  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá el IMC (Índice de Masa Corporal) y mostrá la categoría.
# Pedí al usuario: peso (kg) y altura (m), ambos como float.
# Fórmula: imc = peso / (altura ** 2)
# Mostrá el IMC con un mensaje y, debajo, la categoría usando
# comparaciones (sin if):
#   - "Bajo peso" si imc < 18.5
#   - "Normal" si 18.5 <= imc < 25
#   - "Sobrepeso" si 25 <= imc < 30
#   - "Obesidad" si imc >= 30
# Para mostrar la categoría sin if, podés usar el truco de
# multiplicar strings por bools:
#   "Bajo peso" * (imc < 18.5) + "Normal" * (18.5 <= imc < 25) + ...
#
# Pista: una comparación por categoría, concatenadas con +.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.37  [DIFÍCIL]
# ------------------------------------------------------------------
# Verificá si tres lados pueden formar un triángulo válido.
# Regla: la suma de cualquier par de lados debe ser MAYOR que el
# tercero. Es decir, tres condiciones con and:
#   (a + b > c) and (a + c > b) and (b + c > a)
# Variables fijas:
#   a = 5, b = 7, c = 10   (debería dar True)
# Mostrá el resultado.
# Probá también con: a = 1, b = 2, c = 10  (debería dar False)
#
# Pista: una sola expresión con tres comparaciones unidas con and.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.38  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá la cuota mensual de un préstamo.
# Pedí al usuario:
#   - monto del préstamo (float)
#   - tasa de interés anual (float, por ejemplo 0.12 para 12%)
#   - plazo en meses (int)
# Fórmula simplificada (cuota fija):
#   cuota = (monto * tasa / 12) / (1 - (1 + tasa/12) ** -plazo)
# Mostrá la cuota mensual con 2 decimales.
# Si la fórmula te asusta, hacé una versión más simple:
#   cuota = (monto * (1 + tasa)) / plazo
#
# Pista: usá f"{cuota:.2f}" para mostrar con 2 decimales.
#        El operador ** con número negativo funciona igual.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.39  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá la nota final con pesos.
# Variables:
#   practicos = 8.0    (peso 30%)
#   parcial   = 7.5    (peso 30%)
#   final     = 6.0    (peso 40%)
# Fórmula:
#   nota_final = practicos * 0.30 + parcial * 0.30 + final * 0.40
# Mostrá la nota final y, debajo, True o False indicando si
# aprobó (nota_final >= 4). Usá la comparación con >=.
#
# Pista: una suma de tres productos + una comparación con >=.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.40  [DIFÍCIL]
# ------------------------------------------------------------------
# Programa de beca universitaria.
# Variables:
#   edad                    = 22
#   promedio                = 8.5
#   tiene_solicitud_especial = False
# Regla para conseguir la beca:
#   - edad < 25  Y  promedio >= 8
#   - O  tiene_solicitud_especial = True
# Combiná and y or.
# Mostrá True o False indicando si le dan la beca.
# Probá con dos casos distintos cambiando las variables:
#   Caso A: edad=22, promedio=8.5, solicitud=False  → True
#   Caso B: edad=30, promedio=9.0, solicitud=False  → False
#   Caso C: edad=30, promedio=9.0, solicitud=True   → True
#
# Pista:
#   beca = ((edad < 25) and (promedio >= 8)) or tiene_solicitud_especial
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #  ¡Fin de los 40 ejercicios extra de la Lección 3!              #
# #                                                                #
# #  Cuando termines, mandame este archivo .py con tus soluciones  #
# #  y te lo devuelvo corregido ejercicio por ejercicio.           #
# #                                                                #
# ##################################################################
