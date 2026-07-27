# Creamos las variables y les asignamos el número de manzanas de cada persona
juan = 3
maria = 5
adam = 6

# Imprimimos las tres variables en una línea, separadas por coma
print(juan, maria, adam, sep=",") 

# Creamos una nueva variable que suma las tres anteriores
total_apples = juan + maria + adam 

# se imprime el resultado de la suma
print(total_apples)


# Experimentando con más variables y operaciones aritméticas
diferencia = adam - juan      # resta
promedio = total_apples / 3   # división (resultado flotante)
doble_maria = maria * 2       # multiplicación

print("Diferencia entre Adán y Juan:", diferencia)
print("Promedio de manzanas:", promedio)
print("El doble de las manzanas de María:", doble_maria)

# Combinando cadena y entero con el operador +
# OJO: esto dará error, porque + no puede unir una cadena con un número directamente
# print("Número total de manzanas: " + total_apples)

# Formas correctas de combinarlos:
print("Número total de manzanas:", total_apples)              # con coma (concatena con espacio)
print("Número total de manzanas: " + str(total_apples))       # convirtiendo el número a texto con str()