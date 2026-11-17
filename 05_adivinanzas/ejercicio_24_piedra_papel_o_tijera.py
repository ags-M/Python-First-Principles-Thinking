# ============================================================
# Ejercicio 24: Piedra, papel o tijera (simple)
# Categoría: 05_adivinanzas
# ============================================================
#
# ENUNCIADO:
# La computadora juega siempre 'piedra'. 
# El usuario elige entre 1=piedra, 2=papel, 3=tijera. 
# Decí si ganó, perdió o empató. Termina cuando escriba 'salir'.

cosa_C = "piedra"
piedra = "piedra"
papel = "papel"
tijera = "tijera"
usuario = ""
#while usuario != salir
while not usuario == "salir":
    usuario = input("Elegí: piedra, papel, tijera, o escribir salir: ")
    if usuario == piedra:
       print("el usuario empató")
    elif usuario == papel:
        print("el usuario gano")
    elif usuario == tijera:
        print("el usuario perdio")
    elif usuario == "salir":
        break
    else:
        print("opcion invalida")



