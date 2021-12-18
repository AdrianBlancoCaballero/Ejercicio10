# Ejercicio 10

lista = []

while True:
    numero = input("Introduzca un número: ")
    if numero == "fin":
        break

    numero = float(numero)

    datos = {}
    datos = numero
    lista.append(datos)

print("Lista de números introducidos: ")
for numero in lista:
    print("Número: ", numero)