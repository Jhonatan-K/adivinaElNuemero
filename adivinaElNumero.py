from random import randint

print(end='.:Bienvenido:.\nAdivina el numero que estoy pensando!')

NumRange = randint(0,100)

numberAttemps = 0

whatIsTheNumber = int(input('Adivina el numero de 0 a 100 -> '))
print()
while whatIsTheNumber>=0:
    if whatIsTheNumber>NumRange:
        print(f'{whatIsTheNumber} Es mayor, sigue intentando')
        print()
        whatIsTheNumber = int(input('Adivina el numero de 0 a 100 -> '))
        numberAttemps += 1
    elif whatIsTheNumber<NumRange:
        print(f'{whatIsTheNumber} Es menor, sigue intentando')
        print()
        whatIsTheNumber = int(input('Adivina el numero de 0 a 100 -> '))
        numberAttemps += 1
    elif whatIsTheNumber==NumRange:
        print()
        print(f'{whatIsTheNumber} Es el numero!')
        break
print()
print(f'sus numero de intentos fueron {numberAttemps}')
print('Fin del juego')