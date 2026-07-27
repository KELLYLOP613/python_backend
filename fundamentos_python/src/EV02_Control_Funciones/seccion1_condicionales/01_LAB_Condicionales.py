# ============================================
# Lección 5 - Estructuras de control condicional
# ============================================

# --------------------------------------------
# 1. La declaración if
# --------------------------------------------
edad = 20
if edad >= 18:
    print("Eres mayor de edad.")

temperatura = 30
if temperatura > 25:
    print("Hace calor hoy.")

hora = 10
if hora >= 6 and hora < 12:
    print("Buenos días.")

# --------------------------------------------
# 2. La declaración if-else
# --------------------------------------------
edad = 17
if edad >= 18:
    print("Puedes votar en las elecciones.")
else:
    print("Aún no tienes edad para votar.")

# Nota: en un programa real, "contrasena" vendría de input()
contrasena = "secreta123"
if contrasena == "secreta123":
    print("Acceso concedido.")
else:
    print("Contraseña incorrecta. Acceso denegado.")

numero = 15
if numero % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")

saldo = 300
retiro = 500
if saldo >= retiro:
    saldo -= retiro
    print("Retiro exitoso.")
    print(f"Nuevo saldo: {saldo}")
else:
    print("Fondos insuficientes.")
    print(f"Saldo actual: {saldo}")

# --------------------------------------------
# 3. La declaración if-elif-else
# --------------------------------------------
numero = 0
if numero > 0:
    print("El número es positivo.")
elif numero < 0:
    print("El número es negativo.")
else:
    print("El número es cero.")

nota = 87
if nota >= 90:
    print("Calificación: Sobresaliente")
elif nota >= 80:
    print("Calificación: Notable")
elif nota >= 70:
    print("Calificación: Aprobado")
else:
    print("Calificación: Suspenso")

edad = 45
if edad < 18:
    print("Eres menor de edad.")
elif 18 <= edad < 65:
    print("Eres adulto.")
else:
    print("Eres mayor de 65 años.")

color = "azul"
if color == "rojo":
    print("El color es rojo.")
elif color == "verde":
    print("El color es verde.")
elif color == "azul":
    print("El color es azul.")

# --------------------------------------------
# 4. La declaración match-case
# --------------------------------------------
# Nota: en un programa real, "fruta" vendría de input()
fruta = "manzana"
match fruta:
    case "manzana":
        print("La fruta es una manzana.")
    case "naranja":
        print("La fruta es una naranja.")
    case "plátano":
        print("La fruta es un plátano.")
    case _:
        print("Fruta desconocida.")

punto = (0, 5)
match punto:
    case (0, 0):
        print("El punto está en el origen.")
    case (0, y):
        print(f"El punto está en el eje Y en y={y}.")
    case (x, 0):
        print(f"El punto está en el eje X en x={x}.")
    case (x, y):
        print(f"El punto está en coordenadas x={x}, y={y}.")

edad = 20
match edad:
    case edad if edad < 18:
        print("Eres menor de edad.")
    case edad if edad >= 18 and edad < 65:
        print("Eres adulto.")
    case edad if edad >= 65:
        print("Eres adulto mayor.")

usuarios = [
    {"nombre": "Ana", "rol": "admin"},
    {"nombre": "Luis", "rol": "usuario"},
    {"nombre": "Marta", "rol": "moderador"}
]
for usuario in usuarios:
    match usuario:
        case {"rol": "admin"}:
            print(f"{usuario['nombre']} tiene permisos de administrador.")
        case {"rol": "moderador"}:
            print(f"{usuario['nombre']} puede moderar contenidos.")
        case {"rol": "usuario"}:
            print(f"{usuario['nombre']} es un usuario regular.")
        case _:
            print(f"Rol de {usuario['nombre']} desconocido.")

numeros = [1, 2, 3, 4]
match numeros:
    case []:
        print("La lista está vacía.")
    case [uno]:
        print(f"Un solo elemento: {uno}.")
    case [uno, dos]:
        print(f"Dos elementos: {uno} y {dos}.")
    case [uno, *resto]:
        print(f"Primer elemento: {uno}, resto de la lista: {resto}.")

# --------------------------------------------
# 5. Operadores lógicos en condicionales
# --------------------------------------------
edad = 25
ingresos = 30000
if edad >= 18 and ingresos >= 20000:
    print("Eres elegible para el crédito.")

