couting = 0
time = 0

while True:
    number = int(input())
    time +=1

    if number%2==0:
        couting += 1

    if time == 5:
        print('{} sao pares'.format(couting))
        break
