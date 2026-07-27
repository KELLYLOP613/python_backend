# La palabra "Estoy" tiene 1 comilla a cada lado, "aprendiendo" tiene 2, y "Python" tiene 3.
# Al escribirlas seguidas sin espacios, las comillas de cierre de una palabra
# se juntan con las de apertura de la siguiente (1+2=3 comillas, luego 2+3=5 comillas).
# Usamos apóstrofes para delimitar toda la cadena, así no hace falta escapar
# ninguna de las comillas dobles que están dentro del texto.
print('"Estoy"""aprendiendo"""""Python"""')

# ALTERNATIVA: el mismo resultado se puede lograr delimitando con comillas dobles
# y escapando cada una de las comillas internas con \" para que Python las
# interprete como parte del texto y no como el cierre de la cadena.
# print("\"Estoy\"\"\"aprendiendo\"\"\"\"\"Python\"\"\"")