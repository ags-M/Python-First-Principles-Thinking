# ============================================================
#  RESUMEN: ¿CUÁNDO USAR CADA PLANTILLA DE FOR? | NOVA 🤖
#  Curso Python - Módulo 1 - Lección 5
# ============================================================
# Esta tabla es tu CONSULTA RÁPIDA.
# Cada vez que tengas un ejercicio de for, preguntate:
# "¿qué tipo de problema es?" y elegí la plantilla correspondiente.
# ============================================================

"""
╔══════════════════════════════════════════════════════════════════════════════╗
║  PLANTILLA  │  ESTRUCTURA            │  CUÁNDO USARLA                 │  EJEMPLO TÍPICO              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  #1 Simple  │  for i in range(...)   │  Repetir N veces, contar,      │  Tabla de multiplicar,       ║
║             │                        │  acumular                      │  factorial, suma 1 al 100    ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  #2 Anidado │  for dentro de for     │  Patrones 2D, grillas,         │  Triángulos, rombo,          ║
║             │                        │  tablas completas              │  tablas del 1 al 5           ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  #3 Condición│ for + if/else          │  Filtrar, clasificar,          │  FizzBuzz, pares/impares,    ║
║             │                        │  reemplazar                    │  positivos/negativos         ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  #4 Colección│ for x in lista         │  Recorrer listas, strings,     │  Promedio, buscar mayor,     ║
║             │                        │  tuplas                        │  mostrar frutas              ║
╠══════════════════════════════════════════════════════════════════════════════╣
║  #5 Break/  │  for + break o         │  Controlar el flujo,           │  Buscar elemento,            ║
║  Continue   │  continue              │  salir antes, saltar           │  contraseñas, cajero         ║
╚══════════════════════════════════════════════════════════════════════════════╝
"""

# ============================================================
#  REGLAS DE ORO (acordate siempre)
# ============================================================
# 1. Una plantilla NUNCA se ejecuta tal cual. Siempre hay que completarla.
# 2. Los comentarios (# hacer algo) NO son código. Reemplazalos por código real.
# 3. Si tenés un bucle anidado:
#      - el EXTERNO controla las FILAS
#      - el INTERNO controla las COLUMNAS
# 4. range(inicio, fin+1, paso) → el "fin" NO se incluye.
# 5. break = SALIR del bucle. continue = SALTAR a la siguiente iteración.
# ============================================================

# ============================================================
#  FLUJO DE DECISIÓN RÁPIDO
# ============================================================
# ¿Tenés que repetir N veces algo simple?
#   → Plantilla #1
#
# ¿Tenés que dibujar algo en 2D (filas × columnas)?
#   → Plantilla #2
#
# ¿Tenés que filtrar o clasificar elementos?
#   → Plantilla #3
#
# ¿Tenés una lista/string/tupla que recorrer?
#   → Plantilla #4
#
# ¿Tenés que salir antes de tiempo o saltar iteraciones?
#   → Plantilla #5
# ============================================================

# 📋 RESUMEN: ¿CUÁNDO USAR CADA PLANTILLA DE FOR?

# > Curso Python - Módulo 1 - Lección 5 | NOVA 🤖

## 🎯 Tabla de plantillas

| Plantilla        | Estructura            | Cuándo usarla                          | Ejemplo típico                    
|------------------|-----------------------|----------------------------------------|---------------------------------------
| #1 Simple**    | `for i in range(...)` | Repetir N veces, contar, acumular      | Tabla de multiplicar, factorial    
| #2 Anidado**   | `for` dentro de `for` | Patrones 2D, grillas, tablas completas | Triángulos, rombo, tablas 1 al 5 
| #3 Condición** | `for` + `if/else`     | Filtrar, clasificar, reemplazar        | FizzBuzz, pares/impares 
| #4 Colección** | `for x in lista`      | Recorrer listas, strings, tuplas       | Promedio, buscar mayor, mostrar frutas 
| #5 Break       |for`+`break`o`continue`| Controlar el flujo, salir antes, saltar| Buscar, contraseñas, cajero |
#   /Continue**  

"""
## 🏆 Reglas de oro

1. Una plantilla **NUNCA** se ejecuta tal cual. Siempre hay que completarla.
2. Los comentarios (`# hacer algo`) **NO** son código. Reemplazalos por código real.
3. En bucles anidados:
   - el **EXTERNO** controla las FILAS
   - el **INTERNO** controla las COLUMNAS
4. `range(inicio, fin+1, paso)` → el "fin" **NO** se incluye.
5. `break` = SALIR del bucle. `continue` = SALTAR a la siguiente iteración.

"""

## 🧭 Flujo de decisión rápido
