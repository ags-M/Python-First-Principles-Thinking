# -*- coding: utf-8 -*-
"""
Curso de Python - De cero a experto
LECCIÓN 3: OPERADORES - 50 ejercicios extra

Distribución de dificultad:
  Ejercicios  1 - 20  →  FÁCIL
  Ejercicios 21 - 35  →  MEDIO
  Ejercicios 36 - 50  →  DIFÍCIL

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
# #           NIVEL FÁCIL  (Ejercicios 1 a 20)                     #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.1  [FÁCIL]
# ------------------------------------------------------------------
# Sumá 50 + 23 usando el operador + y mostrá el resultado.
#
# Pista: print(50 + 23)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.2  [FÁCIL]
# ------------------------------------------------------------------
# Restá 200 - 78 usando el operador - y mostrá el resultado.
#
# Pista: print(200 - 78)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.3  [FÁCIL]
# ------------------------------------------------------------------
# Multiplicá 9 * 6 usando el operador * y mostrá el resultado.
#
# Pista: print(9 * 6)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.4  [FÁCIL]
# ------------------------------------------------------------------
# Dividí 144 / 12 y mostrá el resultado.
# Pregunta extra (en comentario): ¿qué tipo de dato devuelve la
# división con /? ¿int o float?
#
# Pista: print(144 / 12)  →  mirá si sale con punto decimal.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.5  [FÁCIL]
# ------------------------------------------------------------------
# Calculá la mitad de 100 usando el operador / y mostrala.
#
# Pista: mitad = 100 / 2 ; print(mitad)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.6  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario un número entero y mostrá su doble (usando *).
#
# Pista: n = int(input("...")) ; print(n * 2)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.7  [FÁCIL]
# ------------------------------------------------------------------
# Compará si 20 es mayor que 15 usando el operador >.
# Guardá el resultado en una variable y mostrá: debería dar True.
#
# Pista: resultado = 20 > 15
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.8  [FÁCIL]
# ------------------------------------------------------------------
# Compará si "rojo" es igual a "azul" usando ==.
# Mostrá el resultado (debería dar False).
#
# Pista: print("rojo" == "azul")
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.9  [FÁCIL]
# ------------------------------------------------------------------
# Verificá si 100 es igual a 100 usando == y mostrá el resultado.
#
# Pista: print(100 == 100)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.10  [FÁCIL]
# ------------------------------------------------------------------
# Calculá el resultado de 25 // 4 (división entera) y mostralo.
# Acordate: // devuelve solo la parte entera, sin decimales.
#
# Pista: print(25 // 4)  →  debería dar 6.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.11  [FÁCIL]
# ------------------------------------------------------------------
# Calculá el resultado de 25 % 4 (módulo o resto) y mostralo.
# Acordate: % devuelve el RESTO de la división.
#
# Pista: print(25 % 4)  →  debería dar 1.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.12  [FÁCIL]
# ------------------------------------------------------------------
# Calculá 3 ** 4 (3 elevado a la 4) usando el operador ** (potencia).
# Mostrá el resultado.
#
# Pista: print(3 ** 4)  →  debería dar 81.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.13  [FÁCIL]
# ------------------------------------------------------------------
# Compará si 50 es distinto de 30 usando el operador !=.
# Mostrá el resultado.
#
# Pista: print(50 != 30)  →  debería dar True.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.14  [FÁCIL]
# ------------------------------------------------------------------
# Pedí al usuario su edad (como int) y mostrá True o False indicando
# si es mayor o igual a 21 (usá el operador >=).
# NO uses if.
#
# Pista: print(edad >= 21)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.15  [FÁCIL]
# ------------------------------------------------------------------
# Mostrá el resultado de comparar si 200 es menor que 100 (usá <).
# Debería dar False.
#
# Pista: print(200 < 100)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.16  [FÁCIL]
# ------------------------------------------------------------------
# Sumá tres números fijos: 1000 + 250 + 75 usando el operador +
# y mostrá el resultado.
#
# Pista: print(1000 + 250 + 75)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.17  [FÁCIL]
# ------------------------------------------------------------------
# Calculá cuántas unidades hay en 8 docenas usando *.
# Una docena = 12 unidades.
# Mostrá el resultado.
#
# Pista: print(8 * 12)  →  debería dar 96.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.18  [FÁCIL]
# ------------------------------------------------------------------
# Compará si 5 es mayor o igual a 5 usando >=.
# Mostrá el resultado (debería dar True).
#
# Pista: print(5 >= 5)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.19  [FÁCIL]
# ------------------------------------------------------------------
# Calculá el resultado de 10 - 3 + 7 y mostralo.
# Acordate: las operaciones se evalúan de izquierda a derecha
# cuando todas tienen la misma prioridad.
#
# Pista: print(10 - 3 + 7)  →  debería dar 14.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.20  [FÁCIL]
# ------------------------------------------------------------------
# Verificá si "hola" es distinto de "chau" usando !=.
# Mostrá el resultado.
#
# Pista: print("hola" != "chau")  →  debería dar True.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL MEDIO  (Ejercicios 21 a 35)                    #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.21  [MEDIO]
# ------------------------------------------------------------------
# Calculá el promedio de 5 números fijos: 10, 20, 30, 40 y 50.
# Usá + para sumar y / para dividir por 5.
# Mostrá el resultado.
#
# Pista: promedio = (10 + 20 + 30 + 40 + 50) / 5
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.22  [MEDIO]
# ------------------------------------------------------------------
# Pedí al usuario dos números (como int): base y exponente.
# Mostrá dos resultados en mensajes separados:
#   - la potencia:   base ** exponente
#   - el módulo:     base % exponente
#
# Pista: dos print() usando ** y %.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.23  [MEDIO]
# ------------------------------------------------------------------
# Calculá el área de un cuadrado con lado fijo:  lado = 8
# Fórmula: area = lado ** 2
# Mostrá el resultado.
#
# Pista: el operador ** sirve para elevar al cuadrado.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.24  [MEDIO]
# ------------------------------------------------------------------
# Calculá el precio con IVA (10%) de un producto.
# Precio fijo: 500.
# Fórmula: precio_final = precio * 1.10
# Mostrá el resultado con un mensaje claro.
#
# Pista: 1.10 = 1 + 0.10  (100% + 10% de IVA).
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.25  [MEDIO]
# ------------------------------------------------------------------
# Convertí millas a kilómetros.
# 1 milla = 1.60934 kilómetros.
# Pedí al usuario las millas (float) y mostrá el equivalente
# en kilómetros.
#
# Pista: km = millas * 1.60934
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.26  [MEDIO]
# ------------------------------------------------------------------
# Verificá si un número es MÚLTIPLO DE 5.
# Pedí al usuario un número entero y mostrá True o False.
# Un número es múltiplo de 5 si el resto de dividirlo por 5 es 0.
# Usá % y ==. NO uses if.
#
# Pista: print((numero % 5) == 0)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.27  [MEDIO]
# ------------------------------------------------------------------
# Calculá el perímetro de un círculo.
# Fórmula: perimetro = 2 * pi * radio
# Usá pi = 3.14159 (como constante).
# Pedí al usuario el radio (float) y mostrá el perímetro.
#
# Pista: perimetro = 2 * 3.14159 * radio
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.28  [MEDIO]
# ------------------------------------------------------------------
# Verificá si la edad ingresada por el usuario corresponde a un
# adolescente (entre 12 y 18 años, ambos incluidos).
# Usá dos comparaciones unidas con and.
# Mostrá True o False.
#
# Pista: 12 <= edad <= 18
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.29  [MEDIO]
# ------------------------------------------------------------------
# Combiná dos condiciones con and.
# Variables fijas:
#   edad           = 25
#   tiene_licencia = True
# Mostrá el resultado de verificar si puede manejar
# (edad >= 18 AND tiene_licencia).
#
# Pista: print((edad >= 18) and tiene_licencia)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.30  [MEDIO]
# ------------------------------------------------------------------
# Calculá un descuento del 15% si el precio supera 5000.
# Precio fijo: 7500.
# Si precio > 5000, el descuento es precio * 0.15. Sino, 0.
# Mostrá el descuento aplicado.
# (Podés usar el operador condicional: descuento = precio*0.15
#  if precio > 5000 else 0  — o una expresión más simple con bool.)
#
# Pista: una sola línea con if/else "en línea".
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.31  [MEDIO]
# ------------------------------------------------------------------
# Mostrá la tabla de multiplicar del 7 del 1 al 5.
# Sin usar bucles: cinco print() separados.
# Cada línea: "7 x 1 = 7"
#
# Pista: print(f"7 x 1 = {7 * 1}")  ...repetilo hasta x 5.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.32  [MEDIO]
# ------------------------------------------------------------------
# Calculá cuántos segundos hay en una cantidad de días.
# Pedí al usuario los días (int).
# Mostrá el total convertido a segundos.
#
# Pista: total = dias * 24 * 60 * 60
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.33  [MEDIO]
# ------------------------------------------------------------------
# Verificá si un número es divisible por 7.
# Pedí el número al usuario (int) y mostrá True o False.
#
# Pista: print((numero % 7) == 0)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.34  [MEDIO]
# ------------------------------------------------------------------
# Calculá cuánta pintura sobra después de pintar paredes.
# Variables fijas:
#   tengo_pintura = 10       (litros)
#   por_pared     = 2        (litros por pared)
#   paredes       = 3        (cantidad de paredes)
# Mostrá el resultado: tengo_pintura - (por_pared * paredes).
#
# Pista: sobrante = tengo_pintura - (por_pared * paredes)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.35  [MEDIO]
# ------------------------------------------------------------------
# Convertí una temperatura de Celsius a Fahrenheit.
# Pedí al usuario la temperatura en Celsius (float).
# Fórmula: Fahrenheit = (Celsius * 9/5) + 32
# Mostrá el resultado con un mensaje claro.
#
# Pista: una sola operación con la variable de entrada.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #           NIVEL DIFÍCIL  (Ejercicios 36 a 50)                  #
# #                                                                #
# ##################################################################


# ------------------------------------------------------------------
# Ej. 3.36  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá la ganancia de un negocio.
# Variables fijas:
#   costo         = 4500       (int, costo unitario)
#   precio_venta  = 6800       (int, precio de venta unitario)
#   cantidad      = 30         (int, unidades vendidas)
# Calculá:
#   - ganancia_bruta = (precio_venta - costo) * cantidad
#   - margen_pct = (precio_venta - costo) / precio_venta * 100
# Mostrá ambos resultados.
#
# Pista: dos fórmulas usando las mismas variables.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.37  [DIFÍCIL]
# ------------------------------------------------------------------
# Verificá si un número cumple TRES condiciones al mismo tiempo:
#   - es par
#   - es positivo (> 0)
#   - es menor a 100
# Pedí el número al usuario (int).
# Combiná tres comparaciones con and.
# Mostrá True o False.
#
# Pista: (n % 2 == 0) and (n > 0) and (n < 100)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.38  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá una factura de electricidad.
# Variables fijas:
#   lectura_anterior = 12500    (int, kWh)
#   lectura_actual   = 13200    (int, kWh)
#   precio_kwh       = 125.50   (float, $ por kWh)
#   iva              = 0.21     (float, 21%)
# Calculá:
#   - consumo = lectura_actual - lectura_anterior
#   - subtotal = consumo * precio_kwh
#   - total = subtotal * (1 + iva)
# Mostrá el consumo, el subtotal y el total.
#
# Pista: tres fórmulas encadenadas, cada una usa la anterior.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.39  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá un descuento escalonado con cuatro rangos.
# Pedí al usuario el monto de la compra (float).
# Reglas:
#   - si la compra es >= 100000  →  descuento del 30%
#   - si es >= 50000             →  descuento del 20%
#   - si es >= 20000             →  descuento del 10%
#   - sino                       →  descuento del 5%
# Mostrá el descuento aplicado y el precio final.
#
# Pista: cuatro condiciones anidadas con if/elif/else.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.40  [DIFÍCIL]
# ------------------------------------------------------------------
# Verificá si una persona puede alquilar un auto.
# Combiná TRES condiciones con and.
# Variables:
#   edad            = 25
#   tiene_licencia  = True
#   tiene_tarjeta   = True
# Regla: edad >= 21 AND tiene_licencia AND tiene_tarjeta
# Mostrá True o False.
#
# Pista: tres comparaciones unidas con and.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.41  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá el costo total de una reserva de hotel.
# Variables:
#   dias              = 4
#   precio_noche      = 12000    (por noche)
#   precio_desayuno   = 2500     (por día)
#   cantidad_extras   = 2        (servicios extra como spa o lavandería)
#   precio_extra      = 3500     (cada servicio extra)
# Calculá cada subtotal y el total:
#   - hotel = dias * precio_noche
#   - desayuno = dias * precio_desayuno
#   - extras = cantidad_extras * precio_extra
#   - total = hotel + desayuno + extras
# Mostrá un desglose claro.
#
# Pista: cuatro fórmulas, tres subtotales + el total final.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.42  [DIFÍCIL]
# ------------------------------------------------------------------
# Convertí una velocidad de km/h a m/s y a mph en el MISMO programa.
# Pedí al usuario la velocidad en km/h (float).
# Fórmulas:
#   m/s = km/h / 3.6
#   mph = km/h / 1.60934
# Mostrá los dos resultados con mensajes claros.
#
# Pista: dos operaciones con la misma variable de entrada.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.43  [DIFÍCIL]
# ------------------------------------------------------------------
# Compará los promedios de dos alumnos (sin usar if).
# Variables fijas:
#   promedio_a = 8.5
#   promedio_b = 7.2
# Mostrá dos booleanos:
#   - ¿A tiene mayor promedio que B?  →  (promedio_a > promedio_b)
#   - ¿B tiene mayor promedio que A?  →  (promedio_b > promedio_a)
# Cada uno en su print().
#
# Pista: dos comparaciones con > y dos print().
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.44  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá el interés compuesto.
# Variables fijas:
#   principal = 100000       (float, monto inicial)
#   tasa      = 0.10         (float, 10% anual)
#   años      = 5            (int)
# Fórmula: monto_final = principal * (1 + tasa) ** años
# Mostrá el monto final con 2 decimales.
#
# Pista: usá f"{monto_final:.2f}" para mostrar con 2 decimales.
#        El operador ** también funciona con potencias enteras.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.45  [DIFÍCIL]
# ------------------------------------------------------------------
# Clasificá a un cliente según sus compras (sin usar if).
# Variables:
#   total_compras = 120000       (float)
#   frecuencia    = 12           (int, compras por mes)
# Mostrá cuatro líneas indicando True/False para cada categoría:
#   - "¿Cliente VIP?"    →  total >= 100000 AND frecuencia >= 10
#   - "¿Cliente Gold?"   →  total >= 50000  AND frecuencia >= 5
#   - "¿Cliente Silver?" →  total >= 20000  AND frecuencia >= 2
#   - "¿Cliente Nuevo?"  →  total < 20000   OR  frecuencia < 2
# Cada línea con un print() que use comparaciones y and/or.
#
# Pista: cuatro print() con expresiones booleanas distintas.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.46  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá la nota final con pesos (distintos a otros ejercicios).
# Variables:
#   tp1     = 8.0    (peso 15%)
#   tp2     = 9.0    (peso 15%)
#   parcial = 7.5    (peso 30%)
#   final   = 9.0    (peso 40%)
# Fórmula:
#   nota_final = tp1*0.15 + tp2*0.15 + parcial*0.30 + final*0.40
# Mostrá la nota final y, debajo, True o False indicando si
# aprobó (nota_final >= 4). Usá la comparación con >=.
#
# Pista: una suma de cuatro productos + una comparación con >=.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.47  [DIFÍCIL]
# ------------------------------------------------------------------
# Programa de beca deportiva universitaria.
# Variables:
#   edad               = 20
#   promedio           = 8.0
#   hace_deporte       = True
#   solicitud_especial = False
# Regla para conseguir la beca:
#   - (edad < 25 AND promedio >= 7) AND (hace_deporte OR solicitud_especial)
# Combiná and y or.
# Mostrá True o False indicando si le dan la beca.
# Probá con dos casos distintos cambiando las variables:
#   Caso A: edad=20, promedio=8, deporte=True, solicitud=False   → True
#   Caso B: edad=30, promedio=9, deporte=True, solicitud=False   → False
#
# Pista:
#   beca = ((edad < 25) and (promedio >= 7)) and (hace_deporte or solicitud_especial)
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.48  [DIFÍCIL]
# ------------------------------------------------------------------
# Verificá si tres lados forman un triángulo válido Y si además
# es un triángulo rectángulo (cumple el teorema de Pitágoras).
# Variables fijas:
#   a = 3, b = 4, c = 5   (debería dar True en ambas)
# Combiná en una sola expresión con and:
#   - es_válido:    (a+b > c) and (a+c > b) and (b+c > a)
#   - es_rectángulo: (a**2 + b**2 == c**2)
# Mostrá el resultado final (True solo si cumple ambas).
#
# Pista: una sola expresión con varias comparaciones unidas con and.
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.49  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá el total de una factura de agua.
# Variables:
#   litros_consumidos = 18000       (int, litros en el mes)
#   cargo_fijo        = 1500        (float, $ fijo mensual)
#   tasa_variable     = 0.05        (float, $ por litro)
#   iva               = 0.21        (float, 21%)
# Calculá:
#   - subtotal = cargo_fijo + (litros_consumidos * tasa_variable)
#   - total = subtotal * (1 + iva)
# Mostrá el subtotal y el total, ambos con 2 decimales.
#
# Pista: dos fórmulas encadenadas + f"{variable:.2f}".
#
# --- Tu solución: -------------------------------------------------


# ------------------------------------------------------------------
# Ej. 3.50  [DIFÍCIL]
# ------------------------------------------------------------------
# Calculá la eficiencia de combustible de un auto.
# Variables:
#   km_recorridos  = 480       (int, kilómetros recorridos)
#   litros_usados  = 32        (float, litros consumidos)
# Calculá DOS indicadores:
#   - rendimiento = km_recorridos / litros_usados   (km por litro)
#   - consumo = (litros_usados * 100) / km_recorridos  (litros cada 100 km)
# Mostrá los dos resultados con mensajes claros.
#
# Pista: dos fórmulas con las mismas variables de entrada.
#
# --- Tu solución: -------------------------------------------------


# ##################################################################
# #                                                                #
# #  ¡Fin de los 50 ejercicios extra de la Lección 3!              #
# #                                                                #
# #  Cuando termines, mandame este archivo .py con tus soluciones  #
# #  y te lo devuelvo corregido ejercicio por ejercicio.           #
# #                                                                #
# ##################################################################
