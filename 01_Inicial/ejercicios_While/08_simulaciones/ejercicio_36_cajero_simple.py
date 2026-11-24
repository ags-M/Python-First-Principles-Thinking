# ============================================================
# Ejercicio 36: Cajero simple
# Categoría: 08_simulaciones
# ============================================================
"""🎯 Objetivo: HACER UN CAJERO AUTOMATICO:

Construir un programa que simule un cajero automático donde el usuario 
puede retirar dinero repetidamente hasta que el saldo no alcance o decida salir. Usá while.

Consigna: arrancá con un saldo inicial. El usuario puede retirar plata o salir. 
El programa sigue dando vueltas hasta que el usuario elija salir o se quede sin saldo.
Si pide más de lo que tiene, se avisa y se vuelve al menú (no se rompe nada)
__________________________________________________________
| Pregunta           | Qué buscamos                       |
|--------------------|------------------------------------|
| ¿Qué se repite?    | El cuerpo del while                |
| ¿Cuándo sigue?     | La condición del while             |
| ¿Cuándo para?      | El break o condición que cambia    |
|____________________|____________________________________|

Consigna: Hacé un cajero automático que:

Empiece con un saldo de $1000.

En cada vuelta, muestre un menú con 4 opciones:

C — Consultar saldo
D — Depositar dinero (suma al saldo)
E — Extraer dinero (resta al saldo, pero no puede quedar negativo)
S — Salir (aqui esta el break)
El cajero sigue funcionando hasta que el usuario elija S.

┌─────────────────────────────────┐
│ 1. Muestra el menú              │
│ 2. Pregunta qué querés hacer    │
│ 3. Ejecuta lo que elegiste      │
│ 4. ¿Elegiste S?                 │
│    ├─ SÍ → se apaga 💤 break    │
│    └─ NO → vuelve al paso 1 🔁  │
└─────────────────────────────────┘ Eso es todo lo que hace el while. Se repite hasta que el usuario diga S


| Concepto clave              | Qué significa en el cajero                      |
|-----------------------------|-------------------------------------------------|
| Acción que se repite        | Mostrar menú → elegir opción → ejecutar         |
| Condición del while         | Mientras el usuario NO elija "S"  salir         |
| Validación antes de extraer | Si monto > saldo → mostrar mensaje Saldo es insuficiente y no restar

🎯 Objetivo del ejercicio:
Crear un cajero automático que:
Muestre un menú repetidamente.
Permita consultar saldo, depositar, retirar o salir.
Use un bucle while para mantener el menú activo hasta que el usuario elija "Salir".
"""
# ---- Ejercicio 36: Cajero simple ----
# Cajero Simple - Ejercicio 36
saldo = 1000
while True:
    
    print("__cajero automatico__")
    print("1.- consulta saldo")
    print("2.- deposita dinero")
    print("3.- retirar dinero")
    print("4.- salir")
    
    opcion = int(input("elije una opcion del 1 al 4: "))
    
    if opcion == 1:
        print("--"* 30)
        print(f"saldo actual: {saldo}")
        print("--"* 30)
    elif opcion == 2:
        deposito = int(input("ingresa la cantidad del deposito: "))
        saldo += deposito
        print("--"* 30)
        print(f"saldo actual: {saldo}")
        print("--"* 30)
    elif opcion == 3:
        retiro = int(input("ingresa el monto a retirar: "))
        if retiro <= saldo:
         saldo -= retiro
         print("--"* 30)
         print(f"retiro: {retiro}. saldo actual = {saldo}")
        else:
         print("--"* 30)
         print("saldo insuficiente")
        print("--"* 30)
    elif opcion == 4:
         print("--"* 30)
         print("gracias por usar el cajero")
         print("--"* 30)
         break # ACA SE CIERRA EL BUCLE
                        
    else:
        print("--"* 30)
        print("opcion invalida. Intenta de nuevo")
        print("--"* 30)