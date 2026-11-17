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
