# Python Backend

Repositorio correspondiente a las evidencias de la actividad **GA1-220501093-04-AA1-EV01 – Fundamentos de Python: variables, operadores y manipulación de cadenas**, del programa Tecnólogo en Análisis y Desarrollo de Software (SENA).

## Estructura del repositorio

fundamentos_python/
  src/
    puntaje_final_jugador.py
    EV01_Fundamentos/
      seccion1_hola_mundo/
        01_LAB_Funcion_Print.py
        02_LAB_Print_Argumentos.py
        03_LAB_Formato_Salida.py
      seccion2_literales/
        01_LAB_Literales_Cadenas.py
      seccion3_operadores/
        01_LAB_Ejs_Operadores.py
        operadores.md
      seccion4_variables/
        01_LAB_Variables.py
        02_LAB_Var_ConvSimple.py
        03_LAB_Operadores_Expresiones.py
        04_LAB_Ejs_Algoritmos.py
    EV02_Control_Funciones/
      seccion1_condicionales/
      seccion2_iterativas/
      seccion3_funciones/

## Contenido

### EV01 - Fundamentos

| Sección | Contenido |
|---|---|
| Sección 1 - Hola Mundo | La función print(), argumentos posicionales y de palabra clave (sep, end), caracteres de escape (\n) |
| Sección 2 - Literales | Enteros, flotantes, notación científica, cadenas (comillas/apóstrofes, escape de comillas), booleanos |
| Sección 3 - Operadores | Operadores aritméticos, prioridad de operadores, paréntesis. Ver documentación detallada abajo |
| Sección 4 - Variables | Creación y uso de variables, operadores abreviados, convertidor de unidades, evaluación de expresiones algebraicas, 16 ejercicios de algoritmos aplicados a un contexto de videojuego |

### EV02 - Control y Funciones
- Estructuras condicionales
- Estructuras iterativas
- Funciones

## Documentación de los ejercicios de operadores matemáticos

Resueltos manualmente y comprobados con Python en seccion3_operadores/operadores.py. El detalle paso a paso de los 15 ejercicios está en seccion3_operadores/operadores.md.

### Lógica utilizada

Todos los ejercicios se resolvieron aplicando la jerarquía de prioridades de Python:

1. Paréntesis () — se resuelven primero.
2. Exponenciación ** — mayor prioridad, con enlazado del lado derecho.
3. Multiplicación *, división /, división entera //, módulo % — misma prioridad, se evalúan de izquierda a derecha.
4. Suma + y resta - — menor prioridad.

### Ejemplo de salida (ejercicio 1)

Expresión: 5 + 3 * 2

Explicación: la multiplicación tiene mayor prioridad que la suma, así que primero se calcula 3 * 2 = 6, y después 5 + 6 = 11.

>>> print(5 + 3 * 2)
11

### Ejemplo de salida (ejercicio 7, con exponenciación)

Expresión: 5 * 2 ** 3

Explicación: la exponenciación tiene la prioridad más alta, así que primero se calcula 2 ** 3 = 8, y después 5 * 8 = 40.

>>> print(5 * 2 ** 3)
40

(El resto de los 15 ejercicios, con su paso a paso completo, está documentado en seccion3_operadores/operadores.md.)

## Cómo ejecutar los programas

1. Tener Python 3 instalado.
2. Ejecutar cualquier script desde la terminal, por ejemplo:
   python fundamentos_python/src/puntaje_final_jugador.py
3. Los scripts que usan input() pedirán datos por consola; escribe un valor numérico y presiona Enter en cada solicitud.

## Autor
Kelly Lopera — Aprendiz, Tecnólogo en Análisis y Desarrollo de Software.