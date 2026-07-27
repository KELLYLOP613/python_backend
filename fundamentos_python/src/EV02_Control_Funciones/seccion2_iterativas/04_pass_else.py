# ============================================
# Lección 6 - Estructuras de control iterativo
# 4. pass y else en bucles
# ============================================

# --- La sentencia pass ---
for numero in range(1, 10):
    if numero % 2 == 0:
        pass  # No hacemos nada con los números pares
    else:
        print(f"Procesando número impar: {numero}")

def procesar_datos():
    # Función aún no implementada
    pass

procesar_datos()  # No hace nada, pero no da error

modo_debug = False
for i in range(3):
    if not modo_debug:
        pass
    else:
        print(f"Procesando iteración {i}")

# --- La cláusula else en bucles for ---
# Caso 1: el bucle termina normalmente (sin break) -> se ejecuta el else
numeros = [4, 6, 8, 9, 10, 12]
for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")

# Caso 2: el bucle termina con break -> el else NO se ejecuta
numeros = [4, 6, 7, 8, 10]
for num in numeros:
    if num % 2 != 0 and num % 3 != 0:
        print(f"¡Encontrado un primo: {num}!")
        break
else:
    print("No se encontró ningún número primo en la lista")

# --- Validación con else ---
def validar_edades(lista_edades):
    for edad in lista_edades:
        if not isinstance(edad, int) or edad < 0:
            print(f"Edad inválida encontrada: {edad}")
            break
    else:
        print("Todas las edades son válidas")
        return True
    return False

validar_edades([25, 17, 30, 42])
validar_edades([25, -3, 30, 42])

# --- Búsqueda con else ---
def buscar_usuario(usuarios, nombre):
    for usuario in usuarios:
        if usuario["nombre"] == nombre:
            print(f"Usuario encontrado: {usuario}")
            return usuario
    else:
        print(f"Usuario '{nombre}' no encontrado, creando nuevo perfil...")
        nuevo_usuario = {"nombre": nombre, "nivel": 1}
        usuarios.append(nuevo_usuario)
        return nuevo_usuario

base_usuarios = [
    {"nombre": "Ana", "nivel": 5},
    {"nombre": "Carlos", "nivel": 3}
]
buscar_usuario(base_usuarios, "Ana")
buscar_usuario(base_usuarios, "Roberto")

# --- Combinando pass y else ---
def analizar_datos(valores, umbral):
    tiene_advertencias = False
    for valor in valores:
        if valor > umbral:
            tiene_advertencias = True
            print(f"Advertencia: valor {valor} excede el umbral {umbral}")
        else:
            pass  # Explícitamente no hacemos nada con valores normales
    else:
        if not tiene_advertencias:
            print("Análisis completo: todos los valores están dentro del rango normal")
            return "OK"
    return "ADVERTENCIA"

analizar_datos([10, 15, 20, 25], 30)
analizar_datos([10, 35, 20, 25], 30)

# --- else en bucles while ---
def encontrar_raiz(numero, max_iteraciones=10):
    aproximacion = numero / 2
    iteracion = 0
    while abs(aproximacion**2 - numero) > 0.001 and iteracion < max_iteraciones:
        aproximacion = (aproximacion + numero / aproximacion) / 2
        iteracion += 1
        print(f"Iteración {iteracion}: {aproximacion:.6f}")
    else:
        if iteracion < max_iteraciones:
            print(f"Convergencia alcanzada en {iteracion} iteraciones")
            return aproximacion
    print("No se alcanzó convergencia en el número máximo de iteraciones")
    return aproximacion

encontrar_raiz(25)
encontrar_raiz(612, 5)

# --- Ejemplo integrado: sistema de validación de formularios ---
def validar_formulario(datos):
    campos_requeridos = ["nombre", "email", "edad"]
    errores = []

    for campo in campos_requeridos:
        if campo not in datos:
            errores.append(f"Falta el campo requerido: {campo}")
            break
        elif not datos[campo]:
            errores.append(f"El campo {campo} no puede estar vacío")
            break
    else:
        if "@" not in datos["email"]:
            errores.append("Email inválido")
        try:
            edad = int(datos["edad"])
            if edad < 18 or edad > 120:
                errores.append("La edad debe estar entre 18 y 120")
        except ValueError:
            errores.append("La edad debe ser un número")

    if "telefono" in datos:
        if not datos["telefono"].isdigit():
            errores.append("El teléfono debe contener solo dígitos")
    else:
        pass  # Explícitamente indicamos que es opcional

    if errores:
        return {"valido": False, "errores": errores}
    else:
        return {"valido": True}

formulario1 = {
    "nombre": "Ana García",
    "email": "ana@ejemplo.com",
    "edad": "28"
}

formulario2 = {
    "nombre": "Carlos López",
    "email": "carlosejemplo.com",  # Falta @
    "edad": "17"  # Menor de edad
}

print(validar_formulario(formulario1))
print(validar_formulario(formulario2))