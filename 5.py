saldo=1000

print(" \t.:menu:")
print("1 - ingresar dinero en la cuenta")
print("2 - retirar dinero de la  cuenta")
print("3 - mostrar dinero disponible")
print("4 -  salir")
opcion=int(input("digite una opcion del menu :"))

print()

if opcion==1:
    extra=float(input("cuanto dinero desea ingresar"))
    saldo+= extra
    print("dinero de la cuenta:{saldo} ")
    
elif opcion==2:
        retirar =float(input("cuanto dinero desea retirar"))
        if retirar>saldo:
            print("no tiene esa cantidad de dinero")
        else:
            saldo-=retirar
            print("dinero de la cuenta: {saldo}")
elif opcion==3:
    print("dinero de la cuenta: {saldo}")
    
elif opcion==4:
    print("gracias")
else:
    print("error se equivoco de opcion de menu")
    
