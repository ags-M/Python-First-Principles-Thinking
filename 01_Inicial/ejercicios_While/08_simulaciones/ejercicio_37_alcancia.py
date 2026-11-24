# ============================================================
# Ejercicio 37: Alcancía
# Categoría: 08_simulaciones
# ============================================================
#
# ENUNCIADO:
# Meta: 500 pesos. El usuario ingresa montos hasta alcanzar o superar la meta. Mostrá cuántos aportes hizo.

"""
# 🎯 TRAZADO MANUAL :

1.- VOLUNTAD DEL USUARIO DE AHORRAR EN UNA ALCANCIA. PEDIR QUE INGRESE EL MONTO DE AHORRO ej 500 META
2.- Inicializar total = 0
3.- while < meta: utilizamos < por que es estricto cuando llega el valor a 500 no permite mas depositos
  pedir depositar dinero en ahorro
  validar el deposito que sea mayor de 0
  ver total += deposito ¿cumple la meta?
  mostrar en cada iteracion cuanto lleva depositado y cuanto le falta para alcanzar la meta
4.-fuera del While: Alcanzaste la meta !!! 🚀

"""
meta = int(input("Cuando dinero quiere ahorrar $: "))
total_ahorro = 0
deposito = 0
contador_depositos = 1
while total_ahorro < meta:
      deposito = int(input("ingresa dinero a tu alcancia $: "))
      print("---" * 30)
      if deposito <= 0:
        print("ingresa un valor de deposito válido")
        continue
      total_ahorro += deposito
      
      if total_ahorro < meta:
        print(f"saldo actual = $ {total_ahorro}, te faltan para alcanzar la meta $: {meta - total_ahorro}")
        print("---" * 30)
      else:
        total_ahorro != meta
        print(f"la meta de ahorro era de $: {meta}, el saldo actual es $: {total_ahorro} ")
        print("---" * 30)
        print(f"contador de depositos: {contador_depositos}")
      contador_depositos += 1
print("alcanzaste la meta!!")
  
          