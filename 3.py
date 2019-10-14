def main():
    print("CUENTA PARES (1)")
    numero = int(input("Escriba un número par: "))
    while numero % 2 != 0:
        numero = int(input(f,"{numero} no es un número par. Inténtelo de nuevo: "))
    contador = 1
    respuesta = input("¿Quiere escribir otro número par? (S/N): ")
    while respuesta == "S" or respuesta == "s":
        numero = int(input("Escriba un número par: "))
        while numero % 2 != 0:
            numero = int(input(f,"{numero} no es un número par. Inténtelo de nuevo: "))
        contador += 1
        respuesta = input("¿Quiere escribir otro número par? (S/N): ")
        print()
    if contador == 1:
        print("Ha escrito 1 número par.")
    else:
        print(f,"Ha escrito {contador} números pares.")


if __name__ == "__main__":
    main()
