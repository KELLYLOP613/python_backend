# ============================================
# Lección 6 - Estructuras de control iterativo
# 3. break y continue
# ============================================

# --- La sentencia break ---
for numero in range(1, 11):
    if numero == 5:
        print("¡Encontrado el 5! Saliendo del bucle...")
        break
    print(f"Número actual: {numero}")
print("Bucle terminado")

# --- break: búsqueda eficiente ---
def buscar_elemento(lista, objetivo):
    for indice, elemento in enumerate(lista):
        if elemento == objetivo:
            return indice
    return -1

numeros = [4, 7, 2, 9, 1, 5]
posicion = buscar_elemento(numeros, 9)
print(f"El elemento se encuentra en la posición: {posicion}")

# --- break: validación de entrada con salida ---
# Nota: en un programa real "entrada" vendría de input(...) en cada vuelta.
entradas_simuladas = ["hola", "adios", "salir"]
indice = 0
while True:
    entrada = entradas_simuladas[indice]
    indice += 1
    if entrada.lower() == 'salir':
        print("Programa terminado.")
        break
    print(f"Has escrito: {entrada}")

# --- break: optimización de algoritmos ---
def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# --- La sentencia continue ---
for numero in range(1, 11):
    if numero % 2 == 0:
        continue
    print(f"Número impar: {numero}")

# --- continue: filtrado de datos ---
temperaturas = [22, -5, 28, 31, -15, 19, 26, -8]
print("Temperaturas positivas:")
for temp in temperaturas:
    if temp <= 0:
        continue
    print(f"{temp}°C")

# --- continue: manejo de casos especiales (evitar división por cero) ---
numeros = [1, 2, 0, 4, 0, 6, 7]
for num in numeros:
    if num == 0:
        print("Omitiendo división por cero")
        continue
    resultado = 10 / num
    print(f"10 / {num} = {resultado}")

# --- continue: validación de datos ---
datos = ["25", "error", "42", "texto", "17"]
suma = 0
for valor in datos:
    if not valor.isdigit():
        print(f"Valor no numérico ignorado: '{valor}'")
        continue
    suma += int(valor)
print(f"La suma de los valores válidos es: {suma}")

# --- Combinando break y continue ---
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
limite = 50
suma = 0
for num in numeros:
    if num % 3 == 0:
        print(f"Omitiendo {num} (múltiplo de 3)")
        continue
    suma += num
    print(f"Añadiendo {num}: suma = {suma}")
    if suma > limite:
        print(f"Límite de {limite} superado")
        break

# --- break/continue en bucles anidados ---
for i in range(1, 4):
    print(f"Grupo {i}:")
    for j in range(1, 6):
        if j == 3:
            print("  Saltando el elemento 3")
            continue  # Solo afecta al bucle interno
        print(f"  Elemento {j}")
    print("Fin del grupo\n")

# --- Salir de bucles anidados usando una bandera ---
encontrado = False
for i in range(5):
    for j in range(5):
        if i * j > 10:
            print(f"Valor encontrado: {i} * {j} = {i*j}")
            encontrado = True
            break  # Sale del bucle interno
    if encontrado:
        break  # Sale del bucle externo

# --- Ejemplo práctico avanzado: validación de contraseña ---
def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    tiene_mayuscula = False
    tiene_minuscula = False
    tiene_numero = False
    for caracter in contrasena:
        if caracter.isupper():
            tiene_mayuscula = True
            continue
        if caracter.islower():
            tiene_minuscula = True
            continue
        if caracter.isdigit():
            tiene_numero = True
    return tiene_mayuscula and tiene_minuscula and tiene_numero

contrasenas = ["abc123", "Password", "Password1", "pass123", "PASS123"]
for pwd in contrasenas:
    if validar_contrasena(pwd):
        print(f"'{pwd}' es válida")
    else:
        print(f"'{pwd}' NO es válida")

# --- Ejemplo práctico avanzado: procesamiento de transacciones ---
transacciones = [
    {"id": 1, "monto": 1200, "estado": "completada"},
    {"id": 2, "monto": -50, "estado": "error"},
    {"id": 3, "monto": 800, "estado": "pendiente"},
    {"id": 4, "monto": 1500, "estado": "completada"},
    {"id": 5, "monto": 0, "estado": "cancelada"}
]

total_procesado = 0
for t in transacciones:
    if t["estado"] != "completada":
        print(f"Transacción {t['id']}: {t['estado']} - ignorada")
        continue
    if t["monto"] <= 0:
        print(f"Transacción {t['id']}: monto inválido ({t['monto']})")
        continue
    total_procesado += t["monto"]
    print(f"Transacción {t['id']}: {t['monto']}€ procesada")

print(f"Total procesado: {total_procesado}€")