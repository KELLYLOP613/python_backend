# EV01 – Fundamentos de Python

Esta evidencia corresponde a la actividad **GA1-220501093-04-AA1-EV01 – Fundamentos de Python: variables, operadores y manipulación de cadenas**, desarrollada como parte del curso **Python Avanzado** del programa **Tecnólogo en Análisis y Desarrollo de Software (ADSO)** del **SENA**.

## Objetivo

Aplicar los conceptos fundamentales del lenguaje Python mediante el desarrollo de ejercicios prácticos relacionados con:

- Función `print()`
- Literales
- Operadores
- Variables
- Expresiones
- Resolución de algoritmos básicos

---

# Estructura

```text
EV01_Fundamentos/
│
├── README.md
│
├── seccion1_hola_mundo/
│   ├── 01_LAB_Funcion_Print.py
│   ├── 02_LAB_Print_Argumentos.py
│   └── 03_LAB_Formato_Salida.py
│
├── seccion2_literales/
│   └── 01_LAB_Literales_Cadenas.py
│
├── seccion3_operadores/
│   ├── 01_LAB_Ejs_Operadores.py
│   └── operadores.md
│
└── seccion4_variables/
    ├── 01_LAB_Variables.py
    ├── 02_LAB_Var_ConvSimple.py
    ├── 03_LAB_Operadores_Expresiones.py
    └── 04_LAB_Ejs_Algoritmos.py
```

---

# Contenido

| Sección | Temas desarrollados |
|----------|---------------------|
| **Sección 1 - Hola Mundo** | Función `print()`, argumentos `sep` y `end`, caracteres de escape y formato de salida. |
| **Sección 2 - Literales** | Enteros, flotantes, notación científica, cadenas de texto y valores booleanos. |
| **Sección 3 - Operadores** | Operadores aritméticos, prioridad de operadores, división entera, módulo y exponenciación. |
| **Sección 4 - Variables** | Declaración de variables, operadores abreviados, convertidor simple, expresiones y ejercicios de algoritmos. |

---

# Ejercicios de operadores matemáticos

La carpeta **`seccion3_operadores`** contiene la solución de los ejercicios propuestos sobre operadores aritméticos.

Además, el archivo **`operadores.md`** documenta el desarrollo paso a paso de cada ejercicio, explicando la prioridad de operadores y el procedimiento seguido para obtener cada resultado.

## Jerarquía de operadores utilizada

Todos los ejercicios fueron resueltos aplicando el orden de precedencia definido por Python:

1. Paréntesis `()`
2. Exponenciación `**`
3. Multiplicación `*`, división `/`, división entera `//` y módulo `%`
4. Suma `+` y resta `-`

---

## Ejemplo 1

Expresión:

```python
5 + 3 * 2
```

Resultado:

```python
>>> print(5 + 3 * 2)
11
```

**Explicación:**

Primero se realiza la multiplicación (`3 * 2 = 6`) y posteriormente la suma (`5 + 6 = 11`).

---

## Ejemplo 2

Expresión:

```python
5 * 2 ** 3
```

Resultado:

```python
>>> print(5 * 2 ** 3)
40
```

**Explicación:**

La exponenciación tiene mayor prioridad, por lo que primero se calcula `2 ** 3 = 8`. Después se realiza la multiplicación (`5 * 8 = 40`).

---

> El desarrollo completo de los ejercicios se encuentra documentado en el archivo **`seccion3_operadores/operadores.md`**.

---

# Cómo ejecutar los programas

1. Tener instalado **Python 3.13** o una versión superior.
2. Abrir una terminal ubicada en la raíz del proyecto.
3. Ejecutar el archivo deseado.

Ejemplo:

```bash
python fundamentos_python/src/EV01_Fundamentos/seccion1_hola_mundo/01_LAB_Funcion_Print.py
```

Cada archivo puede ejecutarse de forma independiente.

---

# Herramientas utilizadas

- Python 3
- Visual Studio Code
- Git
- GitHub

---

# Autor

**Kelly Johana Lopera Chica**

Aprendiz del programa **Tecnólogo en Análisis y Desarrollo de Software (ADSO)**

**Servicio Nacional de Aprendizaje (SENA)**