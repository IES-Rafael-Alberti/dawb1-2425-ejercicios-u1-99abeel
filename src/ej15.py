capital = float(input("Introduzca la cantidad que desea depositar: "))

interes = 4 / 100

interes1 = capital * (interes)

interes2 = interes1 * (interes)

interes3 = interes2 * (interes)

print("El dinero generado el primer año será", round(interes1,2), ", el segundo año será", round(interes2,2), "y el tercer año será", round(interes3,2))