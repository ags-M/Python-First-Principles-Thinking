# ============================================================
# Ejercicio 24: Piedra, papel o tijera (simple)
# Categoría: 05_adivinanzas
# ============================================================
#
# ENUNCIADO:
# La computadora juega siempre 'piedra'. 
# El usuario elige entre 1=piedra, 2=papel, 3=tijera. 
# Decí si ganó, perdió o empató. Termina cuando escriba 'salir'.

cosa_C = piedra = 1
piedra = 1
papel = 2
tijera = 3
usuario = ""
#while usuario != salir
while not usuario == "salir":
    usuario = input("Elegí: 1(piedra), 2(papel), 3(tijera), o 'salir': ")
    if usuario == "1":           
        print("empató")
    elif usuario == "2":
        print("ganó")
    elif usuario == "3":
        print("perdió")
    elif usuario == "salir":
        break
    else:
        print("opción inválida")



