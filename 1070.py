x = int(input())

quantity = 0
time = 0

while True:

    time += 1

    if (x+time) % 2 != 0:
        print(x+time)
        quantity +=1
        if quantity == 6:
            print('over')
            break