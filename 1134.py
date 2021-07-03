x = int(input())

gasolina = 0
diesel = 0
alcool = 0

while True:
    if x != 4:
        x = int(input('Digite de novo: '))
        if x == 1:
            alcool+=1
        elif x == 2:
            gasolina +=1
        elif x == 3:
            diesel +=1
    elif x == 4:
        print('MUITO OBRIGADO')
        print('Alcool = {}'.format(alcool))
        print('Gasolina = {}'.format(gasolina))
        print('Diesel = {}'.format(diesel))
        break