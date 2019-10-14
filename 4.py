#Este es un juego de adivinar el número
import random

intentos=0

print('¡Hola! ¿Cuál es tu nombre?')
nombre = input()

numero=random.randint(1,10)
print('Bueno, '+nombre+', piensa un número entre 1 y 10.')

while intentos<3:
    print ('¡Adivínalo! Tienes 3 intentos')
    adivina=input()
    adivina=int(adivina)

    intentos=intentos+1
   
    if adivina<numero:
        print ('¡Demasiado pequeño!')

    if adivina>numero:
        print('¡Demasiado grande!')

    if adivina==numero:
        break

if adivina==numero:
    intentos=str(intentos)
    print('Fabuloso, '+nombre+', acertaste el número en '+intentos+' intentos. ¡Estarás orgulloso-a!')

if adivina!=numero:
    numero=str(numero)
    print('¡Qué fatalidad '+nombre+' ! Yo estaba pensando en el número '+numero)
  
