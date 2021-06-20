a = int(input())

for i in range(a):
    x,y = [int(i) for i in input().split()]

    if y == 0:
        print('Impossivel de calcular')
    elif x == 0:
        print(0.0)
    elif x and y:
        result = x/y
        print(result)