 #Importo la librería random como rnd
import random as rnd
from tkinter import E

# Función Auxiliar 1
# Esta función la usa goles
# Toma dos equipos, que son una lista o tupla de dos elementos: el primero es el nombre del equipo y el segundo es la efectividad.
# Devuelve una tupla de tres elementos: el primero es la probabilidad de que meta gol el equipo A, el segundo la probabilidad de que no haya goles y el tercero la probabilidad de que meta gol el equipo B.

equipos = [
       ["River", 80], 
       ["Racing", 78], 
       ["Boca", 83], 
       ["San Lorenzo", 75], 
       ["Independiente", 81], 
       ["Talleres", 70], 
       ["Defensores", 73], 
       ["Ferro", 68]]

def jugarPartidos(equipo1, equipo2):
        ganaA = 0
        ganaB = 0
        #Sh - Se podría separar la lógica del partido en más funciones
        for jugadass in range(4):
            jugada = goles(equipo1, equipo2)
            
            if jugada == "A":
                ganaA += 1
                                
            elif jugada == "B":
                ganaB +=1
        
        if ganaA == ganaB:
            for jugadas in range(2):
                jugada = goles(equipo1, equipo2)
                
                if jugada == "A":
                    ganaA += 1
                                
                elif jugada == "B":
                    ganaB +=1
                
            while ganaA == ganaB:
                    jugada = goles(equipo1, equipo2)
                    if jugada == "A":
                        ganaA += 1              
                    elif jugada == "B":
                        ganaB +=1
        return (ganaA,ganaB)

def ronda(equipos):
    rondas = equipos

    while len(rondas) > 1:   
        segunda_ronda = []
        for equipo1 in range(0,len(rondas),2):
            equipo2 = equipo1 + 1
            golesLosDos = jugarPartidos(rondas[equipo1],rondas[equipo2])
            ganaA = golesLosDos[0]
            ganaB = golesLosDos[1]

                        
            if ganaA > ganaB:
                segunda_ronda.append(rondas[equipo1])

            elif ganaA < ganaB:
                segunda_ronda.append(rondas[equipo2])
            #Sh - Borren esto después, era para debuggear
            else:
                print("Si están leyendo esto, hay un bug")

        print(segunda_ronda)
        rondas = segunda_ronda

    return segunda_ronda

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

print("GANADOR: ")
print(ronda(equipos))