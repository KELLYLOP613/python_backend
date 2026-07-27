#reduciendo el número de print usando el salto de línea \n
print("    *\n   * *\n  *   *\n *     *")
print("***   ***\n  *   *\n  *   *\n  *****")

#flecha el doble de grande
print("        *")
print("       * *")
print("      *   *")
print("     *     *")
print("    *       *")
print("   *         *")
print("  *           *")
print(" *             *")
print("***          ***")
print("  *          *")
print("  *          *")
print("  *          *")
print("  *          *")
print("  ************")

#Duplicar la flecha usando el *2 en cadena de caracteres
print(("    *    ")*2)
print(("   * *   ")*2)
print(("  *   *  ")*2)
print((" *     * ")*2)
print(("***   ***")*2)
print(("  *   *  ")*2)
print(("  *   *  ")*2)
print(("  *****  ")*2)

#Eliminación comilla
#print((  *****  ")*2) si se elimina la primer comilla python resalta el error en la segunda comilla 

#Eliminación parentesis
#print("  *****  ")*2) si se elimina uno de los parentesiis python reslta el parentesis restante 

#Print no es una palabra reservada por lo tanto la toma como una variable sale NameError: name 'Print' is not defined Did you mean: 'print'?
#Python distingue las mayusculas y minusculas

#print((’  *****  ")*2) al usar el apostrofe directamente la comilla queda como la inicial y resalta el resto del texto. SyntaxError: unterminated string literal
# Al no cerrar con el mismo símbolo de apertura, la cadena nunca termina correctamente.