dia = "sábado"
if dia == "sábado" or dia == "domingo":
    print("Es fin de semana.")

llueve = False
if not llueve:
    print("Podemos salir al parque.")

edad = 17
permiso_parental = True
if (edad >= 18) or (edad >= 16 and permiso_parental):
    print("Puedes obtener la licencia de conducir.")
else:
    print("No cumples los requisitos para la licencia.")

# Precedencia de operadores lógicos: not > and > or
a = True
b = False
c = not b
resultado = a or b and c
print(resultado)  # se evalúa como: a or (b and c)

resultado = (a or b) and c
print(resultado)

usuario = "admin"
contrasena = "1234"
if usuario == "admin" and contrasena == "1234":
    print("Acceso concedido.")

# --------------------------------------------
# 6. Condicionales anidados
# --------------------------------------------
edad = 30
estado_civil = 'soltero'
if edad >= 18:
    if estado_civil == 'casado':
        print('Eres un adulto casado.')
    else:
        print('Eres un adulto soltero.')
else:
    print('Eres menor de edad.')

edad = 16
permiso_padres = True
if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
else:
    if edad >= 16:
        if permiso_padres:
            print('Puedes obtener la licencia con permiso de tus padres.')
        else:
            print('Necesitas el permiso de tus padres para obtener la licencia.')
    else:
        print('Eres demasiado joven para conducir.')

# Misma lógica anterior, reescrita con elif para mayor claridad
edad = 16
permiso_padres = True
if edad >= 18:
    print('Puedes obtener la licencia de conducir.')
elif edad >= 16 and permiso_padres:
    print('Puedes obtener la licencia con permiso de tus padres.')
elif edad >= 16 and not permiso_padres:
    print('Necesitas el permiso de tus padres para obtener la licencia.')
else:
    print('Eres demasiado joven para conducir.')

usuario = 'admin'
contrasena = '1234'
if usuario == 'admin':
    if contrasena == '1234':
        print('Acceso concedido.')
    else:
        print('Contraseña incorrecta.')
else:
    print('Usuario no reconocido.')

a = 5
b = 10
c = 15
if a > b:
    if a > c:
        print('a es el mayor.')
    else:
        if c > b:
            print('c es el mayor.')
        else:
            print('b es el mayor.')
else:
    if b > c:
        print('b es el mayor.')
    else:
        print('c es el mayor.')

# Alternativa más simple y legible, sin anidar tanto
mayor = a
if b > mayor:
    mayor = b
if c > mayor:
    mayor = c
print(f'El número mayor es {mayor}.')

# --------------------------------------------
# 7. Expresiones condicionales (condicional ternario)
# --------------------------------------------
edad = 17
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)

a = 1
b = 2
print("El máximo es:", a if a > b else b)

edad = 20
categoria = "Menor" if edad < 18 else ("Joven Adulto" if edad < 30 else "Adulto")
print(categoria)

numeros = [1, 2, 3, 4, 5]
paridad = ["par" if n % 2 == 0 else "impar" for n in numeros]
print(paridad)

dividendo = 10
divisor = 0
resultado = dividendo / divisor if divisor != 0 else "División por cero no permitida"
print(resultado)

# --------------------------------------------
# 8. Evaluación de cortocircuito y optimización
# --------------------------------------------
lista = []
if lista and lista[0] == 'Python':
    print("El primer elemento es 'Python'.")
else:
    print("La lista está vacía o el primer elemento no es 'Python'.")

dividendo = 10
divisor = 0
if divisor != 0 and dividendo / divisor > 1:
    print("El resultado de la división es mayor que 1.")
else:
    print("No es posible dividir entre cero.")

acceso_permitido = False
acceso_registrado = True

# NOTA: el material original traía un paréntesis sin cerrar en este bloque
# (print("Acceso concedido." sin el ")" final), lo cual causaba
# SyntaxError: '(' was never closed. Se corrigió aquí.
if acceso_permitido:
    print("Acceso concedido.")
else:
    if acceso_registrado:
        print("Acceso concedido.")

numeros = [0, 0, 1, 0]
if any(numeros):
    print("Al menos un número es no cero.")

condiciones = [True, True, False, True]
if all(condiciones):
    print("Todas las condiciones son verdaderas.")
else:
    print("Al menos una condición es falsa.")