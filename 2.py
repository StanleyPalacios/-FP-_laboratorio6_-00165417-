numero=int(input("numero n: "))

numcol=0

while numcol<numero:
    fila=numcol+1
    cont=0
    m=""
    while(cont<fila):
        m=m+str(numcol+1)+" " # si no necesitas el espacio, seria m=m+str(numcol+1)
        cont+=1
    print(m) 
    numcol=numcol+1
