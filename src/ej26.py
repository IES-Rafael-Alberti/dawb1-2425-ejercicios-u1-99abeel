lista = (input("Introduce los productos de una cesta de la compra: "))

productos = lista.split(",")

print("\nProductos en la cesta: \n")
for nproductos in productos: 
    print(nproductos.strip())


