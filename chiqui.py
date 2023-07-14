 #Importo la librería random como rnd
import random as rnd

# Función Auxiliar 1
# Esta función la usa goles
# Toma dos equipos, que son una lista o tupla de dos elementos: el primero es el nombre del equipo y el segundo es la efectividad.
# Devuelve una tupla de tres elementos: el primero es la probabilidad de que meta gol el equipo A, el segundo la probabilidad de que no haya goles y el tercero la probabilidad de que meta gol el equipo B.

equipos  = [
       ["River", 0, 0, 0], 
       ["Racing", 0, 0, 0], 
       ["Boca", 0, 0, 0], 
       ["San Lorenzo", 0, 0, 0], 
       ["Independiente", 0, 0, 0], 
       ["Talleres", 0, 0, 0], 
       ["Defensores", 0 , 0, 0], 
       ["Ferro", 0, 0, 0]]

media = [
       ["River", 80], 
       ["Racing", 78], 
       ["Boca", 83], 
       ["San Lorenzo", 75], 
       ["Independiente", 81], 
       ["Talleres", 70], 
       ["Defensores", 73], 
       ["Ferro", 68]]

#Sh - No se si es el mejor nombre
def partidos(equipos,media):
    num_jugadas = 4
    for local in range(len(equipos)):
        lista = equipos[local]
        for visitante in range(local + 1, len(equipos)):
            ganaA = 0
            ganaB = 0
            for jugadas in range(num_jugadas):
                jugada = goles(media[local], media[visitante])
                if jugada == "A":
                    ganaA += 1
                    equipos[visitante][3]+=1
                    equipos[local][2]+=1
                
                elif jugada == "B":
                    ganaB +=1
                    equipos[local][3]+=1
                    equipos[visitante][2]+=1
            print(f"{equipos[local][0]}{ganaA}:{ganaB}{equipos[visitante][0]}")
            if ganaA > ganaB:
                equipos[local][1]+=3

            elif ganaA < ganaB:
                equipos[visitante][1]+=3
            
            else:
                equipos[local][1]+=1
                equipos[visitante][1]+=1
    equipos = ordenar_tabla(equipos)
    return equipos

#LLAVES

def probabilidades_de_gol(equipoA, equipoB):
    _,probabilidadA = equipoA
    _,probabilidadB = equipoB
    # Pa * (1 - Pb)
    golA = probabilidadA/100 * (1-probabilidadB/100)
    # Pb * (1 - Pa)
    golB = probabilidadB/100 * (1-probabilidadA/100)
    # 1 - PgolA - PgolB
    empate = 1 - golA - golB
    return golA, empate, golB

#Función Auxiliar 1
# Toma dos equipos, que son una lista o tupla de dos elementos: el primero es el nombre del equipo y el segundo es la efectividad.
# Devuelve A si mete gol A, B si mete gol B, E si no mete gol ninguno.
def goles(equipoA,equipoB):
    victoriaA, empate, victoriaB = probabilidades_de_gol(equipoA, equipoB)
    resultado = rnd.choices(["A", "E", "B"], [victoriaA, empate, victoriaB])[0]
    return(resultado)

#Funcion Auxiliar 2
#Esta función se usa en ordenar_tabla, ignorar
def orden_en_tabla(equipo):
    _,puntos,GF,GC = equipo
    return puntos, GF-GC, GF

#Esta es la función que van a usar: Toma una tabla de posiciones y la ordena de mayor a menor según los criterios de desempate.
#La tabla de posiciones es una lista de listas, donde cada lista interna tiene cuatro elementos: el primero es el nombre del equipo, el segundo es la cantidad de puntos, el tercero es la cantidad de goles a favor y el cuarto es la cantidad de goles en contra.
def ordenar_tabla(tabla):
    return sorted(tabla, key=orden_en_tabla, reverse=True)


#print(partidos(equipos))