import random
from llaves import ronda
from chiqui import partidos


media = [("Argentina",95), ("Brasil", 80), ("Alemania", 70), ("España", 65), ("Uruguay", 79), ("Francia", 86), ("Italia", 68), ("Inglaterra", 83), ("Dinamarca", 66), ("Estados Unidos", 64), ("Colombia", 74), ("Peru", 60), ("Croacia", 77), ("Portugal", 75), ("Belgica", 63), ("Canada", 92) ]

dic = {"Argentina": 0, "Brasil": 0, "Alemania": 0, "España": 0, "Uruguay": 0, "Francia": 0, "Italia": 0, "Inglaterra": 0, "Dinamarca": 0, "Estados Unidos": 0, "Colombia": 0, "Peru": 0, "Croacia": 0, "Portugal": 0, "Belgica": 0, "Canada": 0}

tipo_torneo = int(input("Ingrese:\n1 para simular una liga\n2 para simular un torneo de llaves por eliminación\n3 para simular un torneo de llave ida y vuelta\n4 para simular una tanda de penales "))

equipos = []
for i in media:
     equipos.append([i[0],0,0,0])

for i in range(4):
          inicio = i * 4
          fin = inicio + 4
          valores = equipos[inicio:fin]
          empate = 0
          ganar = 0
          perder = 0
          if tipo_torneo == 1:
           print(media)
           for _ in range(1):
             tabla_final = partidos(valores,media)
             # nos falta saber si empata o gana para hacer la parte de la clasificacion
             print(f"El ganador es: {tabla_final[0][0]}")
             dic[tabla_final[0][0]] += 1
             for fila in valores:
                 fila[1],fila[2],fila[3] = 0,0,0
                 print(dic)
         
         
          # elif tipo_torneo == 2:
          #   for _ in range(3):
          #    ganador = partidos(valores,media)
          #    print(f"El ganador es: {ganador[0]}")
             
          #    dic[ganador[0]] += 1
          #    print(dic)
     