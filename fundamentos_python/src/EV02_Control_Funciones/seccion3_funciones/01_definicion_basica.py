# ============================================
# Lección 7 - Funciones
# 1. Definición básica
# ============================================

def saludar():
    print("¡Hola, mundo!")

saludar()

# --- Función con parámetros y return ---
def calcular_area_rectangulo(base, altura):
    area = base * altura
    return area

resultado = calcular_area_rectangulo(5, 3)
print(f"El área del rectángulo es: {resultado}")

# --- Funciones simples, cada una con una única tarea ---
def es_par(numero):
    return numero % 2 == 0

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

print(es_par(4))
print(celsius_a_fahrenheit(25))

# --- Las funciones son "ciudadanos de primera clase" ---
convertir = celsius_a_fahrenheit
temperatura_f = convertir(25)
print(f"25°C equivalen a {temperatura_f}°F")

# --- Ámbito (scope): las variables internas no existen fuera de la función ---
def calcular_descuento(precio, porcentaje=10):
    descuento = precio * (porcentaje / 100)
    precio_final = precio - descuento
    return precio_final

precio_con_descuento = calcular_descuento(100)
print(f"Precio con descuento: {precio_con_descuento}")
# print(descuento)  # Esto daría NameError: 'descuento' no existe fuera de la función