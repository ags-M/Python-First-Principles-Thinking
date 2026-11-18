"""
______________________________________________________________________________________________________________

14/11/26
                             tema validacion:

🔑 Concepto clave : Este patrón se llama "Bucle de validación" o "Centinela" es decir 1, 2 y 3. 
La estructura siempre es: 
1.- Pedir el dato. 
2.- while si ej. edad < 0 or edad > 120 si ingresa 122 es TRUE
                                           resulta por print dato PONES es inválido: mostrar error y volver a pedir.
3.- Continuar con el programa (ahora sí, con un dato seguro). 
                              SI ingresa 33 es FALSE y entonces imprime print dato valido
______________________________________________________________________________________________________________


### 📊 TABLA RESUMEN: ¿EMPEZAR EN 0 O EN 1? (Patrón de Inicialización)

| Concepto               | Inicio | Por qué                                          | Ejemplo en código        |
|------------------------|:------:|--------------------------------------------------|--------------------------|
| Iteraciones / Vueltas  |   1    | Cuenta ejecuciones del bloque de código.         | Fila 1, Fila 2 del traceo|
| Acumuladores           |   0    | Valor base antes de sumar o construir.           | `invertido = 0`          |
| Contadores de intentos |   0    | Cantidad de intentos realizados antes de empezar.| `intentos = 0`           |
| Índices (Listas/Texto) |   0    | Desplazamiento desde el primer elemento.         | `palabra[0]`             |

"""
"""
💻 El Patrón de Código (Plantilla Reutilizable) SOLO PARA ESTUDIO EN ALUMNO PRINCIPIANTE:

🧠 El Patrón Mental (Regla de los 3 Pasos)
Para recordar la lógica, solo necesitas memorizar estos 3 pasos en orden:
Neutralizar: Quita el signo negativo (conviértelo a positivo).
Excepción: Si el número es 0, ya sabemos que tiene 1 dígito.
Cortar y Contar: Mientras el número sea mayor a 0, córtale el último dígito (// 10) y suma 1 al contador.

💻 El Patrón de Código (Plantilla Reutilizable)
"""
n = -4567 # Prueba cambiando este valor a n = 0, n = 123
contador = 0

# 1. CASO ESPECIAL: El cero tiene exactamente 1 dígito
if n == 0:
    contador = 1

# 2. CASO NEGATIVO: Si es menor a 0, lo volvemos positivo
else:
    if n < 0:
        n = -n   # También se puede escribir como: n = abs(n)
    
    # 3. CASO GENERAL: Ahora sí aplicamos la fórmula de corte y conteo
    while n > 0:
        digito = n % 10      # (Opcional) Aquí "ves" o extraes el dígito
        contador += 1        # Sumamos 1 al contador
        n = n // 10          # "Cortamos" o eliminamos el último dígito

print("Cantidad de dígitos:", contador)
"""
________________________________________________________________________

⚡ El "Patrón Pythonico" (El atajo profesional)
Aunque el patrón matemático de arriba es fundamental para aprender lógica de programación, 
en el mundo real de Python, los programadores usan un atajo de 1 sola línea que hace exactamente 
lo mismo (Neutralizar + Contar).

Guárdalo como tu "Plan B":
"""
def contar_digitos_rapido(n):
    return len(str(abs(n)))

"""
¿Cómo funciona este atajo?
abs(n) lo vuelve positivo (ej: -85 → 85).
str(...) lo convierte en texto (ej: 85 → "85").
len(...) cuenta los caracteres de ese texto (ej: "85" tiene longitud 2).

"""
# 🧠 Regla de oro para tu cuaderno: Esto IMPLICA diferenciar contador de acumulador

# Si la variable siempre suma 1 → es CONTADOR (cuenta vueltas/cosas)

# Si la variable suma un valor variable → es ACUMULADOR (acumula totales)

"""
_________________________________________________________________________________________________

🔑concepto CLAVE si el usuario ingresa un numero float o no ingresa un numero entero ejemplo una palabra

while True:
    entrada = input("Ingrese un número entero: ")
    try:
        numero = int(entrada)
        break
    except ValueError:
        print("❌ Error: debe ingresar un número entero válido.")
"""