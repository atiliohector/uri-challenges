N = int(input())

for i in range(N):
    x = [float(i) for i in input().split()]
    a = x[0]
    b = x[1]
    c = x[2]

    resultado = ((a*2)+(b*3)+(c*5))/10
    print(resultado)