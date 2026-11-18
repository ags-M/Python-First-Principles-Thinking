# LECCIÓN 5 - BUCLE WHILE | PRINCIPIANTE | Ejercicio Extra: Iconos y Unicode
# =========================================================
# CONSIGNA: Ejecutá este script para ver cómo Python maneja 
# emojis e iconos (caracteres Unicode) de forma nativa.
# Además, repasa el funcionamiento del bucle while.
# =========================================================

# 1. Imprimir iconos sueltos (son solo strings para Python)
print("🐍 ¡Hola, Python!")
print("💻 Programando en VS Code")
print("🚀 Despegue hacia el nivel experto")
print("✅ Ejercicio completado")
print("❌ Error (ejemplo de icono)")
print("💡 Idea o pista")
print("📁 Carpeta de ejercicios")
print("📦 Archivo .zip")

print("-" * 50)

# 2. Usar un bucle while con un icono (repaso de tu lección actual)
print("🔄 Contando con el bucle while:")
contador = 1

while contador <= 5:
    # La 'f' al inicio del string permite insertar variables con {}
    print(f"  Paso {contador}: 🐍")
    contador += 1

print("-" * 50)

# 3. Un pequeño arte con texto
print("🎉 ¡Fin del script!")
print("Python 3 usa UTF-8 por defecto, así que los emojis son")
print("tan válidos como cualquier otra letra (a, b, c, 1, 2, 3).")