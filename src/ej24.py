precio = (input("Introduce el precio del producto con 2 decimales: "))

euros = precio.split(",")[0]

centimos = precio.split(",")[1]

print("El precio del producto es de", euros, "euros y", centimos, "centimos")
