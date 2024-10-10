correo = str(input("Introduce tu correo electronico: "))

nombre = correo.split("@")[0]

nuevocorreo = nombre + "@ceu.es"

print("Tu correo electronico ahora es:", nuevocorreo)