
#Realiza una ficha de un cliente
nombre = input("Nombre: ")
email = input("Email: ")
telefono = input("Teléfono: ")
edad = int(input("Edad: "))

print("----------------------------------")
print(f"Nombre:   {nombre}   (tipo: {type(nombre).__name__})")
print(f"Email:    {email}    (tipo: {type(email).__name__})")
print(f"Teléfono: {telefono} (tipo: {type(telefono).__name__})")
print(f"Edad:     {edad}     (tipo: {type(edad).__name__})")
print("----------------------------------")

"""
.__name__ es un atributo especial (dunder method) de los objetos en Python. 
Objeto = cualquier "cosa" que existe en memoria en Python y tiene datos + comportamiento.
Atributo = un dato o valor que pertenece a un objeto. Es como una "característica" o "propiedad" del objeto.
Definición breve
Un objeto es una instancia concreta de un tipo/clase. Todo en Python es un objeto: 
números, textos, listas, funciones, etc.

¿Cómo se llama?
Se llama "dunder name" (double underscore name) o atributo especial __name__.

¿Para qué sirve?
Devuelve el nombre del tipo/clase como un string.

"""