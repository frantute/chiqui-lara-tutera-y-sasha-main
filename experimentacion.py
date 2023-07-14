from llaves import ronda
from chiqui import partidos



dic = {"San Lorenzo": 0, "Boca": 0, "River": 0, "Racing": 0, "Independiente": 0, "Estudiantes de Caseros": 0, "Velez": 0, "Ferro": 0}

media = [("San Lorenzo", 40), ("Boca", 95), ("River", 90), ("Racing", 70), ("Independiente", 80), ("Estudiantes de Caseros", 30), ("Velez", 20), ("Ferro", 10)]

equipos = []
for i in media:
     equipos.append([i[0],0,0,0])


tipo_torneo = int(input("Ingrese:\n1 para simular una liga\n2 para simular un torneo de llaves por eliminación\n3 para simular un torneo de llave ida y vuelta\n4 para simular una tanda de penales "))

# if tipo_torneo == 1:
#      for _ in range(1000):
#          tabla_final = ronda(media)
#          rondas = ronda(media)
#          print(tabla_final)
#          print(f"El ganador es: {rondas[0][0]}")
#          dic[rondas[0][0]] += 1
#          print(dic)
# elif tipo_torneo == 2:
#      for _ in range(1000):
#          ganador = ronda(media)
#          print(f"El ganador es: {ganador[0]}")
#          dic[ganador[0]] += 1
#          print(dic)
if tipo_torneo == 1:
     print(media)
     for _ in range(1000):
         tabla_final = partidos(equipos,media)
         print(f"El ganador es: {tabla_final[0][0]}")
         dic[tabla_final[0][0]] += 1
         for fila in equipos:
             fila[1],fila[2],fila[3] = 0,0,0
             print(dic)
elif tipo_torneo == 2:
     for _ in range(1000):
         ganador = partidos(equipos,media)
         print(f"El ganador es: {ganador[0]}")
         dic[ganador[0]] += 1
         print(dic)
        
#elif tipo_torneo == 3:
 #   for _ in range(1000):
  #      ganador = simular_llaves_ida_vuelta(equipos)
   #     print(f"El ganador es: {ganador[0]}")
    #    dic[ganador[0]] += 1
     #   print(dic)
#elif tipo_torneo == 4:
 #   for _ in range(1000):
  #      ganador = simular_penales()
   #     print(f"El ganador es: {ganador}")
    #    dic[ganador[0]] += 1
     #   print(dic)


