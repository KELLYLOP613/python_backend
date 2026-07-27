# ============================================
# Lección 7 - Funciones
# 2. Parámetros y argumentos
# ============================================

# --- Parámetro vs argumento ---
def saludar_persona(nombre):  # 'nombre' es un parámetro
    print(f"Hola, {nombre}!")

saludar_persona("Ana")  # "Ana" es un argumento

# --- Parámetros posicionales ---
def calcular_precio_final(precio_base, impuesto):
    return precio_base + (precio_base * impuesto)

total = calcular_precio_final(100, 0.21)
print(f"Precio final: {total}")

# --- Parámetros con valores predeterminados ---
def saludar(nombre, mensaje="¡Bienvenido!"):
    print(f"Hola {nombre}. {mensaje}")

saludar("Carlos")
saludar("María", "¿Cómo estás hoy?")

# Los parámetros con valor predeterminado deben ir después de los obligatorios
def crear_perfil(nombre, edad, ciudad="Madrid"):
    return f"Perfil: {nombre}, {edad} años, {ciudad}"

print(crear_perfil("Sofía", 22))

# Incorrecto (causaría SyntaxError): un parámetro sin valor por defecto
# no puede ir después de uno que sí lo tiene.
# def crear_perfil(nombre, ciudad="Madrid", edad):
#     return f"Perfil: {nombre}, {edad} años, {ciudad}"

# --- Parámetros por nombre (keyword arguments) ---
def dividir(dividendo, divisor):
    return dividendo / divisor

resultado1 = dividir(10, 2)
resultado2 = dividir(divisor=2, dividendo=10)
print(resultado1, resultado2)

def crear_usuario(nombre, apellido, edad, email, activo=True):
    return {
        "nombre_completo": f"{nombre} {apellido}",
        "edad": edad,
        "email": email,
        "activo": activo
    }

usuario = crear_usuario(
    nombre="Juan",
    apellido="Pérez",
    edad=28,
    email="juan@ejemplo.com",
    activo=False
)
print(usuario)

# --- Combinando tipos de parámetros ---
def calcular_pago(horas, tarifa=15, moneda="EUR"):
    total = horas * tarifa
    return f"{total} {moneda}"

pago1 = calcular_pago(40)
pago2 = calcular_pago(35, 20)
pago3 = calcular_pago(30, moneda="USD")
pago4 = calcular_pago(horas=25, tarifa=18, moneda="GBP")

print(pago1)
print(pago2)
print(pago3)
print(pago4)

# --- Validación de argumentos ---
def calcular_descuento(precio, porcentaje):
    if not isinstance(precio, (int, float)) or precio < 0:
        raise ValueError("El precio debe ser un número positivo")
    if not isinstance(porcentaje, (int, float)) or not (0 <= porcentaje <= 100):
        raise ValueError("El porcentaje debe ser un número entre 0 y 100")
    descuento = precio * (porcentaje / 100)
    return precio - descuento

try:
    precio_final = calcular_descuento(100, 15)
    print(f"Precio con descuento: {precio_final}")

    precio_erroneo = calcular_descuento(-50, 10)  # Esto lanzará un error
except ValueError as e:
    print(f"Error: {e}")

# --- Número variable de argumentos posicionales (*args) ---
def sumar(*numeros):
    total = 0
    for numero in numeros:
        total += numero
    return total

print(sumar(1, 2))
print(sumar(1, 2, 3, 4, 5))
print(sumar())

# --- Número variable de argumentos por nombre (**kwargs) ---
def mostrar_informacion(**datos):
    for clave, valor in datos.items():
        print(f"{clave}: {valor}")

mostrar_informacion(nombre="Python", creador="Guido van Rossum", anio=1991)

# --- Ejemplo práctico: función flexible para formatear texto ---
def formatear_texto(texto, mayusculas=False, prefijo="", sufijo="", separador=" "):
    if mayusculas:
        texto = texto.upper()

    palabras = texto.split()
    palabras_formateadas = [f"{prefijo}{palabra}{sufijo}" for palabra in palabras]
    resultado = separador.join(palabras_formateadas)

    return resultado

texto_original = "python es un lenguaje versátil"

print(formatear_texto(texto_original))
print(formatear_texto(texto_original, mayusculas=True))
print(formatear_texto(texto_original, prefijo="«", sufijo="»"))
print(formatear_texto(texto_original, separador="-"))
print(formatear_texto(
    texto_original,
    mayusculas=True,
    prefijo="#",
    sufijo="!",
    separador="..."
))