# En el primer print() tenemos 3 argumentos (palabras).
# Usamos sep="***" para que Python separe esas palabras con *** en lugar del espacio que usa por defecto.
# Usamos end="..." para que, en lugar del salto de línea que print() agrega por defecto al terminar, imprima "..." y continúe en la misma línea.
print("Programming", "Essentials", "in", sep="***", end="...")

# Como el print() anterior no envió un salto de línea, esta palabra se imprime justo a continuación, en la misma línea.
print("Python")