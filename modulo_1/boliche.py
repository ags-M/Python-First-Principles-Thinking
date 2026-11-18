"""
Ejercicio: ¿Podés entrar al boliche?
Tenés que hacer un programa que pregunte 3 cosas y al final diga si la persona puede entrar al boliche o no.

1. **Edad:** tiene que ser **mayor o igual a 18**.
2. **Está en la lista de invitados:** si responde `"s"`, sí está. Si responde `"n"`, no está.
3. **Paga la entrada:** si responde `"s"`, sí paga. Si responde `"n"`, no paga.

### Regla final para entrar

Puede entrar si:
- Tiene 18 o más **Y**
- (Está en la lista de invitados **O** paga la entrada)

O sea, si es mayor de edad y, además, o está en la lista o paga la entrada.

## Lo que tenés que programar

1. Pedir la edad (como número entero).
2. Preguntar si está en la lista de invitados → guardarlo en una variable `esta_en_lista`, 
**usando la estructura con `== "s"`** que venimos hablando.
3. Preguntar si paga la entrada → guardarlo en una variable `paga_entrada`, también con `== "s"`.
4. Calcular `edad_ok` (si tiene 18 o más).
5. Calcular `puede_entrar` usando `edad_ok and (esta_en_lista or paga_entrada)`.
6. Imprimir el resultado con un `f-string`:
print(f"¿Podés entrar?: {puede_entrar}")
"""
edad= int(input("ingresa tu edad: "))
edad_ok = edad >= 18
lista_invitados = input("estas en la lista de invitados (s/n): ").lower() == "s"
paga_entrada = input("paga entrada (s/n): ").lower() =="s"
puede_entrar = edad_ok and (lista_invitados or paga_entrada)
print(f"¿podes entrar?: {puede_entrar}")

