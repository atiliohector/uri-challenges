N = int(input())

for i in range(1,N+1):
    if i % 2 == 0:
        resultado = (i**2)
        print('{} * 2 = {}'.format(i, resultado))