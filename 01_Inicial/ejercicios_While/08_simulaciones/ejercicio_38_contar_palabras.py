# ============================================================
# Ejercicio 38: Contar palabras
# Categoría: 08_simulaciones
# ============================================================
#
TABLA_PILARES = """ logica de programacion:
_____________________________________________________________________________________________________________
| # | PILAR       | PREGUNTA           | EN PYTHON                | ANALOGIA: el mate                        |
|---|-------------|--------------------|--------------------------|------------------------------------------|
| 1 | Secuencia   |  En que orden?     | Sentencias una tras otra | Hervir, poner la bolsita de TE, servir   |
| 2 | Seleccion   |  Que camino tomo?  | if / elif / else         | Ya hirvio? Si si, sirvo; si no, espero.  |
| 3 | Repeticion  |  Hasta cuando?     | while (despues, for)     | Mientras no hierva, sigo calentando.     |

Regla de oro: la tabla de estado o Traceo va ANTES del codigo. El codigo solo la traduce.
"""
"""
| CAPA       | PREGUNTA           | QUÉ ES                          | en algun ejercicio        |
|------------|--------------------|---------------------------------|---------------------------|
| Datos      | #¿Qué tengo ?      | Variables y tipos               | contador, acumulador      |
| Condición  | #¿Qué comparo?     | Expresión que da True o False   | saldo < 100               |
| Secuencia  | #¿En qué orden?    | Pasos uno tras otro             | leer, sumar, imprimir     |
| Selección  | #¿Qué camino tomo? | if / elif / else                | if saldo >= 100           |
| Repetición | #¿Hasta cuándo?    | while                           | while frase != "fin"      |
| Traceo     | #¿Cómo lo verifico?| Tabla de estado en papel        | una fila por iteración    |
"""
"""
# __________________________________________________________________________________________________________

# ENUNCIADO:
# El usuario ingresa frases. Cuando escriba 'fin', termina. 
# Mostrá el total de palabras ingresadas (contá espacios + 1).


La lógica de contar palabras: VER teorico.py 

📊 Traceo manual o Tabla de Estado:

CASO A: "hola mundo" 
CASO B: "uno dos tres" 
CASO C: "grito" 
CASO D: "fin"
| Paso | dato leído  | dato == "fin"?  | espacios + 1  | total antes | total después  | ¿sigo? |
|------|-------------|--------------- -|---------------|-------------|----------------|--------|
| 1    |hola mundo   |      no         |     2         |     0       |       2        |  si    |
| 2    |uno dos tres |      no         |     3         |     2       |       5        |  si    |
| 3    |   grito     |      no         |     1         |     5       |       6        |  si
| 4    |     fin     |      si         |     -         |     -       |       -        |  no --> sale del bucle
-----------------------------------------------------------------------------------------------
digo fin TERMINA

"""
total = 0
frase = 0

while frase!= "fin":
    
    frase = input("ingresa una palabra: ").lower()
    
    if frase != "fin":
        total += frase.count(" ") + 1

print("Total de palabras:", total)
#_________________________________________________________________________

print("----"*50)
#__________________________________________________________________________

#EJEMPO BASICO:

frase = "hola mundo desde python"
cantidad = frase.count(" ") + 1
print(cantidad)  # → 4 (3 espacios + 1 = 4 palabras)

#_________________________________________________________________________

print("----"*50)
#__________________________________________________________________________

# otra modalidad de resolucion del codigo
total_palabras = 0

while True:
    frase = input("Ingresá una frase (o 'fin' para terminar): ").strip().lower()
    
    if frase == "fin":
        break
    
    # Contar palabras de esta frase
    contador_palabras = frase.count(" ") + 1
    total_palabras += contador_palabras
    
    print(f"Esta frase tiene {contador_palabras} palabras")

print(f"\nTotal de palabras ingresadas: {total_palabras}")

#_________________________________________________________________________

print("----"*50)
#__________________________________________________________________________

# UTILIZAR SPLIT (forma una lista de una frase y despues con len() contamos las palabras)

total_palabras = 0

while True:
    # 1. Pedimos la frase y la pasamos a minúsculas (aún es un texto, no una lista)
    texto = input("📝 Escribe una frase (o 'fin' para salir): ").lower()
    
    # 2. Comprobamos si escribió "fin" para salir
    if texto == "fin":
        break
        
    # 3. Si no es "fin", ahora sí separamos el texto en una lista de palabras
    lista_palabras = texto.split()
    
    # 4. Sumamos la longitud de esa lista al total (usando len())
    total_palabras += len(lista_palabras)

# 5. Mostramos el resultado final
print(f"\n✨ ¡Terminaste! La cantidad total de palabras es: {total_palabras} ✨")
     
#_________________________________________________________________________

print("----"*50)
#__________________________________________________________________________



















