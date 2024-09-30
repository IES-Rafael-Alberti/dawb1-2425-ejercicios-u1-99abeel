peso = int(input("Escribe tu peso en KG: "))

altura = float(input("Escribe tu estatura en metros: "))

imc = peso / (altura)**2

print("Tu índice de masa corporal es: ", round(imc,2))