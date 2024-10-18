n = int(input("Numero de barras vendidas que no son del día: "))

pan = 3.49

panhoy = pan * n


print("El precio habitual de la barra es de", pan, "y si no es del día tiene un descuento del 60%")

panmalo = panhoy * (60/100)

print("el coste total de las barras no frescas es de", round(panmalo,2))
