"""
📝CONSIGNA:

Calcular la potencia de un número (base elevada a exponente) usando solo while, 
sin usar el operador ** de Python.

"""

# 💻 Código resuelto:

# 1. Pedimos los datos al usuario
base = int(input("Ingresá la base: "))
exponente = int(input("Ingresá el exponente (entero >= 0): "))

# 2. Inicializamos el acumulador multiplicativo en 1.
# ¿Por qué 1? Porque 1 es el "neutro" de la multiplicación (1 * X = X).
# Además, matemáticamente, cualquier número elevado a la 0 es 1.
resultado_potencia = 1
# 3. El contador empieza en 0 para contar cuántas veces multiplicamos.
contador = 0

# 4. Mientras no hayamos multiplicado la cantidad de veces del exponente, seguimos.
while contador < exponente:
    resultado_potencia = resultado_potencia * base   # Acumulamos la multiplicación
    contador = contador + 1        # Avanzamos el contador

# 5. Mostramos el resultado final
print(f"{base} elevado a la {exponente} es: {resultado_potencia}")

#_____________________________________________________________________________________________________________
"""
📊 Traceo manual (hacelo en papel para base = 2, exponente = 3) / el contador = 0 y resultado = 1 
_____________________________________________________________________________________________________________
#                                           aca esta el acumulador
Iteración  contador    ¿contador < 3?             Operación                 contador después
             valor    contador < exponente     (resultado * base)         al final (contador +=1)          
          de entrada
_____________________________________________________________________________________________________________

  1           0              Sí                  1 * 2  =   2                     1
                            0 < 3             
_____________________________________________________________________________________________________________

  2           1              Sí                  2 * 2  =    4                     2
                            1 < 3           
_____________________________________________________________________________________________________________

  3           2              Sí                  4 * 2  =    8                        3
                            2 < 3           
____________________________________________________________________________________________________________

  4           3             3 < 3   FALSE    sale del Bucle                       —
______________________________________________________________________________________________________________

Resultado: 8 ✅ (2³ = 8)
                                   

"""
