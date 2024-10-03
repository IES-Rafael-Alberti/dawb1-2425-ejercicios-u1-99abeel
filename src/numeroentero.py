def comprobar_entero(cadena):
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())

    
def dame_entero():
    cadena = input("Escribe un numero entero: ").strip()
   
    while not comprobar_entero(cadena):
        cadena = input("ERROR, eso no es un entero\n\n Escribe un numero entero otra vez: ").strip()
    return int(cadena)
     

def main():
    num = dame_entero
    print(f"Has introducido el numero {num}")
   
if __name__ =="__main__":
    main()