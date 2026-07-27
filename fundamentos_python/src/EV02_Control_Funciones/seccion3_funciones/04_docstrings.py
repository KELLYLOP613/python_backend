# ============================================
# Lección 7 - Funciones
# 4. Docstrings
# ============================================

def sumar(a, b):
    """Suma dos números y devuelve el resultado."""
    return a + b

print(sumar(3, 4))

# --- Estructura completa de un docstring ---
def calcular_promedio(numeros):
    """
    Calcula el promedio de una lista de números.

    Suma todos los números de la lista y divide el resultado
    entre la cantidad de elementos.

    Args:
        numeros: Una lista de valores numéricos

    Returns:
        El promedio como valor flotante

    Ejemplo:
        >>> calcular_promedio([1, 2, 3, 4])
        2.5
    """
    return sum(numeros) / len(numeros)

# --- Accediendo a los docstrings en tiempo de ejecución ---
print(calcular_promedio.__doc__)

# --- Estilo Google ---
def validar_email(email):
    """
    Verifica si una dirección de correo electrónico tiene formato válido.

    Args:
        email (str): La dirección de correo a validar

    Returns:
        bool: True si el formato es válido, False en caso contrario

    Raises:
        TypeError: Si email no es una cadena de texto
    """
    if not isinstance(email, str):
        raise TypeError("El email debe ser una cadena de texto")
    return "@" in email and "." in email.split("@")[-1]

print(validar_email("ana@ejemplo.com"))

# --- Estilo reStructuredText (reST) ---
def convertir_a_celsius(fahrenheit):
    """
    Convierte una temperatura de Fahrenheit a Celsius.

    :param fahrenheit: Temperatura en grados Fahrenheit
    :type fahrenheit: float
    :return: Temperatura en grados Celsius
    :rtype: float
    """
    return (fahrenheit - 32) * 5/9

print(convertir_a_celsius(98.6))

# --- Estilo NumPy/SciPy ---
def filtrar_pares(lista):
    """
    Filtra los números pares de una lista.

    Parameters
    ----------
    lista : list
        Lista de números enteros

    Returns
    -------
    list
        Nueva lista que contiene solo los números pares
    """
    return [num for num in lista if num % 2 == 0]

print(filtrar_pares([1, 2, 3, 4, 5, 6]))

# --- Docstring de una sola línea (funciones simples) ---
def es_mayor_de_edad(edad):
    """Determina si una persona es mayor de edad (18 años o más)."""
    return edad >= 18

print(es_mayor_de_edad(20))

# --- Documentando comportamientos especiales con ejemplos ---
def dividir_seguro(a, b):
    """
    Realiza una división segura entre dos números.

    Args:
        a: El numerador
        b: El denominador

    Returns:
        El resultado de la división a/b, o None si b es cero

    Ejemplo:
        >>> dividir_seguro(10, 2)
        5.0
        >>> dividir_seguro(10, 0)
    """
    if b == 0:
        return None
    return a / b

print(dividir_seguro(10, 2))
print(dividir_seguro(10, 0))

# --- Generador de contraseñas (ejemplo con módulos random/string) ---
def generar_contrasena(longitud=8):
    """
    Genera una contraseña aleatoria.

    Args:
        longitud: Número de caracteres de la contraseña (predeterminado: 8)

    Returns:
        Una cadena con la contraseña generada
    """
    import random
    import string
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

print(generar_contrasena())

# --- Buena práctica: usar verbos en presente ---
def validar_usuario(nombre):
    """Verifica si el nombre de usuario cumple con los requisitos."""
    return len(nombre) >= 3

print(validar_usuario("Ana"))

# --- Documentar tipos de datos ---
def contar_palabras(texto):
    """
    Cuenta el número de palabras en un texto.

    Args:
        texto (str): El texto a analizar

    Returns:
        int: El número de palabras encontradas
    """
    return len(texto.split())

print(contar_palabras("Python es un lenguaje versátil"))

# --- Incluir ejemplos prácticos ---
def formatear_nombre(nombre, apellido):
    """
    Formatea un nombre completo en formato "Apellido, Nombre".

    Args:
        nombre: Nombre de la persona
        apellido: Apellido de la persona

    Returns:
        Cadena formateada como "Apellido, Nombre"

    Ejemplo:
        >>> formatear_nombre("Juan", "Pérez")
        'Pérez, Juan'
    """
    return f"{apellido}, {nombre}"

print(formatear_nombre("Juan", "Pérez"))

# --- Documentar excepciones ---
def obtener_elemento(lista, indice):
    """
    Obtiene un elemento de una lista por su índice.

    Args:
        lista: La lista de elementos
        indice: Posición del elemento a obtener (comienza en 0)

    Returns:
        El elemento en la posición especificada

    Raises:
        IndexError: Si el índice está fuera del rango de la lista
    """
    return lista[indice]

print(obtener_elemento([10, 20, 30], 1))

# --- Ejemplo práctico completo: docstring con todas las buenas prácticas ---
def calcular_precio_final(precio_base, descuento=0, impuesto=0.21):
    """
    Calcula el precio final de un producto aplicando descuento e impuesto.

    NOTA: los ejemplos con >>> más abajo se verifican automáticamente con
    doctest al final de este archivo, y DOS de ellos fallarán por un motivo
    interesante: precisión de punto flotante (ver explicación en el chat).

    Args:
        precio_base (float): Precio original del producto
        descuento (float, opcional): Porcentaje de descuento (0-100). Predeterminado: 0
        impuesto (float, opcional): Tasa de impuesto (0-1). Predeterminado: 0.21

    Returns:
        float: Precio final después de aplicar descuento e impuesto

    Raises:
        ValueError: Si alguno de los parámetros tiene un valor negativo

    Ejemplos:
        >>> calcular_precio_final(100)
        121.0
        >>> calcular_precio_final(100, 10)
        108.9
        >>> calcular_precio_final(100, 10, 0.1)
        99.0
    """
    if precio_base < 0 or descuento < 0 or impuesto < 0:
        raise ValueError("Los valores no pueden ser negativos")

    precio_con_descuento = precio_base * (1 - descuento/100)
    precio_final = precio_con_descuento * (1 + impuesto)

    return precio_final

print(calcular_precio_final(100))
print(calcular_precio_final(100, 10))
print(calcular_precio_final(100, 10, 0.1))

# --- Ejecutar los ejemplos de los docstrings como pruebas automáticas ---
import doctest
resultados = doctest.testmod(verbose=False)
print(f"\nPruebas doctest: {resultados.attempted} ejecutadas, {resultados.failed} fallidas")