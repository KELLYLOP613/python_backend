# ============================================
# LAB - Ejercicios de Algoritmos (Gameplay)
# Fundamentos de Python - Variables y Operadores
# ============================================

# --- Ejercicio 1: Puntaje total del jugador ---
# NOTA: Este ejercicio también se guarda por separado como puntaje_final_jugador.py (requisito de la guía)
nivel1 = float(input("Puntos obtenidos en el nivel 1: "))
nivel2 = float(input("Puntos obtenidos en el nivel 2: "))
nivel3 = float(input("Puntos obtenidos en el nivel 3: "))
puntaje_total = nivel1 + nivel2 + nivel3
print("Puntaje total del jugador:", puntaje_total)
print()

# --- Ejercicio 2: Tiempo total de juego en segundos ---
horas = float(input("Horas jugadas: "))
minutos = float(input("Minutos jugados: "))
segundos = float(input("Segundos jugados: "))
tiempo_total_segundos = horas * 3600 + minutos * 60 + segundos
print("Tiempo total jugado en segundos:", tiempo_total_segundos)
print()

# --- Ejercicio 3: Daño total causado ---
ataque1 = float(input("Daño causado en el ataque 1: "))
ataque2 = float(input("Daño causado en el ataque 2: "))
ataque3 = float(input("Daño causado en el ataque 3: "))
dano_total = ataque1 + ataque2 + ataque3
print("Daño total causado:", dano_total)
print()

# --- Ejercicio 4: Experiencia total ganada ---
mision1 = float(input("Experiencia ganada en la misión 1: "))
mision2 = float(input("Experiencia ganada en la misión 2: "))
mision3 = float(input("Experiencia ganada en la misión 3: "))
experiencia_total = mision1 + mision2 + mision3
print("Experiencia total acumulada:", experiencia_total)
print()

# --- Ejercicio 5: Porcentaje de vida restante ---
vida_maxima = float(input("Vida máxima: "))
vida_actual = float(input("Vida actual: "))
porcentaje_vida = (vida_actual / vida_maxima) * 100
print("Porcentaje de vida restante:", round(porcentaje_vida, 2), "%")
print()

# --- Ejercicio 6: Oro total recolectado ---
oro1 = float(input("Oro recolectado en la misión 1: "))
oro2 = float(input("Oro recolectado en la misión 2: "))
oro3 = float(input("Oro recolectado en la misión 3: "))
oro_total = oro1 + oro2 + oro3
print("Oro total acumulado:", oro_total)
print()

# --- Ejercicio 7: Velocidad promedio ---
distancia = float(input("Distancia recorrida (metros): "))
tiempo = float(input("Tiempo tomado (segundos): "))
velocidad_promedio = distancia / tiempo
print("Velocidad promedio:", round(velocidad_promedio, 2), "m/s")
print()

# --- Ejercicio 8: Costo total de mejoras ---
mejora1 = float(input("Costo de la mejora 1: "))
mejora2 = float(input("Costo de la mejora 2: "))
mejora3 = float(input("Costo de la mejora 3: "))
costo_total_mejoras = mejora1 + mejora2 + mejora3
print("Costo total de las mejoras:", costo_total_mejoras)
print()

# --- Ejercicio 9: Tiempo restante para completar misión ---
tiempo_total_mision = float(input("Tiempo total de la misión (minutos): "))
tiempo_transcurrido = float(input("Tiempo transcurrido (minutos): "))
tiempo_restante = tiempo_total_mision - tiempo_transcurrido
print("Tiempo restante para completar la misión:", tiempo_restante, "minutos")
print()

# --- Ejercicio 10: Nivel promedio del equipo ---
nivel_jugador1 = float(input("Nivel del jugador 1: "))
nivel_jugador2 = float(input("Nivel del jugador 2: "))
nivel_jugador3 = float(input("Nivel del jugador 3: "))
nivel_promedio = (nivel_jugador1 + nivel_jugador2 + nivel_jugador3) / 3
print("Nivel promedio del equipo:", round(nivel_promedio, 2))
print()

# --- Ejercicio 11: Daño crítico ---
dano_base = float(input("Daño base del ataque: "))
multiplicador_critico = float(input("Multiplicador crítico: "))
dano_critico = dano_base * multiplicador_critico
print("Daño crítico:", dano_critico)
print()

# --- Ejercicio 12: Minutos a horas y minutos ---
tiempo_total_minutos = float(input("Tiempo total jugado (minutos): "))
horas_convertidas = tiempo_total_minutos // 60
minutos_restantes = tiempo_total_minutos % 60
print("Tiempo total jugado:", int(horas_convertidas), "horas y", int(minutos_restantes), "minutos")
print()

# --- Ejercicio 13: Porcentaje de misiones completadas ---
total_misiones = float(input("Número total de misiones: "))
misiones_completadas = float(input("Número de misiones completadas: "))
porcentaje_completado = (misiones_completadas / total_misiones) * 100
print("Porcentaje de misiones completadas:", round(porcentaje_completado, 2), "%")
print()

# --- Ejercicio 14: Costo total de objetos comprados ---
objeto1 = float(input("Costo del objeto 1: "))
objeto2 = float(input("Costo del objeto 2: "))
objeto3 = float(input("Costo del objeto 3: "))
costo_total_objetos = objeto1 + objeto2 + objeto3
print("Costo total de los objetos comprados:", costo_total_objetos)
print()

# --- Ejercicio 15: Tiempo promedio de partidas ---
partida1 = float(input("Tiempo de la partida 1 (minutos): "))
partida2 = float(input("Tiempo de la partida 2 (minutos): "))
partida3 = float(input("Tiempo de la partida 3 (minutos): "))
tiempo_promedio = (partida1 + partida2 + partida3) / 3
print("Tiempo promedio de las partidas:", round(tiempo_promedio, 2), "minutos")
print()

# --- Ejercicio 16: Porcentaje de enemigos derrotados ---
total_enemigos = float(input("Número total de enemigos: "))
enemigos_derrotados = float(input("Número de enemigos derrotados: "))
porcentaje_derrotados = (enemigos_derrotados / total_enemigos) * 100
print("Porcentaje de enemigos derrotados:", round(porcentaje_derrotados, 2), "%")