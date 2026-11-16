# ============================================================
# Ejercicio 14: Contraseña
# Categoría: 03_validacion
# ============================================================
#
# ENUNCIADO:
# Pedile al usuario una contraseña hasta que escriba exactamente 'python123'. Mostrá 'Acceso concedido'.
#
contraseña_secreta= "python123"
contraseña = input("ingresa una contraseña valida: ")
while contraseña != contraseña_secreta:
    print("contraseña no valida")
    contraseña = input("ingresa una contraseña valida: ")
print(f"ingresaste la contraseña valida")

#📊 Traceo manual
# ______________________________________________________________________________________________

# iteracion        valor de la contraseña        se cumple el valor            que imprime
                                               #contraseña != python123
#_______________________________________________________________________________________________
#
#     1                alfa02344                        TRUE                contraseña no valida
# 
# 
#                     
#     2                python123                        FALES                  sale del bucle        
# ______________________________________________________________________________________________
# 
#                                                                         imprime contraseña valida
#_______________________________________________________________________________________________