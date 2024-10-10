frase = str(input("Introduce una frase: "))

vocal = str(input("Introduce una vocal: "))

frasem = frase.replace(vocal.lower(), vocal.upper())

print("La frase es:", frasem)