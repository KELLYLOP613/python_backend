# Pruebas realizadas:
# x = 0  -> y = -1.0
# x = 1  -> y = 3.0
# x = -1 -> y = -9.0   (esta es la que se ejecuta actualmente)

x = -1 # dato del valor x de la función
x = float(x) # se convierte en float

# Expresión a evaluar: 3x3 - 2x2 + 3x - 1
# La exponenciación (**) tiene la prioridad más alta de todos los operadores, por eso x**3 y x**2 se calculan ANTES que las multiplicaciones por 3 y 2,
# sin necesidad de agregar paréntesis para forzar ese orden.
y = 3*x**3 - 2*x**2 + 3*x - 1

print("y =", y)