#consigna contar cuantas consonante tiene una palabra y guardar las consonantes a medida que las encontrás

palabra = input("Ingresá una palabra: ").lower()
vocales = "aeiou"
contador_consonantes = 0
consonantes_encontradas = "" # ✅ Nueva variable para guardar las consonantes. 
#La forma más simple es usar una cadena vacía e ir concatenándole cada consonante. se usa " " por que son string o cadena
indice = 0

while indice < len(palabra):
    caracter = palabra[indice]
    if caracter.isalpha() and caracter not in vocales: #El método .isalpha() verifica: 
                                                       # si el carácter es una letra del alfabeto
        contador_consonantes += 1
        consonantes_encontradas += caracter  # ✅ Se agrega la consonante a la cadena
    indice += 1

print(f"La palabra tiene {contador_consonantes} consonantes.")
print(f"Las consonantes son: {consonantes_encontradas}")

