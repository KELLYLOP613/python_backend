# ============================================
# Lección 6 - Estructuras de control iterativo
# 1. Bucles for y la función range()
# ============================================

# --- Bucle for básico ---
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# --- range(stop) ---
for i in range(5):
    print(i)

# --- range(start, stop) ---
for i in range(3, 8):
    print(i, end=" ")
print()

# --- range(start, stop, step) ---
for i in range(2, 11, 2):
    print(i, end=" ")
print()

# --- Cuenta regresiva con step negativo ---
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# --- Iterando sobre índices con range(len(...)) ---
nombres = ["Ana", "Carlos", "Elena"]
for i in range(len(nombres)):
    print(f"Posición {i}: {nombres[i]}")

# --- Forma más elegante: enumerate() ---
for indice, nombre in enumerate(nombres):
    print(f"Posición {indice}: {nombre}")

# --- Iterando sobre cadenas ---
mensaje = "Python"
for letra in mensaje:
    print(letra)

# --- Iterando sobre diccionarios ---
usuario = {"nombre": "Laura", "edad": 28, "ciudad": "Madrid"}

for clave in usuario:
    print(f"Clave: {clave}, Valor: {usuario[clave]}")

for clave, valor in usuario.items():
    print(f"{clave}: {valor}")

for valor in usuario.values():
    print(valor)

# --- Comprensiones de listas con for ---
cuadrados = [x**2 for x in range(1, 6)]
print(cuadrados)

pares = [x for x in range(10) if x % 2 == 0]
print(pares)

# --- Bucles for anidados: tabla de multiplicar ---
for i in range(1, 4):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}", end="\t")
    print()

# --- Caso práctico 1: suma de los primeros n números ---
n = 10
suma = 0
for i in range(1, n + 1):
    suma += i
print(f"La suma de los primeros {n} números es: {suma}")

# --- Caso práctico 2: números primos en un rango ---
def es_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

primos = []
for num in range(2, 20):
    if es_primo(num):
        primos.append(num)
print(f"Números primos entre 2 y 19: {primos}")

# --- Caso práctico 3: procesamiento de datos ---
temperaturas = [22, 19, 24, 25, 21, 23, 20]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

max_temp = max(temperaturas)
indice_max = temperaturas.index(max_temp)
print(f"El día más caluroso fue {dias[indice_max]} con {max_temp}°C")

promedio = sum(temperaturas) / len(temperaturas)
print(f"Temperatura promedio: {promedio:.1f}°C")

for i in range(len(dias)):
    if temperaturas[i] > promedio:
        print(f"{dias[i]}: {temperaturas[i]}°C (por encima del promedio)")