
segundos = int (input ("Por favor, entre com o número de segundos que deseja converter:"))
dias = segundos // 86400
horas = segundos % 86400 // 3600
segundos_restantes = segundos % 3600
minutos = segundos_restantes //60
segundos = segundos_restantes % 60


print (dias, "dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")