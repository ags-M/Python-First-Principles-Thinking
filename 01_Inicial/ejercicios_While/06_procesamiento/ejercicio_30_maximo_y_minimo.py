# ============================================================
# Ejercicio 30: Máximo y mínimo
# Categoría: 06_procesamiento
# ============================================================
#
# ENUNCIADO:
# El usuario ingresa números. Cuando ingrese 0, termina. Mostrá el mayor y el menor ingresado.



lista_n = [ ]
n = 1
while n != 0: # ZONA A
    n = int(input("ingresa un numero:  "))
    if n != 0:
     lista_n.append(n)
    else:
       print("se termino el ingreso con cero")

mayor = max(lista_n) # ZONA B
menor = min(lista_n) 
print(f"La lista de los numeros es: {lista_n}") 
print(f" el numero mayor es: {mayor}")
print(f" el numero menor es: {menor}")

"""
### 🔄 Flujo correcto del programa
### 🔄 Ejecución paso a paso

| Etapa              | Acción                                                |
|:-------------------|:------------------------------------------------------|
| 1. Inicializar     | `lista_n = []`, `n = 1`                               |
| 2. Bucle           | Pedir números y agregarlos a la lista (sin el 0)      |
| 3. Fin del bucle   | Cuando `n == 0`, sale del bucle                       |
| 4. **Después**     | Calcular `mayor = max(lista_n)` y `menor = min(...)`  |
| 5. Mostrar         | `print()` con los resultados                          |


_____________________________________________________________________________

📊 Traceo del programa (ejemplo con entrada: 5, 8, 3, 0)
_____________________________________________________________________________

----------------------------------------------------------------
| Paso | Acción                           | Estado de lista_n   |
|:----:|:---------------------------------|:--------------------|
| 1    | Inicializar `lista_n = []`       | `[]`                |
| 2    | Inicializar `n = 1`              | `[]`                |
| 3    | Usuario ingresa `5`              | `[5]`               |
| 4    | Usuario ingresa `8`              | `[5, 8]`            |
| 5    | Usuario ingresa `3`              | `[5, 8, 3]`         |
| 6    | Usuario ingresa `0`              | `[5, 8, 3]` (sin 0) |
| 7    | Sale del bucle                   | `[5, 8, 3]`         |
| 8    | `mayor = max(lista_n)` → 8       | `[5, 8, 3]`         |
| 9    | `menor = min(lista_n)` → 3       | `[5, 8, 3]`         |
| 10   | Imprime resultados               |                     |
_________________________________________________________________

### 🎯 Conceptos aplicados 🧠

| Concepto              | ¿Cómo lo aplicaste?                                   |
|:----------------------|:------------------------------------------------------|
| Bucle `while`         | Mientras el usuario no ingrese 0                      |
| Validación con `if`   | Solo agregar a la lista si `n != 0`                   |
| Listas dinámicas      | `lista_n.append(n)` para acumular valores             |
| Funciones `max/min`   | Calcular mayor y menor después del bucle              |
| ZONA A / ZONA B       | Lógica dentro del bucle vs. resultado final después   |
| Variable centinela    | `n` como señal para terminar el bucle                 |
--------------------------------------------------------------------------------

"""