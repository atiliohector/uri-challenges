couting = 0
time = 0

while True:
    
    number = float(input('Number: '))
    time += 1

    if number>0:
        couting +=1
    
    if time == 6:
        print('{}'.format(couting))
        break