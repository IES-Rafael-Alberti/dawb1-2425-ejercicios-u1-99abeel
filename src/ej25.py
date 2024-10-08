fecha = input("introduce tu fecha de nacimiento en formato dd/mm/aaaa: ")

dia = fecha.split("/")[0]

mes = fecha.split("/")[1]

año = fecha.split("/")[2]

print ("Naciste el dia", dia, ",en el mes", mes, "y en el año", año)