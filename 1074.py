N = int(input())

for i in range(N):
    x = int(input())

    if x %2 ==0:
        print('EVEN')
    elif x %2 !=0:
        print('ODD')
    elif x > 0:
        print('POSITIVE')
    elif x < 0:
        print('NEGATIVE')
    elif x == 0:
        print('EVEN NULL')