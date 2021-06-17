while True:

    a,b = [int(i) for i in input().split()]


    if a > b:
        print('Decrescente')
    elif b > a:
        print('Crecente')
    elif a == b:
        break