# ============================================
# Lección 6 - Estructuras de control iterativo
# 2. Bucles while
# ============================================

# --- Bucle while básico ---
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# --- Validación de entrada con while ---
# Nota: en un programa real "entrada" vendría de input() en cada vuelta.
# Aquí ya la dejamos válida para poder ejecutar el script sin interacción.
entrada = "42"
while not entrada.isdigit():
    entrada = input("Introduce un número: ")
print(f"Has introducido el número: {entrada}")

# --- Bucle controlado por un evento (juego de adivinar un número) ---
# Nota: en un programa real "objetivo" vendría de random.randint(1, 10)
# y "numero" de int(input(...)). Aquí se simulan los intentos del usuario
# con una lista, para que el script sea reproducible.
objetivo = 7
intentos_simulados = [3, 7]
intentos = 0
adivinado = False

while not adivinado and intentos < 3:
    numero = intentos_simulados[intentos]
    intentos += 1
    print(f"Intento {intentos}/3: se prueba con {numero}")
    if numero == objetivo:
        print(f"¡Correcto! Has adivinado en {intentos} intentos.")
        adivinado = True
    else:
        pista = "mayor" if numero < objetivo else "menor"
        print(f"Incorrecto. El número es {pista} que {numero}.")

if not adivinado:
    print(f"Se acabaron los intentos. El número era {objetivo}.")

# --- Bucle con condición de salida variable (cajero) ---
# Nota: en un programa real "gasto" vendría de float(input(...)) en cada vuelta.
saldo = 1000
gastos_simulados = [200, 900, 0]  # el 0 simula que el usuario decide salir
indice = 0

while saldo > 0 and indice < len(gastos_simulados):
    print(f"Saldo actual: {saldo}€")
    gasto = gastos_simulados[indice]
    indice += 1

    if gasto == 0:
        break

    if gasto > saldo:
        print("No tienes suficiente saldo.")
        continue

    saldo -= gasto

print(f"Saldo final: {saldo}€")

# --- Bucle infinito controlado (while True + break) ---
# Nota: en un programa real "respuesta" vendría de input(...).lower()
respuestas_simuladas = ["x", "s", "n"]
indice = 0

while True:
    respuesta = respuestas_simuladas[indice].lower()
    indice += 1

    if respuesta == "n":
        print("Programa finalizado.")
        break

    if respuesta == "s":
        print("Continuando...")
    else:
        print("Respuesta no válida. Introduce 's' o 'n'.")

# --- Procesamiento de datos con while: factorial ---
def calcular_factorial(n):
    resultado = 1
    while n > 0:
        resultado *= n
        n -= 1
    return resultado

numero = 5
print(f"El factorial de {numero} es {calcular_factorial(numero)}")

# --- Simulaciones y aproximaciones: raíz cuadrada ---
def calcular_raiz_cuadrada(numero, precision=0.0001):
    aproximacion = numero / 2
    while abs(aproximacion**2 - numero) > precision:
        aproximacion = (aproximacion + numero / aproximacion) / 2
    return aproximacion

print(f"Raíz cuadrada de 25: {calcular_raiz_cuadrada(25):.6f}")
print(f"Raíz cuadrada de 7: {calcular_raiz_cuadrada(7):.6f}")

# --- Validación de entrada con while (rango de valores) ---
# Nota: en un programa real cada valor vendría de int(input(mensaje)).
def obtener_numero_en_rango_simulado(mensaje, minimo, maximo, entradas_simuladas):
    indice = 0
    while True:
        try:
            valor = int(entradas_simuladas[indice])
        except ValueError:
            print("Error: Debes introducir un número entero.")
            indice += 1
            continue
        indice += 1
        if minimo <= valor <= maximo:
            return valor
        print(f"Error: El número debe estar entre {minimo} y {maximo}.")

edad = obtener_numero_en_rango_simulado(
    "Introduce tu edad (0-120): ", 0, 120, ["abc", "200", "45"]
)
print(f"Edad registrada: {edad} años")

# --- Patrones con while: triángulo ---
def imprimir_triangulo(altura):
    fila = 1
    while fila <= altura:
        print("*" * fila)
        fila += 1

imprimir_triangulo(5)

# --- Consideraciones de rendimiento: ejemplo de bucle infinito (NO EJECUTAR) ---
# Este es un ejemplo de código ERRÓNEO que el material muestra como advertencia.
# Si se ejecutara tal cual, el programa se quedaría colgado para siempre,
# porque "contador" nunca se incrementa dentro del bucle.
#
# contador = 1
# while contador <= 5:
#     print(contador)
#     # Olvidamos incrementar contador -> bucle infinito

# --- Comparación for vs while (equivalentes) ---
suma = 0
i = 1
while i <= 10:
    suma += i
    i += 1
print(f"Suma (while): {suma}")

suma = 0
for i in range(1, 11):
    suma += i
print(f"Suma (for): {suma}")