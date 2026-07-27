# ============================================
# Lección 7 - Funciones
# 3. Return
# ============================================

def calcular_cuadrado(numero):
    resultado = numero * numero
    return resultado

area = calcular_cuadrado(4)
print(area)

# --- Funciones sin return devuelven None ---
def saludar(nombre):
    print(f"Hola, {nombre}")

resultado = saludar("Laura")
print(f"La función devolvió: {resultado}")

# --- Retornando múltiples valores (empaquetados en una tupla) ---
def estadisticas(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    minimo = min(numeros)
    maximo = max(numeros)
    return total, promedio, minimo, maximo

datos = [4, 8, 15, 16, 23, 42]
suma, media, menor, mayor = estadisticas(datos)

print(f"Suma: {suma}")
print(f"Promedio: {media}")
print(f"Mínimo: {menor}")
print(f"Máximo: {mayor}")

resultado_tupla = estadisticas(datos)
print(type(resultado_tupla))
print(resultado_tupla)
print(resultado_tupla[1])

# --- Return anticipado (early return) ---
def dividir_seguro(a, b):
    if b == 0:
        print("Error: División por cero")
        return None
    resultado = a / b
    return resultado

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))

# --- Función booleana (predicado) ---
def es_mayor_de_edad(edad):
    return edad >= 18

def es_correo_valido(email):
    return "@" in email and "." in email

usuario_edad = 16
if es_mayor_de_edad(usuario_edad):
    print("Acceso permitido")
else:
    print("Acceso denegado")

# --- Transformación de datos ---
def formato_nombre(nombre, apellido):
    return f"{apellido.upper()}, {nombre.capitalize()}"

print(formato_nombre("ana", "garcía"))

# --- Cálculos y procesamiento ---
def calcular_precio_con_iva(precio_base, tasa_iva=0.21):
    return precio_base * (1 + tasa_iva)

precio_final = calcular_precio_con_iva(100)
print(f"Precio con IVA: {precio_final} €")

# --- Return con estructuras de datos ---
def crear_lista_pares(maximo):
    return [num for num in range(2, maximo + 1, 2)]

def crear_diccionario_cuadrados(numeros):
    return {num: num ** 2 for num in numeros}

pares = crear_lista_pares(10)
print(pares)

cuadrados = crear_diccionario_cuadrados([1, 2, 3, 4])
print(cuadrados)

# --- Buena práctica: coherencia en el tipo de retorno ---
def filtrar_positivos(numeros):
    if not isinstance(numeros, list):
        return []
    return [num for num in numeros if num > 0]

print(filtrar_positivos([-3, 5, -1, 8, 2]))
print(filtrar_positivos("no es una lista"))

# --- Buena práctica: documentar el valor de retorno ---
def calcular_descuento(precio, porcentaje):
    """
    Calcula el precio con descuento.

    Args:
        precio: El precio original
        porcentaje: El porcentaje de descuento (0-100)

    Returns:
        float: El precio después de aplicar el descuento
    """
    return precio - (precio * porcentaje / 100)

print(calcular_descuento(200, 25))

# --- Buena práctica: evitar efectos secundarios (separar cálculo de impresión) ---
def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

notas = [7, 8, 6, 9]
promedio = calcular_promedio(notas)
print(f"El promedio es: {promedio}")

# --- Buena práctica: return temprano para casos especiales ---
def obtener_calificacion(puntuacion):
    if puntuacion < 0 or puntuacion > 100:
        return "Puntuación inválida"
    if puntuacion >= 90:
        return "Sobresaliente"
    if puntuacion >= 70:
        return "Notable"
    if puntuacion >= 60:
        return "Bien"
    if puntuacion >= 50:
        return "Suficiente"
    return "Insuficiente"

for p in [95, 75, 65, 55, 30, 150]:
    print(f"{p} -> {obtener_calificacion(p)}")

# --- Ejemplo práctico completo: conversión de temperatura ---
def convertir_temperatura(valor, origen, destino):
    """
    Convierte una temperatura entre diferentes unidades.

    Args:
        valor: El valor de la temperatura a convertir
        origen: Unidad de origen ('C', 'F' o 'K')
        destino: Unidad de destino ('C', 'F' o 'K')

    Returns:
        float: La temperatura convertida, o None si los parámetros son inválidos
    """
    unidades_validas = {'C', 'F', 'K'}
    if origen not in unidades_validas or destino not in unidades_validas:
        return None

    if origen == destino:
        return valor

    if origen == 'F':
        celsius = (valor - 32) * 5/9
    elif origen == 'K':
        celsius = valor - 273.15
    else:
        celsius = valor

    if destino == 'F':
        return celsius * 9/5 + 32
    elif destino == 'K':
        return celsius + 273.15
    else:
        return celsius

print(convertir_temperatura(25, 'C', 'F'))
print(convertir_temperatura(98.6, 'F', 'C'))
print(convertir_temperatura(0, 'C', 'K'))
print(convertir_temperatura(20, 'X', 'Y'))